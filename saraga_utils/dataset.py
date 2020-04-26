import numpy as np
import pandas as pd
import os
import json
from compmusic import dunya as dn
from saraga_utils import meta
from saraga_utils.utils import download_file

class Dataset:
    """
    Dataset class that perform fetching operations for one dataset
    """

    def __init__(self, tradition_slug, api_token=None):
        """
        Init the class...
        :param tradition_slug: str
            Slug of the tradition to be set for processing (dunya-carnatic-cc or dunya-hindustani-cc).
        """
        # setting api token first
        if not api_token:
            raise Exception("API token not provided")
        else:
            dn.set_token(api_token)

        if tradition_slug not in meta.info.keys():
            raise Exception("Wrong tradition slug specified")

        # setting the info for the tradition
        self.info = meta.info[tradition_slug]
        # reading metadata info (just a mapping of needed info)
        self.__read_metadata_info(tradition_slug)
        # reading file info (just a mapping of needed info)
        self.__read_file_info(tradition_slug=tradition_slug)

        # init some needed variables
        self.metadata_stats = None
        self.file_stats = None
        self.recs = None
        self.rec_infos = None

    def get_mbids(self):
        """
        fetches mbids in the dataset
        """
        # first setting the collection
        self.info['tradition_dunya'].set_collections([self.info['tradition_id']])

        # fetching mbids in one shot
        if self.recs is None:
            self.recs = self.info['tradition_dunya'].get_recordings()
        return [r['mbid'] for r in self.recs]

    def compute_metadata_stats(self):
        """
        Fetches number of different "unique" entities link to all the recordings of a collection
        This function also returns total length of the recordings in the collection
        """
        # first lets set the collection
        self.info['tradition_dunya'].set_collections([self.info['tradition_id']])
        # fetching metadata info for all the recordings
        if self.rec_infos is None:
            self.rec_infos = self.info['tradition_dunya'].get_recordings(recording_detail=True)

        entities = self.cmap['entities']
        stats = dict(zip(entities, [[] for e in entities]))
        # iterating over each recording and appending stats
        for rec_info in self.rec_infos:
            for e in entities:
                if e in rec_info:
                    if e == 'artists':
                        temp = [x['artist'] for x in rec_info[e]]
                        stats[e].extend([x[self.cmap['id_mapping'][e]] for x in temp])
                    elif e == 'length':
                        stats[e].append(rec_info[e])
                    else:
                        stats[e].extend([x[self.cmap['id_mapping'][e]] for x in rec_info[e]])
        stats.update(dict(num_mbids=len(self.rec_infos)))
        self.metadata_stats = stats

    def get_metadata_stats(self):
        """
        Essentially a getter function for the metadata stats
        :return:
        """
        if self.metadata_stats is None:
            print("Computing metadata stats now...")
            self.compute_metadata_stats()
        return self.metadata_stats

    def print_metadata_stats(self):
        """
        Function to print the stats (this could be converted to pretty printing)
        :return:
        """
        if self.metadata_stats is None:
            print("Metadata stats were not computed, computing them now...")
            self.compute_metadata_stats()
        print('----------------------------------------')
        print("Stats for %s tradition:" % self.info['tradition_name'])
        for ent, nums in self.metadata_stats.items():
            if ent == 'num_mbids':
                print("Total number of recordings %d" % nums)
            elif ent != 'length':
                print("Total number of unique %s are:%d" % (ent, len(set(nums))))
            else:
                print("Total length of the recordings: %0.2f hrs" % (np.sum(nums) / 3600000.))


    def compute_file_stats(self):
        """
        This function computes stats of different file types in the dataset
        :return:
        """
        print("This function might take some time...")

        # setting the collection
        self.info['tradition_dunya'].set_collections([self.info['tradition_id']])

        # fetching all recordings in the collection
        if self.recs is None:
            self.recs = self.info['tradition_dunya'].get_recordings()

        slugs = self.file_info.thetype.unique()

        output = []
        for rec in self.recs:
            mapp = {}
            try:
                content = dn.document(rec['mbid'])
                df = pd.DataFrame(index=slugs, data={'col1': np.zeros(len(slugs))})
                inds1 = set(content['sourcefiles']).intersection(set(slugs))
                inds2 = set(content['derivedfiles'].keys()).intersection(set(slugs))
                df.loc[inds1] = 1
                df.loc[inds2] = 1
                mapp.update(df.to_dict('dict')['col1'])
                mapp.update(dict(mbid=rec['mbid']))
            except:
                print("Issue with: %s, %s"%( self.info['tradition_name'], rec['mbid']))
            output.append(mapp)
        self.file_stats = pd.DataFrame(output)

    def get_file_stats(self):
        """
        Getter for file stats
        :return:
        """
        if self.file_stats is None:
            print("Computing file stats now...")
            self.compute_file_stats()
        return self.file_stats

    def print_file_stats(self):
        """
        Printing file stats
        :return:
        """
        if self.file_stats is None:
            print("File stats are not computed, computing them now...")
            self.compute_file_stats()
        for file_type, group in self.file_info.groupby('file_type'):
            print("-------------------------------------------------------------")
            print("-------------------------------------------------------------")
            print("These are the stats for %s type of files"%file_type)
            cols = group.thetype.unique()
            print(self.file_stats[cols].sum().to_markdown())

    def download_files(self, dir_name, overwrite=False, file_types=[], thetype=[]):
        """
        Download files in the datasets.
        To know what different types of files exists in the dataset use explain_filetypes() function
        You can choose to download only certain type of files.

        :param dir_name: str
            Directory where the downloaded files are to be dumped
        :param overwrite: bool
            Whether or not to overwrite existing files
        :param file_types: array
            Array of file types to be processed. Default: all the file types will be downloaded
        :return:
        """

        # setting the collection
        self.info['tradition_dunya'].set_collections([self.info['tradition_id']])
        if self.rec_infos is None:
            self.rec_infos = self.info['tradition_dunya'].get_recordings(recording_detail=True)

        # if no file type is specified, populate every type
        if len(file_types)==0:
            file_types = self.file_info.file_type.unique()

        # if no thetype filter is specified, we fetch all possible thetypes present in chosen file_type
        if len(thetype)==0:
            thetype = self.file_info[self.file_info.file_type.isin(file_types)].thetype.unique()

        # iterate over each recording mbid and process the download
        for rec_info in self.rec_infos:
            # fetching names (since we need them for create apt folder structure)
            release = rec_info[self.cmap['release']][0]['title']
            recording = rec_info['title']
            artist = rec_info['album_artists'][0]['name']

            # sometimes release and recording names contain strange chars like "/"
            release = release.replace("/", "_")
            recording = recording.replace("/", "_")
            artist = artist.replace("/", "_")

            file_dir = os.path.join(dir_name, self.info['tradition_name'], "%s by %s" % (release, artist), recording)
            if not os.path.isdir(file_dir):
                os.makedirs(file_dir)

            # dumping json file for the metadata
            json.dump(rec_info, open(os.path.join(file_dir, recording + '.json'), 'w'))

            # downloading stuff from the server
            for index, row in self.file_info[self.file_info.file_type.isin(file_types)].iterrows():
                ext = ".%s.%s" % (row['thetype'], row['content_type'])
                file_path = os.path.join(file_dir, recording + ext)
                if not (os.path.isfile(file_path) and not overwrite):
                    try:
                        if row['thetype'] in thetype:
                            download_status = download_file(rec_info['mbid'], row['thetype'], row['subtype'], file_path)
                    except Exception as e:
                        print("File downloading failed for tradition: %s, mbid: %s, thetype: %s, subtype: %s" % (
                        self.info['tradition_name'], rec_info['mbid'], row['thetype'], row['subtype']))

    def explain_filetypes(self):
        """
        This function explains different types of file types in the dataset
        :return:
        """
        if self.file_info.file_type.nunique()<1:
            print("There's something wrong...")
            return

        print("There are %d types of file types in this collection"%self.file_info.file_type.nunique())
        for file_type, group in self.file_info.groupby('file_type'):
            print('------------')
            print('File type: %s'%file_type)
            print("There are %d types of files within this file type."%group.thetype.nunique())
            for thetype, group1 in group.iterrows():
                print('Slug of the file: %s\t\t, description: %s'%(group1.thetype, group1.description))
            print('------------')

    def __read_metadata_info(self, tradition_slug):
        self.cmap = meta.concept_mapp[tradition_slug]

    def __read_file_info(self, tradition_slug):
        self.file_info = meta.content_info[tradition_slug]

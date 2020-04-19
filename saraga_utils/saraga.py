from compmusic import dunya as dn
from saraga_utils import meta
import numpy as np
import pandas as pd
import os
import json


def download_file(mbid, thetype, subtype, file_path):
    """
    Utility function (wrapper) to download a file
    """
    try:
        content = dn.file_for_document(mbid, thetype, subtype)

        if thetype == 'pitch':
            content = json.loads(content)
            np.savetxt(file_path, content, delimiter='\t')
        else:
            fid = open(file_path, 'wb')
            fid.write(content)
            fid.close()
    except Exception as e:
        raise e
    return True

class Dataset():

    def __init__(self, tradition_slug):
        self.info = meta.info[tradition_slug]
        self.__read_metadata_info(tradition_slug)
        self.__read_file_info(tradition_slug=tradition_slug)

    def get_mbids(self):
        """
        fetches mbids in the dataset
        """
        self.info['tradition_dunya'].set_collections([self.info['tradition_id']])
        recs = self.info['tradition_dunya'].get_recordings()
        return [r['mbid'] for r in recs]

    def __read_file_info(self, tradition_slug):
        self.file_info = meta.content_info[tradition_slug]

    def compute_file_stats(self):

        self.info['tradition_dunya'].set_collections([self.info['tradition_id']])
        recs = self.info['tradition_dunya'].get_recordings()

        slugs = self.file_info.thetype.unique()

        output = []
        for rec in recs[:20]:
            try:
                content = dn.document(rec['mbid'])
                mapp = {}
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

    def print_file_stats(self):

            for file_type, group in self.file_info.groupby('file_type'):
                print("-------------------------------------------------------------")
                print("-------------------------------------------------------------")
                print("These are the stats for %s type of files"%file_type)
                cols = group.thetype.unique()
                print(self.file_stats[cols].sum().to_markdown())

    def download_files(self, dir_name, overwrite=False, file_types=[]):

        self.info['tradition_dunya'].set_collections([self.info['tradition_id']])
        rec_infos = self.info['tradition_dunya'].get_recordings(recording_detail=True)

        if len(file_types)==0:
            file_types = self.file_info.file_type.unique()
        for rec_info in rec_infos[:5]:
            # fetching names
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
                        download_status = download_file(rec_info['mbid'], row['thetype'], row['subtype'], file_path)
                    except Exception as e:
                        print("File downloading failed for tradition: %s, mbid: %s, thetype: %s, subtype: %s" % (
                        self.info['tradition_name'], rec_info['mbid'], row['thetype'], row['subtype']))

    def explain_filetypes(self):

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

    def compute_metadata_stats(self):
        """
        Fetches number of different "unique" entities link to all the recordings of a collection
        This function also returns total length of the recordings in a cosllection
        """

        self.info['tradition_dunya'].set_collections([self.info['tradition_id']])
        rec_infos = self.info['tradition_dunya'].get_recordings(recording_detail=True)

        entities = self.cmap['entities']
        stats = dict(zip(entities, [[] for e in entities]))
        for rec_info in rec_infos:
            for e in entities:
                if e in rec_info:
                    if e == 'artists':
                        temp = [x['artist'] for x in rec_info[e]]
                        stats[e].extend([x[self.cmap['id_mapping'][e]] for x in temp])
                    elif e == 'length':
                        stats[e].append(rec_info[e])
                    else:
                        stats[e].extend([x[self.cmap['id_mapping'][e]] for x in rec_info[e]])
        self.metadata_stats = stats

    def get_metadata_stats(self):
        return self.metadata_stats

    def print_metadata_stats(self):
        print('----------------------------------------')
        print("Stats for %s tradition:" % self.info['tradition_name'])
        for ent, nums in self.metadata_stats.items():
            if ent == 'num_mbids':
                print("Total number of recordings %d" % nums)
            elif ent != 'length':
                print("Total number of unique %s are:%d" % (ent, len(set(nums))))
            else:
                print("Total length of the recordings: %0.2f hrs" % (np.sum(nums) / 3600000.))


class Saraga:

    def __init__(self, api_token=None, tradition_slug=None, mode=None):

        if not api_token:
            raise Exception("API token not provided")
        else:
            dn.set_token(api_token)

        if tradition_slug is None:
            self.info = meta.info
        else:
            if tradition_slug not in meta.info.keys():
                raise Exception("Wrong tradition slug specified")
            else:
                self.info = {tradition_slug:meta.info[tradition_slug]}
        self.datasets = {}
        for tradition_slug, collection in self.info.items():
            self.datasets[tradition_slug] = Dataset(tradition_slug)



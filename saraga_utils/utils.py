from compmusic import dunya as dn
import json
import numpy as np
import os
import pandas as pd
from compmusic.file import file_metadata
import hashlib

def download_file(mbid, thetype, subtype, file_path):
    """
    Utility function (wrapper) to download a file

    :param mbid: str
        Musicbrainz id of the recording
    :param thetype: str
        Dunya type of the file
    :param subtype: str
        Dunya subtype of the file
    :param file_path: str
        Path where the file is to be dumped
    :return:
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


def get_files_in_dir(dir_name):
    """
    Get filenames within a directory (recursively)
    :param dir_name:
    :return:
    """
    names = []
    for (path, dirs, files) in os.walk(dir_name):
        for ii, f in enumerate(files):
            names.append(f)
    return names

def count_file_types(root_dir):
    """
    For specific way in which we dump files in the dataset, this function counts the files per filetype
    :param root_dir:
    :return:
    """
    filenames = get_files_in_dir(root_dir)
    stats = []
    for filename in filenames:
        parts = filename.split('.')
        length = len(parts)
        thetype = ">>".join(parts[-length + 1:])
        stats.append(dict(thetype=thetype,filename=filename))

    stats_df = pd.DataFrame(stats)
    print(stats_df.thetype.value_counts())
    return stats_df

def get_paths(root_dir, seed_ext ='.mp3.mp3'):
    """
    This function fetches file paths for recordings and stores them as a csv with mbid and corresponding paths
    :param root_dir:
    :param seed_ext:
    :return:
    """
    out = []
    for (path, dirs, files) in os.walk(root_dir):
        for ii, f in enumerate(files):
            if f.lower().endswith(seed_ext):
                path = os.path.join(path, f)
                out.append(dict(filepath=path.replace(root_dir, '').replace(seed_ext, ''),
                                mbid=file_metadata(path)['meta']['recordingid']))
    out_df = pd.DataFrame(out)
    out_df.to_csv(os.path.join(root_dir, 'file_paths.csv'))

def generate_md5_for_audio(root_dir, seed_ext='.mp3.mp3'):
    """
    This function creates md5 hashes of files which ends in extention seed_ext.
    This is needed to store md5 hashes for large files (like audios) to maintain records.
    The generated hash is stored in the same folder structure

    NOTE: there is a hardcoding currenty for audio md5. If this function is needed elsewhere, the harcoding can be
    removed
    :param root_dir: str
        Directory where the files are to be searched
    :param seed_ext: str
        Extension of the file for which md5 hash is to be generated
    :return:
    """
    for (path, dirs, files) in os.walk(root_dir):
        for ii, f in enumerate(files):
            if f.lower().endswith(seed_ext):
                path = os.path.join(path, f)
                content = open(path, 'rb').read()
                md5 = hashlib.md5(content).hexdigest()
                fid = open(path[:-4] + '.md5', 'w')
                fid.write(md5)
                fid.close()

def add_to_git(root_dir):
    """
    Adds files with allowed extention to git
    :param root_dir:
    :return:
    """
    allowed_exts = ['ctonic.txt',
                    'sama-manual.txt',
                    'bpm-manual.txt',
                    'tempo-manual.txt',
                    'sections-manual-p.txt',
                    'mphrases-manual.txt',
                    'mp3.md5',
                    'json']
    filenames = []
    for (path, dirs, files) in os.walk(root_dir):
        for ii, f in enumerate(files):
            filenames.append(os.path.join(path, f))

    for filename in filenames:
        ext = ".".join(os.path.basename(filename).split('.')[1:])
        if ext in allowed_exts:
            os.system("git add %s"%(filename))
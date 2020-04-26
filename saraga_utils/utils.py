from compmusic import dunya as dn
import json
import numpy as np

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

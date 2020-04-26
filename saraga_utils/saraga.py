from compmusic import dunya as dn
from saraga_utils import meta
from saraga_utils.dataset import Dataset

class Saraga:
    """
    Main class through which one can do bulk operations like
    1) Fetching statistics around annotations and metadata
    2) Download files (annotations, audio etc)
    3) Get description of types of files in the dataset
    """
    def __init__(self, root_dir=None, api_token=None, tradition_slug=None, mode=None):
        """
        :paran root_dir: str
            root directory where files will be dumped (if asked for)
        :param api_token: str
            Get api token after registering in Dunya (https://dunya.compmusic.upf.edu/)
        :param tradition_slug: str
            Slug of the tradition to be set for processing (dunya-carnatic-cc or dunya-hindustani-cc).
            Default is None which essentially includes both the datasets for processing
        :param mode: str
            If its set to 'test' system doesn't iterate on all the files in the dataset but first N(=5)
            This is needed for testing the system since downloading and fetching takes a lot of time.
        """

        # setting api token first
        if not api_token:
            raise Exception("API token not provided")
        else:
            dn.set_token(api_token)

        # if no slug is provided, we process both the datasets (hindustani and carnatic)
        if tradition_slug is None:
            self.info = meta.info
        else:
            if tradition_slug not in meta.info.keys():
                raise Exception("Wrong tradition slug specified")
            else:
                self.info = {tradition_slug:meta.info[tradition_slug]}

        # creating object for each dataset that can be used for processing on those datasets
        self.datasets = {}
        for tradition_slug, collection in self.info.items():
            self.datasets[tradition_slug] = Dataset(tradition_slug)


    # fetching statistics for metadata

    # fetching statistics for files

    # downloading all metadata

    # downloading all files





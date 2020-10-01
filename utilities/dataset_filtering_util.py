from utilities.dataset import Dataset
from utilities.utils import series_to_list, get_multi_select_widget
from utilities import meta
import pandas as pd
import os


class DatasetFilteringUtil():

    def __init__(self, api_token, tradition_slug, use_cached):
        self.api_token = api_token
        self.tradition_slug = tradition_slug
        self.use_cached = use_cached

        # Initiating dataset object to do all the needed IO operations
        self.obj_dataset = Dataset(tradition_slug=tradition_slug, api_token=self.api_token)

        # what are the selectable concepts
        self.selectable_concepts = {'album_artists': None, 'raga': None, 'tala': None, 'form':None}

        # selectable file slugs (this will be done depending on what we fetch, depending on the tradition)
        self.selectable_file_slugs = None

        # fetching information to get started
        self.dataset_local_path = os.path.join(os.path.dirname('__file__'), '%s.pkl'%self.tradition_slug)
        if os.path.isfile(self.dataset_local_path) and use_cached:
            self.dataset_info = pd.read_pickle(self.dataset_local_path)
        else:
            self.dataset_info = self.obj_dataset.consolidate_dataset_info()
            self.dataset_info.to_pickle(self.dataset_local_path)

    def prepare_filters(self):

        # lets find out selectable file slugs
        self.selectable_file_slugs = list(set(self.dataset_info.columns).intersection(meta.content_info[self.tradition_slug].slug))

        # Initialising selectors for concepts
        for concept, _ in self.selectable_concepts.items():
            col_name = meta.concept_mapp[self.tradition_slug]['entity_mapp'][concept]
            list_items = series_to_list(self.dataset_info[col_name])
            selector_obj = get_multi_select_widget(list_items, concept.replace('_', ' ').title())
            self.selectable_concepts[concept] = selector_obj

        # initialising selectors for file types
        list_items = self.selectable_file_slugs
        self.file_selector_obj = get_multi_select_widget(list_items, "File slugs")


    def perform_filtering(self):
        self.dataset_info['is_selected'] = True

        # Performing filtering w.r.t the concepts
        for concept, obj in self.selectable_concepts.items():
            col_name = meta.concept_mapp[self.tradition_slug]['entity_mapp'][concept]
            col_val = obj.value
            if len(col_val) > 0:
                dec_col = self.dataset_info.apply(lambda x: len((set(x[col_name])).intersection(col_val)) > 0, axis=1)
                self.dataset_info['is_selected'] = self.dataset_info['is_selected'] & dec_col

        # performing filtering wrt the file slugs
        if len(self.file_selector_obj.value) >0: # only when at least one value is selected
            for col in self.file_selector_obj.value:
                dec_col = self.dataset_info.apply(lambda x: x[col]==1, axis=1)
                self.dataset_info['is_selected'] = self.dataset_info['is_selected'] & dec_col

        return self.dataset_info[self.dataset_info.is_selected]









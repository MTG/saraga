
## Accessing the Saraga collections
Saraga collections can be found in [this Zenodo entry](https://zenodo.org/records/4301737). The data can be directly downloaded from this link. We have created a `mirdata` dataloader for [Saraga Carnatic](https://mirdata.readthedocs.io/en/stable/source/mirdata.html#module-mirdata.datasets.saraga_carnatic) and another one for [Saraga Hindustani](https://mirdata.readthedocs.io/en/stable/source/mirdata.html#module-mirdata.datasets.saraga_hindustani). These dataloader will allow you to directly download, validate, and load the audio, annotations, and metadata in both Saraga collections. Please find more details in the documentation.

These dataloaders can also be summoned through `compiam`, a Python library to assist the computational analysis of Carnatic and Hindustani music. Please find documentation for these functionalities in our [ISMIR 2022 Tutorial webbook](https://mtg.github.io/IAM-tutorial-ismir22/corpora_and_datasets/datasets.html).

In this Tutorial, you can also find functionalities to [access the entire Dunya corpora](https://mtg.github.io/IAM-tutorial-ismir22/corpora_and_datasets/corpora.html), using the compmusic API.

## Other resources (discontinued)
Although discontinued and not mantained anymore, the Saraga collections were initially [accessed and browsed ](https://github.com/MTG/saraga/blob/master/examples/usage_demo.ipynb) using the resources in this Section. For reference, we are linking the series of notebooks that can be used for that, but potential issues may arise, and is not the recommended method to access the datasets.

* **[dataset_statistics.ipynb](https://github.com/MTG/saraga/blob/master/scripts/dataset_statistics.ipynb)** : to get the statistics of metadata fields and files in the collections
* **[concept_statistics.ipynb](https://github.com/MTG/saraga/blob/master/scripts/concept_statistics.ipynb)** : to get the number of recordings (MBIDs) corresponding to each metadata field
* **[download_by_filtering.ipynb](https://github.com/MTG/saraga/blob/master/scripts/download_by_filtering.ipynb)** : to filter the dataset using metadata fields and associated file types, and subsequently download the filtered dataset
* **[download_in_bulk.ipynb](https://github.com/MTG/saraga/blob/master/scripts/download_in_bulk.ipynb)** : to download the complete dataset at once

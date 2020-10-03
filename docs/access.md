## API access to the data collections
A set of utility scripts to access the data in the collections is in [saraga_utils](https://github.com/MTG/saraga/tree/master/saraga_utils) folder. The scripts use the PyCompMusic API to access the data. Access to the data requires the users to register on [Dunya](https://dunya.compmusic.upf.edu) and obtain an API token that needs to be used for authentication with PyCompMusic API to download audio, metadata and annotations. All available data/metadata/annotations in the collections can be accessed through the API. 

## Examples
Several python notebooks that explain the API and show examples of how you can use the utility code provided in this repository is available [Python notebook](https://github.com/MTG/saraga/blob/master/examples/usage_demo.ipynb)

* **[dataset_statistics.ipynb](https://github.com/MTG/saraga/blob/master/scripts/dataset_statistics.ipynb)** : to get the statistics of metadata fields and files in the collections
* **[concept_statistics.ipynb](https://github.com/MTG/saraga/blob/master/scripts/concept_statistics.ipynb)** : to get the number of recordings (MBIDs) corresponding to each metadata field
* **[download_by_filtering.ipynb](https://github.com/MTG/saraga/blob/master/scripts/download_by_filtering.ipynb)** : to filter the dataset using metadata fields and associated file types, and subsequently download the filtered dataset
* **[download_in_bulk.ipynb](https://github.com/MTG/saraga/blob/master/scripts/download_in_bulk.ipynb)** : to download the complete dataset at once

## Zip archive of audio and pitch files 
In case you don't wish to use the API to access audio (including multitracks in Carnatic collection) and pitch files (they are not available through this repository), we have a zip archive of those files. Please [fill this form](https://forms.gle/Zs853Jwg6NCSCBFL8) or [contact us](https://github.com/MTG/saraga/blob/master/docs/index.md#contact) for a link to the archive. 

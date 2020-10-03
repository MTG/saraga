# Saraga
This is the companion repository of the Saraga collections. The repository contains a dump of the data collections and has further detailed documentation on the format and organization of the data, access to the data, Python notebooks and code snippets illustrating different ways to access the data, and ways for community to contribute to the collections. The repository also hosts the [companion website for the Saraga collections](https://mtg.github.io/saraga/). 

# Steps to setup
### Clone the repository

### Create virtual environment
```virtualenv -p python3 env```

### Activate environment
```source env/bin/activate```

### Install dependencies
```pip install -r requirements.txt```

### Get an API token

You can register and get an API token from : https://dunya.compmusic.upf.edu/


That's it, scripts are ready to use.

# Scripts and Notebooks
The following notebooks are available to interact with the collections. The primary purpose of the notebooks is to provide examples to download different data and metadata available in the collections. The notebooks also provide some basic illustrative examples to interact with the data collections for analysis.  

* **[dataset_statistics.ipynb](scripts/dataset_statistics.ipynb)** : to get dataset counts of metadata fields and files in the dataset
* **[concept_statistics.ipynb](scripts/concept_statistics.ipynb)** : to get dataset counts of mbids (recordings) linked with each metadata field
* **[download_by_filtering.ipynb](scripts/download_by_filtering.ipynb)** : to filter the dataset using metadata fields and associated file types, and subsequently download the filtered dataset
* **[download_in_bulk.ipynb](scripts/download_in_bulk.ipynb)** : to download the entire dataset at once.

# Glossary

* MBID : MusicBrainz identifier for the recording
* slug : An identifier for a concept (file or metadata)

### Tradition slug
It is a machine readable identifier to specify a tradition name that you are analysing.

These are the possible values

| Tradition  | slug |
|---|---|
|Hindustani   |  dunya-hindustani-cc |
|Carnatic   |  dunya-carnatic-cc |

### File slug
It is an identifier for the type of file that we want to be processing

These are the possible values

| Name  | slug | type of file |
|---|---|---|
audio recording | mp3 | audio |
pitch | pitch | annotation |
tonic | ctonic | annotation |
sama | sama-manual | annotation |
bpm | bpm-manual | annotation |
tempo | tempo-manual | annotation |
sections | sections-manual-p | annotation |
melodic phrases | mphrases-manual | annotation |
vocal recording (multitrack) | multitrack-vocal | audio |
vocal second channel recording (multitrack) | multitrack-vocal-s | audio |
violin recording (multitrack) | multitrack-violin | audio |
ghatam  recording (multitrack) | multitrack-ghatam | audio |
mridangam_left  recording (multitrack) | multitrack-mridangam-left | audio |
mridangam_right  recording (multitrack) | multitrack-mridangam-right | audio |

### Metadata slug

It is an identifier for the metadata (e.g. release, raga, tala etc)

list the slugs for different metadata types in Hindustani and Carnatic tradition:

| Metadata | Hindustani (slug) | Carnatic (slug) |
| --- | --- | --- |
| Rāga | raags | raaga |
| Tāla | taals | taala |
| Form | forms | form |
| Laya | layas | laya |
| Work | works | work |
| Release | release | concert |
| Album artist | album_artists | album_artists |

# Welcome to Saraga collections

**Website under construction**

*(Last updated: 03 Oct 2020)*

This is the companion website to the Saraga collections. Saraga collections are currently the largest annotated open data collections available for computational research on Indian Art Music. They comprise audio, editorial metadata, manual and automatically extracted annotations for different aspects of melody, rhythm and structure. The Saraga collections were conceived and built as a part of the CompMusic project and is currently maintained by the [Music Technology Group](https://www.upf.edu/web/mtg/), Universitat Pompeu Fabra, Barcelona. 

This page provides up-to-date statistics of the collections, detailed documentation on the organization of the collections, available annotations and their formats, example scripts to access the collections through the PyCompMusic API. 

## Collection statistics

As of 03 Oct 2020, here are the coverage and completeness statistics of the Saraga collections. 

### Coverage statistics 
Coverage statistics describe the different unique entities of different concepts in the data collections. 

Content | Hindustani | Carnatic
------------ | ------------- | ----------------
Total releases | 36 | 26
Total recordings | 108 | 249
Total recordings in multi-track | - | 168 | 
Total artists (lead+accompanying) | 36 | 64
Compositions | 113 | 202
Unique rāga | 61 | 96
Unique tāla | 9 | 10
**Total duration** | **43.6 hours** | **52.7 hours**

### Completeness Statistics
Completeness statistics describe how complete the available data and metadata are, by reporting the total number of recordings in the collections that contain the associated metadata. Detailed information is provided along with a [description of file formats](https://mtg.github.io/saraga/organization.html#file-formats), but a summary is provided below. The last two columns show the number of recordings in the Hindustani music collection (HM) and Carnatic Music collection (CM) that contain the corresponding data/metadata. `-NA` indicates "Not Available". 

Data/Metadata | Description | HM | CM
------ | ------ | ----- | -------
Stereo mix | Audio file (mp3) |108|249
Raga | raga/s of the music piece | TBD | TBD| 
Taala | taala/s of the music recording | TBD | TBD 
Laya | laya/s of the music recording | TBD | `-NA-`
Form | Music form of the recording | TBD | TBD
Tonic | The tonic of the recording |108|249
Pitch | F0 extracted from mixed stereo track |108|249
Vocal Pitch | F0 extracted from the vocal track | `-NA` |168
Lead vocal track | For multitrack | `-NA-` |168
Violin track | For multitrack | `-NA` | 168
Secondary vocal track | For multitrack |`-NA-` |24
Mridangam bass drum track | For multitrack |`-NA-` |168
Mridangam treble drum track | For multitrack |`-NA-` |168
Ghatam track | For multitrack |`-NA-` | 46
Melodic phrases| Manually annotated melodic phrases |53|117
Sama | Time-aligned sama annotations |75|141
Tempo | Tempo related annotations |75|133
Section | Section boundaries and section names|75|119

## Data Organization
The data in Saraga collections are organized by individual music cultures - Carnatic and Hindustani, and further organized into releases and recordings. For each recording, we have associated audio, editorial metadata and annotations identified by the MusicBrainz ID of the recording. Further details are here: [Organization and file formats](organization.md)

## Access
The data in the collections can be accessed through the [PyCompMusic](https://github.com/MTG/pycompmusic) API built to access Dunya collections. In addition, the Saraga repository provides a dump of all editorial metadata and some annotations. Larger files such as audio and pitch annotations are not amenable for storage in a git repository and hence a zip archive of the data is available. For tracking and versioning, the Saraga repository stores the md5 checksum of the file for comparsion with the files in the zip archive. Further details are here: [Access to data and example scripts](access.md)

## Applications
We illustrate some of the applications that use Saraga collections for music education or exploration:

1. **The [Musical Bridges](https://www.upf.edu/web/musicalbridges) project** aims at bringing together different cultures through music understanding. The tools in Musical Bridges offer interactive visualizations synchronized to recordings from the Saraga collections and facilitate the comprehension of some of the key elements of Carnatic and Hindustani music traditions. 

2. **Saraga App**: We have built an android mobile app that is a music exploration tool and provides an enhanced listening experience with a subset of Saraga Hindustani and Carnatic collections. The app is free - we invite you to [download the app from Play Store](https://play.google.com/store/apps/details?id=com.mtg.saraga) and try it out. 

## License
The audio, metadata, annotations in the collections and the code in this repository are released under different open licenses. Please see [LICENSE](https://github.com/MTG/saraga/blob/master/LICENSE.md) file for more details.

## Contributors
Several people and institutions have contributed to the Saraga data collections. Please see the list of [contributors](https://github.com/MTG/saraga/blob/master/contributors.md) for a complete list of contributors.  

## Contribute
Saraga collections are envisioned to be living and growing collections of data. Community contributions to the collections in terms of more audio data, editorial metadata, manual annotations and automatic extractors is welcome. Research problems and innovative applications using Saraga data collections can be showcased here. Please contact us if you wish to contribute to the data collections. 

## Contact
If you have any questions, queries or comments about the data collections, or if you wish to contribute to the collections, please contact us: 

Ajay Srinivasamurthy (ajays.murthy@upf.edu)

Sankalp Gulati (sankalp.gulati@upf.edu)

Rafael Caro (rafael.caro@upf.edu)

Prof. Xavier Serra (xavier.serra@upf.edu)

We would be glad to know more about how you have used the Saraga data collections in your work!

## Organization

The collections are organized into Carnatic and Hindustani sub-collections and present in the [dataset](dataset) folder of the repository. Within each folder, the collections are organized into releases and then into recordings, following the `<music_tradition>/<release>/<recording_name>` format, where the release and recording names are provided in a human readable names for easy browsing. The `release` is of the form "release_name by lead_artist" where release_name and lead_artist correspond to the names from editorial metadata for the release in MusicBrainz. The `recording_name` also corresponds to the name of the recording in MusicBrainz. 

Within each `recording_name` folder, all the editorial metadata, source and derived files of a recording are stored. The source and derived files for each recording are stored within the folder `<music_tradition>/<release>/<recording_name>/` as `<recording_name>.<slug>`. The `slug` depends on the type of the source or derived files corresponding to the recording. For each recording, the mapping from the MusicBrainz ID (MBID) to the file paths is provided in the following mapping files: 

Carnatic: [dataset/carnatic/file_paths.csv](dataset/carnatic/file_paths.csv)

Hindustani: [dataset/hindustani/file_paths.csv](dataset/hindustani/file_paths.csv)

### File formats
The format of each source and derived files along with the slug is explained in the following section:  

File type | slug | Format | Source/Derived | Description | Hindustani | Carnatic
------ | ----- | ------ | ----- | ------ | ----- | -------
metadata | `.json` | JSON | Metadata | A json containing the editorial metadata about the recording | 108 | 249
mp3 | `.mp3.md5` | [Audio file format](#audio-file-format) | Source | Audio file of a stereo mix of the recording | 108 | 249 
multitrack-vocal | `.multitrack-vocal.md5` | [Audio file format](#audio-file-format) | Source | Audio file corresponding to the lead vocal track (if available) | - | 168
multitrack-vocal-s | `.multitrack-vocal-s.md5` | [Audio file format](#audio-file-format) | Source | Audio file corresponding to the secondary vocal track (if available) | - | 24
multitrack-violin | `.multitrack-violin.md5` | [Audio file format](#audio-file-format) | Source | Audio file corresponding to the violin track (if available) | - | 168
multitrack-mridangam-left | `.multitrack-mridangam-left.md5` | [Audio file format](#audio-file-format) | Source | Audio file corresponding to the mridangam bass drum track (if available) | - | 168
multitrack-mridangam-right | `.multitrack-mridangam-right.md5` | [Audio file format](#audio-file-format) | Source | Audio file corresponding to the mridangam treble drum track (if available) | - | 168
multitrack-ghatam | `.multitrack-ghatam.md5` | [Audio file format](#audio-file-format) | Source | Audio file corresponding to the ghatam track (if available) | - | 46
tonic | `.ctonic.txt` | [Tonic file format](#tonic-file-format) | Derived | A file with the tonic of the recording in Hz | 108 | 249 
pitch | `.pitch.md5` | [Pitch file format](#pitch-file-format) | Derived | A file with predominant melody (F0) extracted from mixed stereo track using Melodia algorithm in Essentia | 108 | 249
pitch-vocal | `.pitch-vocal.md5` | [Pitch file format](#pitch-file-format) | Derived | A file with predominant melody (F0) extracted from the vocal track using Melodia algorithm in Essentia | - | 168
mphrases-manual | `.mphrases-manual.txt` | [Melodic phrases file format](#melodic-phrases-file-format) | Source | A text file with manually annotated melodic phrases | 53 | 117
sama-manual | `.sama-manual.txt` | [Sama file format](#sama-file-format) | Source | A text file with timestamps of sama in the audio recording | 75 | 141
tempo-manual | `.tempo-manual.txt` | [Tempo file format](#tempo-file-format) | Source | 
This file shows different tempo related annotations derived from sama timestamps | 75 | 133
sections-manual | `.sections-manual-p.txt` | [Sections file format](#sections-file-format) | Source | A text file containing the section boundaries and section names | 75 | 119 

#### Audio file format

audio mp3 md5 hash

#### Pitch file format

#### Tonic file format

#### Melodic phrases file format

#### Sama file format

#### Tempo file format
For each section, this file shows different tempo related annotations derived from sama timestamps. A value of -1 indicates a section without rhythmic content (such as an melodic improvisation) 

#### Sections file format

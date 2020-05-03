## Organization

The collections are organized into Carnatic and Hindustani sub-collections and present in the [dataset](dataset) folder of the repository. Within each folder, the collections are organized into releases and then into recordings, following the `<music_tradition>/<release>/<recording_name>` format, where the release and recording names are provided in a human readable names for easy browsing. The `release` is of the form "release_name by lead_artist" where release_name and lead_artist correspond to the names from editorial metadata for the release in MusicBrainz. The `recording_name` also corresponds to the name of the recording in MusicBrainz. 

Within each `recording_name` folder, all the editorial metadata, source and derived files of a recording are stored. The source and derived files for each recording are stored within the folder `<music_tradition>/<release>/<recording_name>/` as `<recording_name>.<slug>`. The `slug` depends on the type of the source or derived files corresponding to the recording. For each recording, the mapping from the MusicBrainz ID (MBID) to the file paths is provided in the following mapping files: 

Carnatic: [dataset/carnatic/file_paths.csv](dataset/carnatic/file_paths.csv)

Hindustani: [dataset/hindustani/file_paths.csv](dataset/hindustani/file_paths.csv)

### File formats
The format of each source and derived files along with the slug is explained in the following table. The last two columns show the number of recordings in the Hindustani music collection (HM) and Carnatic Music collection (CM) that contain the corresponding source/derived files. 

File type | slug | Format | Source/Derived | Description | HM | CM
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
tempo-manual | `.tempo-manual.txt` | [Tempo file format](#tempo-file-format) | Source | This file shows different tempo related annotations derived from sama timestamps | 75 | 133
sections-manual | `.sections-manual-p.txt` | [Sections file format](#sections-file-format) | Source | A text file containing the section boundaries and section names | 75 | 119 

#### Audio file format
All audio files (both stereo mixes and multitracks) in the collection are stored as 128 kbps mp3 audio sampled at 44.1 kHz. However, since large audio files are not suitable for storing in a git repository, the audio files can be accessed through the API or through the tarball of audio recordings. However, to enable versioning of the audio files, we store the md5 checksum of the audio file in the repository (as `.md5` files) so that it can be used to verify and reconcile with the audio files. 

#### Tonic file format
Tonic file is a text file with a single float value corresponding to the tonic of the recording expressed in Hz

#### Pitch file format
The pitch files in the collection are derived from the pitch extractor in PyCompMusic tools, which internally uses the Melodia algorithm to extract predominant melody. The pitch is typically computed over short audio frames with a hop size of 4.4 ms. The file is stored as a text file with the format

`timestamp pitch_value`

in each line of the file, e.g.

```
11.2400000	154.6684418
11.2444444	156.4656219
11.2488889	158.2836609
```

The `timestamp` are expressed in seconds and `pitch_value` in Hz. A zero pitch value indicates unvoiced regions. 

Since pitch files are large text files that are not suitable for storing in a git repository, the pitch files can be accessed through the API or through the tarball of audio recordings. However, to enable versioning of the pitch files, we store the md5 checksum of the pitch file in the repository (as `.md5` files) so that it can be used to verify and reconcile with the pitch files. 

#### Melodic phrases file format
The manually annotated melodic phrases are stored as a text file. Each line of the file corresponds to one instance of an annotated phrase and stored in the format

`start_time flag  duration  notes`

e.g.

```
19.159183673	1	2.253061224	pdnspmg
28.816326530	2	2.089795918	pngpm
```
 
The start_time indicates the start time of the phrase annotation in the audio file expressed in seconds. The `flag` takes two values, with 1 indicating a representative phrase of a recording, and 2 representative phrase of a rāga, which also implies a representative phrase of the recording. `duration` indicates the duration of the phrase expressed in seconds. `notes` denotes the sequence of notes played/sung in the phrase. 

#### Sama file format

#### Tempo file format
For each section, this file shows different tempo related annotations derived from sama timestamps. A value of -1 indicates a section without rhythmic content (such as an melodic improvisation) 

#### Sections file format

## Organization

The collections are organized into Carnatic and Hindustani sub-collections and present in the [dataset](https://github.com/MTG/saraga/tree/master/dataset) folder of the repository. Within each folder, the collections are organized into releases and then into recordings, following the `<music_tradition>/<release>/<recording_name>` format, where the release and recording names are provided in a human readable names for easy browsing. The `release` is of the form "release_name by lead_artist" where release_name and lead_artist correspond to the names from editorial metadata for the release in MusicBrainz. The `recording_name` also corresponds to the name of the recording in MusicBrainz. 

Within each `recording_name` folder, all the editorial metadata, source and derived files of a recording are stored. The source and derived files for each recording are stored within the folder `<music_tradition>/<release>/<recording_name>/` as `<recording_name>.<slug>`. The `slug` depends on the type of the source or derived files corresponding to the recording. For each recording, the mapping from the MusicBrainz ID (MBID) to the file paths is provided in the following mapping files: 
* Carnatic: [dataset/carnatic/file_paths.csv](https://github.com/MTG/saraga/tree/master/dataset/carnatic/file_paths.csv)
* Hindustani: [dataset/hindustani/file_paths.csv](https://github.com/MTG/saraga/tree/master/dataset/hindustani/file_paths.csv)

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

--- 

#### Audio file format
All audio files (both stereo mixes and multitracks) in the collection are stored as 128 kbps mp3 audio sampled at 44.1 kHz. However, since large audio files are not suitable for storing in a git repository, the audio files can be accessed through the API or through the tarball of audio recordings. However, to enable versioning of the audio files, we store the md5 checksum of the audio file in the repository (as `.md5` files) so that it can be used to verify and reconcile with the audio files. 

---

#### Tonic file format
Tonic file is a text file with a single float value corresponding to the tonic of the recording expressed in Hz.

--- 

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

---

#### Melodic phrases file format
The manually annotated melodic phrases are stored as a text file. Each line of the file corresponds to one instance of an annotated phrase and stored in the format

`start_time flag duration notes`

e.g.

```
19.159183673	1	2.253061224	pdnspmg
28.816326530	2	2.089795918	pngpm
```
 
The start_time indicates the start time of the phrase annotation in the audio file expressed in seconds. The `flag` takes two values, with 1 indicating a representative phrase of a recording, and 2 representative phrase of a rāga, which also implies a representative phrase of the recording. `duration` indicates the duration of the phrase expressed in seconds. `notes` denotes the sequence of notes played/sung in the phrase. 

---

#### Sama file format
The sama file is a text file that contains a non-decreasing series of time instants corresponding to successive sama of the tāla cycles in the music piece, aligned with the audio recording. Each line of the file is one timestamp of a sama (expressed in seconds), e.g.

```
18.426
23.187
27.944
32.683
37.390
42.055
```

---

#### Sections file format
The section file stores the different structural sections in a recording. The sections in Carnatic music are lyrical, while Hindustani music sections are based on different bandishes in the same rāg with different tāl and lay. The file formats are different for Carnatic and Hindustani music collections. 

For Hindustani music recordings, the section file has one section annotation per line with the following format: 

`start_time,section_number,duration,section_name`

e.g.

```
0.0,1,29.694,Ālāp
29.694,2,198.953,Khyāl (vilambit ēktāl)
228.647,3,104.179122449,Tarānā (dr̥t tīntāl)
```

`start_time` denotes the start of the section (in seconds) in the audio recording. `duration` indicates the duration of the section (in seconds) and `section_name` is the name of the section. `section_number` indicates the serial number of the section in the recording. The section name also includes the name of the tāl if available. 

For Carnatic music recordings, the section file has one section annotation per line with the following format: 

`start_time ignore_flag duration section_name`

e.g.

```
50.808163265	1	75.069387755	Anupallavi
125.87755102	1	137.697959184	Caraṇam
```

`start_time` denotes the start of the section (in seconds) in the audio recording. `duration` indicates the duration of the section (in seconds) and `section_name` is the name of the section. `ignore_flag` does not capture any useful information and can be ignored. 

---

#### Tempo file format
The tempo file stores different tempo related annotations derived from sama timestamps for each section of the audio recording. The file format is different for Carnatic and Hindustani music collections to capture different information. 

For Hindustani music recordings, since the sections are related to rhythmic changes (laya), the tempo file stores the tempo information for each timestamped section of the recording. Each line of the tempo file is stored as, 

`tempo, matra_interval, sama_interval, matras_per_cycle, start_time, duration`

e.g. if there are three sections in an audio recording, the tempo file might look like: 

```
-1, -1, -1, -1, 0.000, 29.000
26, 2.323, 27.879, 12, 29.694, 224.114
243, 0.247, 3.955, 16, 228.647, 317.696
```

`tempo` stores the median tempo for the section in mātrās per minute (MPM), `matra_interval` is the tempo expressed as the duration of the mātra (essentially dividing 60 by tempo, expressed in seconds), `sama_interval` is the median duration of one tāl cycle in the section, `matras_per_cycle` is an indicator of the structure of the tāl, showing the number of mātrā in a cycle of the tāl of the recording. The last two columns, `start_time` and `duration` are expressed in seconds and correspond to the start time and duration of the section in the audio recording. 

For Carnatic music recordings, since the sections are lyrical, they do not typically associated with a change of tempo. Hence the tempo files are stored with tempo information on a single line corresponding to the entire audio file treated as one section, with the following format: 

`tempo_apm, tempo_bpm, sama_interval, beats_per_cycle, subdivisions`

e.g. 

```
340, 170, 2.471, 14, 2
```

`tempo_apm` and `tempo_bpm` stores the median tempo of the recording in aksharas per minute (APM) and beats per minute (BPM), respectively. `sama_interval` is the median duration (in seconds) of one tāla cycle in the recording. The last two columns capture the structure of the tāla, with `beats_per_cycle` storing the number of beats in one cycle of the tāla of the recording, and `subdivision` storing the number of aksharas per beat of the tāla of the recording (called the naḍe in Carnatic music terminology). 

In both Carnatic and Hindustani recordings, a value of -1 for tempo related values indicate a section/recording without rhythmic content (such as an melodic improvisation). 

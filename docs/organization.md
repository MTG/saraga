## Organization

The collections are organized into Carnatic and Hindustani sub-collections and present in the [dataset](dataset) folder of the repository. Within each folder, the collections are organized into releases and then into recordings, following the `<music_tradition>/<release>/<recording_name>` format, where the release and recording names are provided in a human readable names for easy browsing. The `release` is of the form "release_name by lead_artist" where release_name and lead_artist correspond to the names from editorial metadata for the release in MusicBrainz. The `recording_name` also corresponds to the name of the recording in MusicBrainz. Within each `recording_name` folder, all the source and derived files of a recording are stored. The source and derived files for each recording are stored within the folder `<music_tradition>/<release>/<recording_name>/` as `<recording_name>.<slug>`. The `slug` depends on the type of the source or derived files corresponding to the recording. 

For each recording, the mapping from the MusicBrainz ID (MBID) to the file paths is provided in the following mapping files: 

Carnatic: [dataset/carnatic/file_paths.csv](dataset/carnatic/file_paths.csv)

Hindustani: [dataset/hindustani/file_paths.csv](dataset/hindustani/file_paths.csv)

### File formats
The format of each source and derived files along with the slug is explained in the following section:  

File type | slug | Format | Description | Hindustani | Carnatic
------ | ----- | ------ | ----- | ------ | ----- 
mp3 | `.mp3.md5` | audio mp3 | Audio file of the stereo mix | 108 | 249 | 
[Pitch format](#pitch-file-format)


`<recording_name>.`

#### Pitch file format

#### Tonic file format

#### Melodic phrases file format

#### Sama file format

#### Tempo file format

#### Sections file format

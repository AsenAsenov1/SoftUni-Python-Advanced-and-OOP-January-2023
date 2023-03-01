### You are tasked to create three classes: a Song class, an Album class, and a Band class.
 
### The Song class should receive a name (string), a length (float), and a single (bool) upon initialization. It has one method:
### -	get_info()
<br>    o	Returns the information of the song in this format: "{song_name} - {song_length}"<br>

The Album class should receive a name (string) upon initialization and might receive one or more songs. 
It also has instance attributes: published (False by default) and songs (an empty list). It has four methods:
### -	add_song(song: Song)
  <br>o	Adds the song to the album and returns "Song {song_name} has been added to the album {name}."<br>
  <br>o	If the song is single, returns "Cannot add {song_name}. It's a single"<br>
  <br>o	If the album is published, returns "Cannot add songs. Album is published."<br>
  <br>o	If the song is already added, return "Song is already in the album."<br>
### -	remove_song(song_name: str)
 <br>o	Removes the song with the given name and returns "Removed song {song_name} from album {album_name}."<br>
<br>o	If the song is not in the album, returns "Song is not in the album."<br>
<br>o	If the album is published, returns "Cannot remove songs. Album is published."<br>

### -	publish()
<br>o	Publishes the album (set to True) and returns "Album {name} has been published."<br>
<br>o	If the album is published, returns "Album {name} is already published."<br>
### -	details()
<br>o	Returns the information of the album, with the songs in it, in the format: <br>
"Album {name}
 == {first_song_info}
 == {second_song_info}
 …
 == {n_song_info}"

The Band class should receive a name (string) upon initialization. It also has an attribute albums (an empty list). 
The class has three methods:
### -	add_album(album: Album)
<br>o	Adds an album to the collection and returns "Band {band_name} has added their newest album {album_name}."<br>
<br>o	If the album is already added, returns "Band {band_name} already has {album_name} in their library."<br>
### -	remove_album(album_name: str)
<br>o	Removes the album from the collection and returns "Album {name} has been removed."<br>
<br>o	If the album is published, returns "Album has been published. It cannot be removed."<br>
<br>o	If the album is not in the collection, returns "Album {name} is not found."<br>
### -	details()
<br>o	Returns the information of the band, with their albums, in this format: <br>
<br>"Band {name}<br>
<br> {album details}<br>
<br> ...<br>
 <br>{album details}"<br>

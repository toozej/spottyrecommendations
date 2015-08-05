# batch add top 5 songs of artists to selected playlist
## discover new artists by seeing if you like their top songs ##

1. read in list of artists names
2. check artist name exists in spotify
3. convert artist name into spotify ID
4. get top 5 tracks for artist's spotify ID
5. pipe those top 5 tracks into a playlist

### Usage
```
./autodisco spotify_connection artist_list playlist_name

where

spotify_connection
API key, username/pass, etc.

artist_list is \n-separated or comma-separated text file

```

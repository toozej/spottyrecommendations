## discover new artists by seeing if you like their top songs ##

This script adds the top 10 songs of each artist you specify and adds them to a playlist of your choosing. The intent is that this will create a quick way to check out new artists' music (likely by "Saving" the playlist for offline or "Always on device" usage). 

### Usage
```
$ cp auth.sh.example auth.sh
$ vim auth.sh # and fill it in!
$ chmod u+x auth.sh
$ ./auth.sh
$ python autodisco.py username playlist_name artist_name ...
```

### Example
'''
$ python autodisco.py myUsername tmp Radiohead Nirvana "Avenged Sevenfold"
'''
Will add the top 10 songs each for Radiohead, Nirvana and Avenged Sevenfold to a playlist called tmp which is owned by myUsername

import pprint
import sys
import os
import subprocess

import spotipy

import spotipy.util as util

def get_artist_id(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]['id']
    else:
        return None

def valid_playlist_id(username, playlist_name):
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist_name in playlist['name']:
            return playlist['id']
        else:
            return '0'

def playlist_contain_track(username, playlist_name, track_name):
    # get playlist
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['owner']['id'] == username:
            results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
            tracks = results['tracks']
            # for each track in playlist
            for item in tracks['items']:
                track = item['track']
                if track['name'] is track_name:
                    print(track_name + " is already in playlist " + playlist_name + ", skipping duplicate")
                    return True
                else:
                    return False

if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
        playlist_name = sys.argv[2]
        artist_name = sys.argv[3:]
    else:
        print "Usage: %s username playlist_name artist_name ..." % (sys.argv[0],)
        sys.exit()

    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(username, scope)

    if token:
        sp = spotipy.Spotify(auth=token)
        playlist_id = valid_playlist_id(username, playlist_name)
        if playlist_id > 0:
            print "has valid playlist"
            for artist in artist_name:
                print( "currently on artist: " + artist)
                # get artist id
                artist_id = get_artist_id(artist)
                # get top tracks
                top_tracks_response = sp.artist_top_tracks(artist_id)
                # put tracks into playlist
                for track in top_tracks_response['tracks']:
                    if not playlist_contain_track(username, playlist_name, track['name']):
                        print("adding track " + track['name'])
                        sp.user_playlist_add_tracks(username, playlist_id, [track['uri']])

        else:
            print("Sorry, " + playlist_name + " is not a valid playlist")
    else:
        print("Can't get token for", username)

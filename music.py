import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from os import environ


# def display(res):
#     list = []
#     for track in enumerate(res['tracks']):
#         list.append(track[1]['name'])
#     list = json.dumps(list)
#     print(list)

x = environ.get('CLIENT_ID')
y = environ.get('CLIENT_SECRET')


def recom(song):
    print(song)
    sp = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials(x, y))

    result = sp.search(q=song, limit=1)
    id_list = [result['tracks']['items'][0]['id']]
    rec = sp.recommendations(seed_tracks=id_list, limit=10)
    # display(rec)
    return rec['tracks']

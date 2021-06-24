import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from os import environ


# def display(res):
#     list = []
#     for track in enumerate(res['tracks']):
#         list.append(track[1]['name'])
#     list = json.dumps(list)
#     print(list)

CLIENT_ID = environ.get('CLIENT_ID')
CLIENT_SECRET = environ.get('CLIENT_SECRET')


def recom(song):
    print(song)
    sp = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET))

    result = sp.search(q=song, limit=1, type='track', market=None)
    try:
        id_list = [result['tracks']['items'][0]['id']]
    except:
        return 'Sorry! Seems like there is no match!'
    rec = sp.recommendations(seed_tracks=id_list, limit=20)

    # display(rec)
    return rec['tracks']

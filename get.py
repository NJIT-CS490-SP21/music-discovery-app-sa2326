import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

CLIENT_ID=os.getenv('CLIENT_ID')
CLIENT_SECRET=os.getenv('CLIENT_SECRET')

auth_url='https://accounts.spotify.com/api/token'
base_url='https://api.spotify.com/v1/'

def get_music_data(artist_id):

    response=requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })
    
    response_data=response.json()
    access_token=response_data['access_token']
    
    headers={
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    
    request=requests.get(base_url + 'artists/' + artist_id + '/top-tracks', 
        headers=headers,
        params={'market':'US'})
    
    response=request.json()
    song_data=response['tracks'][0]
 
    def get_song_name():
        return song_data['name']
    def get_preview_url():
         return song_data['preview_url']
    def get_album_cover():
        return song_data['album']['images'][1]['url']
    def get_artist_name():
        return song_data['artists'][0]['name']
        
    song=get_song_name()
    artist=get_artist_name()
    image=get_album_cover()
    preview=get_preview_url()
    
    my_data=[song, artist, image, preview]
    
    return{'data': my_data}
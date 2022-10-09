from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json
import notion_helpers
import picture

# store spotify environmental variables
from dotenv import load_dotenv
load_dotenv()

# initialize spotipy
spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials())

# get user input
query = input("What album do you want to add to the Notion Database? ")
print()

# search from spotify
results = spotify.search(query, limit=10, type='album')
for i, album in enumerate(results['albums']['items']):
    print("{}. {} by {} ".format(
        i+1, album['name'], [artist['name'] for artist in album['artists']]))

# choose an album
print()
choice = int(input("Choose an album (1-10): "))
album = results['albums']['items'][choice-1]
album_name = album['name']
album_artists = [artist['name'] for artist in album['artists']]
album_released = album['release_date']
album_image = album['images'][0]['url']
album_uri = results['albums']['items'][choice-1]['href']
alblum_external_urls = album['external_urls']['spotify']

star = int(input("album star nums (1-5): "))
star_num = "⭐"* star
print(star_num)
print(album_image)
new_link = picture.save_image_to_github(album_image)
print(new_link)
# create a notion page w proper information and store created page
page_id = notion_helpers.create_page(album_name, album_artists,
                                     album_released, alblum_external_urls, star_num, new_link)

# get album track details
results = spotify.album_tracks(album_uri)
tracks = []
for i, track in enumerate(results['items']):
    tracks.append({
        'number': track['track_number'],
        'name': track['name']
    })

# create header for each track in the album page
notion_helpers.fill_page(tracks, page_id)

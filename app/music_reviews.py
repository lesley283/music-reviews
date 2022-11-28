# this is the "music_reviews.py" file...

# CODE TO REQUEST SPOTIFY DATA WAS ADAPTED FROM THE FOLLOWING LINK:
# https://stmorse.github.io/journal/spotify-api.html
# and https://developer.spotify.com/console/get-search-item/

import requests
import json
from IPython.display import Image, display
import os
from dotenv import load_dotenv

load_dotenv()  # look in the ".env" file for env vars

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

auth_url = 'https://accounts.spotify.com/api/token'

# POST request
auth_response = requests.post(auth_url, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# GET request with proper header
song = input("Please input the title of the song you would like to review: ")
response = requests.get(BASE_URL + 'search?q=' + song +
                        '&type=track&limit=20', headers=headers)

data = json.loads(response.text)

# Cleaning the data
song_ids = []
song_names = []
artist_name = []
album_name = []
album_art = []

for track in data["tracks"]["items"]:
    if track["artists"][0]["name"] not in artist_name:
        song_names.append(track["name"])
        song_ids.append(track["id"])
        artist_name.append(track["artists"][0]["name"])
        album_name.append(track["album"]["name"])
        album_art.append(track["album"]["images"][1]["url"])


# Select which specific song / artist you want
print("Here are all of the songs that we've come up with that might fit your search criteria:")
count = 0
for singer in artist_name:
    print(song_names[count], " by ", singer)
    count = count + 1
print("-------------------")
artist = input(
    "Please input the artist of the correct song you want to review (with correct capitalization): ")

if artist not in artist_name:
    print("Sorry, that artist was not found.")
else:
    index = artist_name.index(artist)

    print("You have selected the following song to review...")
    print("SONG TITLE: " + song_names[index])
    print("ARTIST: " + artist_name[index])
    print("ALBUM TITLE: " + album_name[index])

    # display album image
    from IPython.display import Image, display
    image_url = album_art[index]
    display(Image(url=image_url))

# Add a review
user_review = input("Please write your review for " +
                    song_names[index].upper() + ": ")
user_rating = input(
    "Please rate the song a value out of 5 (with 5 being the best): ")
user_name = input("Please input your username: ")

# Create a list of dictionaries with past reviews...
review_info = {"song": song_names[index], "track id": song_ids[index], "artist": artist_name[index],
               "album": album_name[index], "art": album_art[index], "review": user_review, "rating": user_rating, "user": user_name}
all_reviews = []
all_reviews.append(review_info)

# Print past reviews...
print("Here are recent reviews:")
print("-------------------")
for review in all_reviews:
    print("SONG: " + review["song"] + " by " + review["artist"])
    print("REVIEW: " + review["review"])
    print("RATING: " + review["rating"] + "/5")
    print("USER: " + review["user"])
    print("-------------------")

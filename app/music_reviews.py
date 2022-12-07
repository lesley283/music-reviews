# this is the "music_reviews.py" file...

# Allows user to input reviews

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


def song_input():
    #"""
    #Ask user for song to review and return correct song information.

    #Param: none

    #Returns: song information including title, artist, album title, and album artwork
    #"""
    song = input(
        "Please input the title of the song you would like to review: ")
    response = requests.get(BASE_URL + 'search?q=' +
                            song + '&type=track&limit=20', headers=headers)

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

    while True:
        artist = input(
            "Please input the artist of the correct song you want to review (with correct capitalization). If you do not see the correct song in the list, enter 'NA': ")
        if artist == "NA":
            break
        elif artist in artist_name:
            break
        else:
            print(
                "Sorry, that artist was not found. Please make sure you have used the correct capitalization.")

    if artist in artist_name:
        index = artist_name.index(artist)

        song_info = {"title": song_names[index], "track id": song_ids[index],
                     "artist": artist_name[index], "album": album_name[index], "art": album_art[index]}
        return song_info

    if artist == "NA":
        print("You have indicated that the correct song you want to review is not listed. Please input the song title again, perhaps using different keywords.")
        return None


# call the song input function
chosen_song = None
while chosen_song == None:
    chosen_song = song_input()

# output the chosen song's information

print("You have selected the following song to review...")
print("SONG TITLE: " + chosen_song["title"])
print("ARTIST: " + chosen_song["artist"])
print("ALBUM TITLE: " + chosen_song["album"])

# display album image
image_url = chosen_song["art"]
display(Image(url=image_url))

# ADD A REVIEW
user_review = input("Please write your review for " +
                    chosen_song["title"].upper() + ": ")

test = True
while test == True:
    user_rating = input(
        "Please rate the song using a value from 1 to 5 (with 5 being the best): ")
    try:
        user_rating = int(user_rating)
    except ValueError:
        print("Please make sure you are inputting an integer value.")
        continue

    if user_rating < 1 or user_rating > 5:
        print("Please make sure you are entering a value between 1 and 5.")
        continue

    test = False

user_name = input("Please input your name: ")

# Create a list of dictionaries with past reviews...
chosen_song.update(
    {'review': user_review, 'rating': user_rating, 'user': user_name})
all_reviews = []
all_reviews.append(chosen_song)

print("Thanks! Your review has been submitted.")

# this is the "music_reviews.py" file...

# Allows user to input reviews

# CODE TO REQUEST SPOTIFY DATA WAS ADAPTED FROM THE FOLLOWING LINK:
# https://stmorse.github.io/journal/spotify-api.html
# and https://developer.spotify.com/console/get-search-item/

import requests
import json
from IPython.display import Image, display
from app.spotify import CLIENT_ID, CLIENT_SECRET
import os
from dotenv import load_dotenv
import pickle

def fetch_spotify_data(song):
    """Fetches song data from the Spotify API. Returns a dictionary."""

    auth_url = 'https://accounts.spotify.com/api/token'

    # POST request
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET, })

    # convert the response to JSON
    auth_response_data = auth_response.json()

    # save the access token
    access_token = auth_response_data['access_token']

    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    # base URL of all Spotify API endpoints
    BASE_URL = 'https://api.spotify.com/v1/'

    response = requests.get(BASE_URL + 'search?q=' +
                            song + '&type=track&limit=20', headers=headers)
    data = json.loads(response.text)
    return data

if __name__ == "__main__":

    song = input("Please input the title of the song you would like to review: ")

    data = fetch_spotify_data(song)

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
            "Please input the artist of the correct song you want to review (with correct capitalization): ")
        if artist in artist_name:
            break
        else:
            print("Sorry, that artist was not found. Please make sure you have used the correct capitalization.")

    if artist in artist_name:
        index = artist_name.index(artist)

        song_info = {"title": song_names[index], "track id": song_ids[index],
                     "artist": artist_name[index], "album": album_name[index], "art": album_art[index]}

    # output the chosen song's information

    print("You have selected the following song to review...")
    print("SONG TITLE: " + song_info["title"])
    print("ARTIST: " + song_info["artist"])
    print("ALBUM TITLE: " + song_info["album"])

    # display album image
    image_url = song_info["art"]
    display(Image(url=image_url))

    # ADD A REVIEW
    user_review = input("Please write your review for " +
                        song_info["title"].upper() + ": ")

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

    # update song info with review information
    song_info.update({'review': user_review, 'rating': user_rating, 'user': user_name})

    # open a pickle file
    filename = 'reviews.pk'

    all_reviews = []

    if os.path.exists(filename):
        with open(filename, 'rb') as rfp:
            all_reviews = pickle.load(rfp)

    all_reviews.append(song_info)

    with open(filename, 'wb') as wfp:
        pickle.dump(all_reviews, wfp)

    print("Thanks! Your review has been submitted.")

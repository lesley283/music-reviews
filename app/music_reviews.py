# this is the "music_reviews.py" file...

# Allows user to input reviews

# CODE TO REQUEST SPOTIFY DATA WAS ADAPTED FROM THE FOLLOWING LINK:
# https://stmorse.github.io/journal/spotify-api.html
# and https://developer.spotify.com/console/get-search-item/

import requests
import json
from app.spotify import CLIENT_ID, CLIENT_SECRET
import os
import pickle # used to save reviews into a file that can be accessed between multiple runs of the code

def fetch_spotify_data(song):
    """Fetches song data from the Spotify API. Returns a dictionary of songs that fit the user-inputted search criteria (the parameter: song)."""

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
                            song + '&type=track&limit=20', headers=headers) # if there are a lot of results that match the search criteria, only send back the first 20 songs
    data = json.loads(response.text)
    return data


def open_pickle_file(song_info):
    """Open and store data in a pickle file."""
    """Param song_info includes the song that we want to append to the all reviews list"""

    # Set the filename of the pickle file we are trying to open
    filename = 'reviews.pk'

    # Create an empty list for all reviews, will then load in data to it
    all_reviews = []

    if os.path.exists(filename): # if the pickle file exists already, load the existing reviews into all_reviews
        try:
            with open(filename, 'rb') as rfp:
                all_reviews = pickle.load(rfp)
        except EOFError: # if the pickle file is empty, then all_reviews should be empty an empty list as well
            all_reviews = []

    # add the most recent song review into the all_reviews list
    all_reviews.append(song_info)

    # dump the appended all_reviews list into a pickle file
    with open(filename, 'wb') as wfp:
        pickle.dump(all_reviews, wfp)


def data_cleaning(data):
    """Clean complex data retrieved from the Spotify API."""
    song_names = []
    artist_name = []
    album_name = []
    album_art = []

    for track in data["tracks"]["items"]:
        if track["artists"][0]["name"] not in artist_name: # if the artist hasn't already been added to the list (used to remove duplicate songs by the same artist)
            song_names.append(track["name"])
            artist_name.append(track["artists"][0]["name"])
            album_name.append(track["album"]["name"])
            album_art.append(track["album"]["images"][1]["url"])

    return song_names, artist_name, album_name, album_art


if __name__ == "__main__":

    song = input("Please input the title of the song you would like to review: ")

    data = fetch_spotify_data(song)

    song_names, artist_name, album_name, album_art = data_cleaning(data)

    # Print list of songs that might match search criteria and allow user to select which specific song / artist they want to review
    print("Here are all of the songs that we've come up with that might fit your search criteria:")
    count = 0
    for singer in artist_name:
        print(song_names[count], " by ", singer)
        count = count + 1
    print("-------------------")

    while True:
        artist = input("Please input the artist of the correct song you want to review (with correct capitalization): ")
        if artist in artist_name:
            break
        else:
            print("Sorry, that artist was not found. Please make sure you have used the correct capitalization.")

    # store chosen song and its attributes into a dictionary
    index = artist_name.index(artist)
    song_info = {"title": song_names[index], "artist": artist_name[index], "album": album_name[index], "art": album_art[index]}

    # output the chosen song's information
    print("You have selected the following song to review...")
    print("SONG TITLE: " + song_info["title"])
    print("ARTIST: " + song_info["artist"])
    print("ALBUM TITLE: " + song_info["album"])

    # ADD A REVIEW
    user_review = input("Please write your review for " + song_info["title"].upper() + ": ")

    test = True
    while test == True:
        user_rating = input("Please rate the song using a value from 1 to 5 (with 5 being the best): ")
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

    # update song info dictionary with review information
    song_info.update({'review': user_review, 'rating': user_rating, 'user': user_name})

    # store new review information into a pickle file
    open_pickle_file(song_info)

    print("Thanks! Your review has been submitted.")

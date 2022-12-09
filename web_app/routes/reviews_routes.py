# this is the "web_app/routes/reviews_routes.py" file ...

from flask import Blueprint, request, render_template, redirect, flash

from app.music_reviews import fetch_spotify_data, open_pickle_file, data_cleaning
from web_app.request_method import request_method

reviews_routes = Blueprint("reviews_routes", __name__)

@reviews_routes.route("/add-review")
def song_form():
    print("SONG FORM...")
    return render_template("song_form.html")


@reviews_routes.route("/add-review/list", methods=["GET", "POST"])
def reviews_list():
    print("SONG LIST...")

    request_data = request_method(request) # custom function used to remove duplication in requesting data via POST vs. GET

    song = request_data.get("song") # get song inputted by user via the song form

    try:
        data = fetch_spotify_data(song=song)

        song_names, artist_name, album_name, album_art = data_cleaning(data)

        return render_template("reviews_list.html",
                               song_list=zip(song_names, artist_name, album_name, album_art)
                               )
    except Exception as err:
        print('OOPS', err)

        return redirect("/add-review")


@reviews_routes.route("/add-review/form", methods=["GET", "POST"])
def review_form():
    print("REVIEW FORM...")

    request_data = request_method(request) # custom function used to remove duplication in requesting data via POST vs. GET

    try:
        song_title = request.form['title'] # get all attributes of song that user wants to review
        song_artist = request.form['artist']
        song_album = request.form['album']
        song_art = request.form['art']

        return render_template("review_form.html",
                               song_title=song_title,
                               song_artist=song_artist,
                               song_album=song_album,
                               song_art=song_art
                               )
    except Exception as err:
        print('OOPS', err)

        return redirect("/add-review")


@reviews_routes.route("/add-review/submit", methods=["GET", "POST"])
def submit_form():
    print("SUBMIT FORM...")

    request_data = request_method(request) # custom function used to remove duplication in requesting data via POST vs. GET

    try:
        # get all attributes and review information of song that user has reviewed
        review = request.form['review']
        rating = request.form['rating']
        user = request.form['username']
        title = request.form['title']
        artist = request.form['artist']
        album = request.form['album']

        song_info = {"title": title, "artist": artist,
                    "album": album, "review": review, "rating": rating, "user": user}

        open_pickle_file(song_info=song_info) # load into pickle file for storage

        return render_template("submit_form.html",
                               )
    except Exception as err:
        print('OOPS', err)

        return redirect("/")

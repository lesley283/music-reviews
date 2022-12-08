# this is the "web_app/routes/reviews_routes.py" file ...

from flask import Blueprint, request, render_template, redirect, flash

from app.music_reviews import fetch_spotify_data

reviews_routes = Blueprint("reviews_routes", __name__)

@reviews_routes.route("/add-review")
def song_form():
    print("SONG FORM...")
    return render_template("song_form.html")

@reviews_routes.route("/add-review/list", methods=["GET", "POST"])
def reviews_list():
    print("SONG LIST...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    song = request_data.get("song")

    try:
        data = fetch_spotify_data(song=song)

        # Cleaning the data
        song_ids = []
        song_names = []
        artist_name = []
        album_name = []
        album_art = []

        for track in data["tracks"]["items"]:
            if track["artists"][0]["name"] not in artist_name:
                song_names.append(track["name"])
                artist_name.append(track["artists"][0]["name"])
                album_name.append(track["album"]["name"])
                album_art.append(track["album"]["images"][1]["url"])

        #flash("Fetched Real-time Market Data!", "success")
        return render_template("reviews_list.html",
                               song_list=zip(song_names, artist_name, album_name, album_art)
                               )
    except Exception as err:
        print('OOPS', err)

        #flash("Market Data Error. Please check your symbol and try again!", "danger")
        return redirect("/add-review")


@reviews_routes.route("/add-review/form", methods=["GET", "POST"])
def review_form():
    print("REVIEW FORM...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    song_title = request.form['title']
    song_artist = request.form['artist']
    song_album = request.form['album']
    song_art = request.form['art']

    try:
        return render_template("review_form.html",
                               song_title=song_title,
                               song_artist=song_artist,
                               song_album=song_album,
                               song_art=song_art
                               )
    except Exception as err:
        print('OOPS', err)

        #flash("Market Data Error. Please check your symbol and try again!", "danger")
        return redirect("/add-review/list")


@reviews_routes.route("/add-review/submit", methods=["GET", "POST"])
def submit_form():
    print("SUBMIT FORM...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    title = request.form['title']
    artist = request.form['artist']
    album = request.form['album']
    review = request.form['review']
    rating = request.form['rating']
    user = request.form['user']

    song_info = {"title": title, "artist": artist,
                 "album": album, "review": review, "rating": rating, "user": user}

                 

    try:
        return render_template("submit_form.html",
                               )
    except Exception as err:
        print('OOPS', err)

        #flash("Market Data Error. Please check your symbol and try again!", "danger")
        return redirect("/add-review/form")

# this is the "web_app/routes/search_routes.py" file ...

from app.music_reviews import fetch_spotify_data, open_pickle_file
from flask import Blueprint, request, render_template, redirect, flash
from app.search_reviews import reverse_list
import pickle

search_routes = Blueprint("search_routes", __name__)


@search_routes.route("/search-review")
def search_form():
    print("SEARCH REVIEW FORM...")
    return render_template("search_reviews.html")


@search_routes.route("/search-review/output", methods=["GET", "POST"])
def search_validation():
    print("SEARCH VALIDATION...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    name = request_data.get("name")
    name = name.upper()
    review_level = request_data.get("review_level")

    # load data from pickle file back to memory
    with open('reviews.pk', 'rb') as rfp:
        all_reviews = pickle.load(rfp)

    avg_rating = []
    match_reviews = []
    match_user = []

    for review in all_reviews:
        if (review_level == "artist" and name == review["artist"].upper()) or (review_level == "title" and name == review["title"].upper()) or (review_level == "album" and name == review["album"].upper()):
            avg_rating.append(review["rating"])
            match_reviews.append(review["review"])
            match_user.append(review["user"])

    # if list is empty, there is nothing that matches the search criteria
    if len(avg_rating) == 0:
        flash("There seems to be no reviews for that particular " + review_level + ". Please make sure you have entered the name correctly or leave a review yourself!", "danger")
        return redirect("/search-review")
    else:
        avg_rating = [int(x) for x in avg_rating]
        rating_output = sum(avg_rating) / len(avg_rating)
        rating_output = round(rating_output, 2)

        # reverse list (since most recent reviews are at the back of the list)
        reviews = reverse_list(match_reviews, 5)
        ratings = reverse_list(avg_rating, 5)
        users = reverse_list(match_user, 5)

        try:
            #flash("Fetched Real-time Market Data!", "success")
            return render_template("search_output.html",
                                    name=name,
                                    review_level=review_level,
                                    rating_output=rating_output,
                                    review_list=zip(reviews, ratings, users)
                                )

        except Exception as err:
            print('OOPS', err)
            return redirect("/search-review")

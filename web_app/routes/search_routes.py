# this is the "web_app/routes/search_routes.py" file ...

from flask import Blueprint, request, render_template, redirect, flash
from app.search_reviews import load_pickle_data, load_matching_reviews, reviews_output
from web_app.request_method import request_method

search_routes = Blueprint("search_routes", __name__)


@search_routes.route("/search-review")
def search_form():
    print("SEARCH REVIEW FORM...")
    return render_template("search_reviews.html")


@search_routes.route("/search-review/output", methods=["GET", "POST"])
def search_validation():
    print("SEARCH VALIDATION...")

    request_data = request_method(request) # custom function used to remove duplication in requesting data via POST vs. GET

    try:
        name = request_data.get("name")
        name = name.upper() # convert to uppercase to compare to list of reviews (without case sensitivity)
        review_level = request_data.get("review_level")

        all_reviews = load_pickle_data() # load past reviews from pickle file

        avg_rating, match_reviews, match_user, match_song, match_artist, match_album = load_matching_reviews(name, review_level, all_reviews)

        # if list is empty, there is nothing that matches the search criteria
        if len(avg_rating) == 0:
            flash("There seems to be no reviews for that particular " + review_level + ". Please make sure you have entered the name correctly or leave a review yourself!", "danger")
            return redirect("/search-review")
        else:
            rating_output, reviews, ratings, users, song, artist, album = reviews_output(avg_rating, match_reviews, match_user, match_song, match_artist, match_album) # return the correct output, including 5 most recent reviews and average rating

            return render_template("search_output.html",
                                    name=name,
                                    review_level=review_level,
                                    rating_output=rating_output,
                                    review_list=zip(reviews, ratings, users, song, artist, album)
                                )

    except Exception as err:
        print('OOPS', err)
        return redirect("/search-review")

# this is the "web_app/routes/past_reviews_routes.py" file ...


import pickle
from itertools import islice
from app.search_reviews import reverse_list
from flask import Blueprint, request, render_template, redirect, flash


past_reviews_routes = Blueprint("past_reviews_routes", __name__)


@past_reviews_routes.route("/past-reviews")
def past_reviews():
    print("PAST REVIEWS FORM...")

    try:
        # load data from pickle file back to memory
        with open('reviews.pk', 'rb') as rfp:
            all_reviews = pickle.load(rfp)

        recent_reviews = reverse_list(all_reviews, 10)

        return render_template("past_reviews.html",
                                recent_reviews=recent_reviews)

    except Exception as err:
        print('OOPS', err)

        return redirect("/")

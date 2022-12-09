# this is the "web_app/routes/past_reviews_routes.py" file ...

from app.search_reviews import reverse_list, load_pickle_data
from flask import Blueprint, request, render_template, redirect, flash


past_reviews_routes = Blueprint("past_reviews_routes", __name__)


@past_reviews_routes.route("/past-reviews")
def past_reviews():
    print("PAST REVIEWS FORM...")

    try:
        all_reviews = load_pickle_data()

        recent_reviews = reverse_list(all_reviews, 10)

        return render_template("past_reviews.html",
                                recent_reviews=recent_reviews)

    except Exception as err:
        print('OOPS', err)

        return redirect("/")

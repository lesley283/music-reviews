# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    #return "Welcome Home"
    return render_template("home.html")


#@home_routes.route("/add-review")
#def about():
    #print("Add review...")
    #return "Add review"
    #return render_template("add_review.html")


#@home_routes.route("/search-review")
#def about():
    #print("Search review...")
    #return "Search review"
    #return render_template("search_review.html")

# this is the "web_app/routes/reviews_routes.py" file ...

from flask import Blueprint, request, render_template, redirect, flash

reviews_routes = Blueprint("reviews_routes", __name__)

# this is the "web_app/routes/search_routes.py" file ...

from flask import Blueprint, request, render_template, redirect, flash

search_routes = Blueprint("search_routes", __name__)

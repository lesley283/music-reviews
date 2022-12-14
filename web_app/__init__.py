# this is the "web_app/__init__.py" file...

from flask import Flask
from app.spotify import SECRET_KEY

from web_app.routes.home_routes import home_routes
from web_app.routes.reviews_routes import reviews_routes
from web_app.routes.search_routes import search_routes
from web_app.routes.past_reviews_routes import past_reviews_routes

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    app.register_blueprint(home_routes)
    app.register_blueprint(reviews_routes)
    app.register_blueprint(search_routes)
    app.register_blueprint(past_reviews_routes)
    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)

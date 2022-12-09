# Spotify Review App - OPIM 244 Freestyle Project

This web app allows users to write and read reviews on songs using the Spotify API.

## Setup


Create and activate a virtual environment:

```sh
conda create -n reviews-env python=3.8

conda activate reviews-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration


Log in/sign up for a [Spotify account](https://accounts.spotify.com/en/login), and obtain a [Client ID and Client Secret](https://developer.spotify.com/) from the Spotify Developer Dashboard (i.e. `CLIENT_ID` and `CLIENT_SECRET`).

Then create a local ".env" file and provide the keys like this:

```sh
# this is the ".env" file...

CLIENT_ID="__________________"
CLIENT_SECRET="__________________"
SECRET_KEY="__________________" # secret key used for FLASK web app
```

## Usage

Run the music review app to input reviews (from the command line):

```sh
python -m app.music_reviews
```

Run the search review app to search past reviews (from the command line):
```sh
python -m app.search_reviews
```

## Web App

Run the web app from the command line (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```
## Deploying
View the [Deploying Guide](https://github.com/lesley283/music-reviews/blob/main/DEPLOYING.md) for instructions on deploying to a production server hosted by Heroku.

Visit the deployed website at https://music-reviews-lam.herokuapp.com/

## Testing

Run tests:

```sh
pytest
```
## [License](https://github.com/lesley283/music-reviews/blob/main/LICENSE.md)

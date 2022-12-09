# music-reviews

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
SECRET_KEY="__________________" # used for web app deploying


```

## Usage


Run the music review app to input reviews:

```sh
python -m app.music_reviews
```

Run the search review app to search past reviews:
```sh
python -m app.search_reviews
```


## Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

## Testing

Run tests:

```sh
pytest
```

# music-reviews
# Music review app using the Spotify API

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
```

# this is the "app/spotify.py" file...
# load CLIENT_ID and CLIENT_SECRET from the .env file

import os
from dotenv import load_dotenv

load_dotenv() # look in the ".env" file for env vars

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SECRET_KEY = os.getenv("SECRET_KEY")

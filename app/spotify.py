# this is the "app/spotify.py" file...

import os
from dotenv import load_dotenv

load_dotenv() # look in the ".env" file for env vars

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

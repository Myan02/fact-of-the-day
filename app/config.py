import os
from dotenv import load_dotenv

# load env variables from .env file
load_dotenv()

# set env variables for app use
api_key = os.getenv("API_KEY")
api_url_base = os.getenv("API_URL_BASE")

sender = os.getenv("SENDER")
recipient = os.getenv("RECIPIENT")
password = os.getenv("PASSWORD")
"""
Date: 01/13/2026
Author: Michael Baburyan

Details: 
    - load environment variables from .env file
    - set vars for modules in app to use
"""

import os
from dotenv import load_dotenv
import requests_cache
from retry_requests import retry
import openmeteo_requests

# load env variables from .env file
load_dotenv()

# ----- set env variables for app use ----- #

# weather API
api_url_base_weather = os.getenv("API_URL_BASE_WEATHER")

# facts API
api_key_fact = os.getenv("API_KEY_FACT")
api_url_base_fact = os.getenv("API_URL_BASE_FACT")

# email and server configuration
sender = os.getenv("SENDER")
recipients = os.getenv("RECIPIENTS").split(",")
password = os.getenv("PASSWORD")
host = os.getenv("HOST")
port = os.getenv("PORT")


# ----- set up weather api configs ----- #

# API instance and caching
cache_session = requests_cache.CachedSession(".cache", expire_after=3600)  # cache for 1 hour
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)        # retry failed requests
openmeteo = openmeteo_requests.Client(session=retry_session)               # openmeteo client with custom session

# API params, update with your city coordinates and timezone (curr set to NYC)
latitude = 40.7433
longitude = -73.855
timezone = "America/New_York"
"""
Date: 01/13/2026
Author: Michael Baburyan

Details: 
    - fetch data from different apis
    - return data as a string
    - data differs based on api endpoint provided as parameter
"""

import requests
from weather_params import params
from config import api_key_fact, api_url_base_fact, api_url_base_weather, openmeteo


# return a fact
def getFact(endpoint: str) -> str:
    try:
        # request fact from api, input credentials, convert to dictionary
        response = requests.get(url=f"{api_url_base_fact}/{endpoint}", headers={"X-Api-Key":api_key_fact}).json()
    except Exception as e:
        raise Exception(f"Bad Response: {e}")
    
    # initial response format: [{"fact": "..."}]
    return response[0]["fact"]

def getWeather():
    try:
        response = openmeteo.weather_api(api_url_base_weather, params=params)
    except Exception as e:
        raise Exception(f"Bad Response: {e}")

    response = response[0]

    hourly = response.Hourly()
    


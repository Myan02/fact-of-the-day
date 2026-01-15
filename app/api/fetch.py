"""
Date: 01/13/2026
Author: Michael Baburyan

Details: 
    - fetch data from different apis
    - return data as a string or pandas dataframes
    - data differs based on api endpoint or parameters
"""

import requests
import pandas as pd

from api.weather_configs import getParams, getHourlyWeather, getDailyWeather
from config import api_key_fact, api_url_base_fact, api_url_base_weather, openmeteo

# return a fact
def getFact(endpoint: str) -> str:
    try:
        # request fact from api, input credentials, convert to dictionary
        response = requests.get(url=f"{api_url_base_fact}/{endpoint}", headers={"X-Api-Key":api_key_fact}).json()
    except Exception as e:
        raise Exception(f"Bad Response: {e}")
    
    # response format: [{"fact": "..."}]
    return response[0]["fact"]

# return weather for the day
def getWeather() -> tuple[pd.DataFrame, ...]:
    try:
        # request weather info form api, input api url and parameters of the endpoint query
        responses = openmeteo.weather_api(api_url_base_weather, params=getParams())
    except Exception as e:
        raise Exception(f"Bad Response: {e}")

    # set response to info locale, 0 for first and only requested location
    response = responses[0]

    # configure data into pandas dataframes
    hourly_dataframe = getHourlyWeather(response)
    daily_dataframe = getDailyWeather(response)

    # response format: (DataFrame, DataFrame)
    return hourly_dataframe, daily_dataframe
    


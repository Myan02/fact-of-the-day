"""
Date: 01/13/2026
Author: Michael Baburyan

Details: 
    - fetch data from fact api
    - return data as a string
    - data differs based on api endpoint provided as parameter
"""

import requests
from config import api_key, api_url_base

# return a fact
def getFact(endpoint: str) -> str:
    try:
        # request fact from api, input credentials, convert to dictionary
        response = requests.get(url=f"{api_url_base}/{endpoint}", headers={"X-Api-Key":api_key}).json()
    except Exception as e:
        raise Exception(f"Bad Response: {e}")
    
    # initial response format: [{"fact": "..."}]
    return response[0]["fact"]
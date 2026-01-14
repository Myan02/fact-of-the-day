import requests
from config import api_key, api_url_base

# return a random fact
def getRandomFact() -> str:
    try:
        response = requests.get(url=f"{api_url_base}/facts", headers={"X-Api-Key":api_key}).json()
    except Exception as e:
        raise Exception(f"Bad Response: {e}")
    

    return response[0]["fact"]


# return the fact of the day
def getFactOfTheDay() -> str:
    try:
        response = requests.get(url=f"{api_url_base}/factoftheday", headers={"X-Api-Key":api_key}).json()
    except Exception as e:
        raise Exception(f"Bad Response: {e}")
    
    return response[0]["fact"]
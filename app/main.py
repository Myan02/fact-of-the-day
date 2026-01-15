"""
Date: 01/13/2026
Author: Michael Baburyan

Details: 
    - call getFact from queries to retrieve facts
    - send an email with those facts
"""
from api.fetch import getFact, getWeather
from routing.emails import Email

def main():
    # retrieve data from apis
    random_fact = getFact("facts")
    fact_of_the_day = getFact("factoftheday")
    hourly_weather, daily_weather = getWeather()

    # set email parameters as dict
    email_parameters = {
        "random_fact": random_fact,
        "fact_of_the_day": fact_of_the_day,
        "hourly_weather": hourly_weather,
        "daily_weather": daily_weather
    }

    # initialize a new email and send it with params
    email = Email()
    email.createEmail(email_parameters)
    email.sendEmail()

if __name__ == "__main__":
    main()
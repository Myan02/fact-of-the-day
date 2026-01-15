"""
Date: 01/13/2026
Author: Michael Baburyan

Details: 
    - call getFact from queries to retrieve facts
    - send an email with those facts
"""

# modules
from app.api.fetch import getFact
from routing.emails import Email

def main():
    rand_fact = getFact("facts")            # retrieve random fact
    daily_fact = getFact("factoftheday")   # get fact of the day

    # initialize a new email and send it with the facts
    email = Email()
    email.createEmail(random_fact=rand_fact, fact_of_the_day=daily_fact)
    email.sendEmail()

if __name__ == "__main__":
    main()
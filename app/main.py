import config
from facts.queries import getRandomFact, getFactOfTheDay
from routing.format import newEmail

def main():
    newEmail(getRandomFact(), getFactOfTheDay())

if __name__ == "__main__":
    main()
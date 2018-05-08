import requests
from bs4 import BeautifulSoup
from db import DBConn
from api import QuotesAPI

AUTHOR = "Mahatma Gandhi"
DB_NAME = 'quotes.db'

def format_quote(q):
    """
    Given an author and a correspond quote, format it nicely.
    """
    return "{}\n\t\t-{}".format(q["quote"], q["author"])

def main():
    """
    Main function that runs our stuff.
    """
    db = DBConn(DB_NAME)
    print(format_quote(db.get_random_quote()))
    # qapi = QuotesAPI()
    # quotes = qapi.get_quotes(AUTHOR)
    # num_quotes = len(quotes)
    # if num_quotes > 0:
    #     print("Inserting {} quotes for {}".format(num_quotes ,AUTHOR))
    #     db.insert_quotes(quotes)
    # else:
    #     print("No quotes for {}".format(AUTHOR))

main()

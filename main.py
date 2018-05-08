import requests
from bs4 import BeautifulSoup
from db import DBConn
from api import QuotesAPI

AUTHOR = "Mahatma Gandhi"
BASE_URL = "https://www.brainyquote.com/authors/"
DB_NAME = 'quotes.db'

def main():
    """
    Main function that runs our stuff.
    """
    db = DBConn(DB_NAME)
    qapi = QuotesAPI()
    quotes = qapi.get_quotes(AUTHOR)
    num_quotes = len(quotes)
    if num_quotes > 0:
        print("Inserting {} quotes for {}".format(num_quotes ,AUTHOR))
        db.insert_quotes(quotes)
    else:
        print("No quotes for {}".format(AUTHOR))

main()

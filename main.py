import requests
from bs4 import BeautifulSoup
from db import DBConn

AUTHOR = "Epictetus"
BASE_URL = "https://www.brainyquote.com/authors/"
DB_NAME = 'quotes.db'

def format_author(auth):
    """
    Given the name of an author, format it so that it can be appended to the
    end of a url
    """
    return auth.lower().replace(' ', '_')

def build_url(auth):
    """
    Build a url pointing to the location of quotes associated with the given
    author.
    """
    return "{}{}".format(BASE_URL, format_author(auth))

def get_quotes(auth):
    """
    Scrape quotes from BrainyQuote for a given author.
    """
    url = build_url(auth)
    r = requests.get(url)
    if not r.status_code == requests.codes.ok:
        return []
    soup = BeautifulSoup(r.text, 'html.parser')
    quotes = soup.find_all('a', {'class': 'b-qt', 'title': 'view quote'})
    return list(map(lambda q: (auth, q.contents[0]), quotes))

def main():
    """
    Main function that runs our stuff.
    """
    db = DBConn(DB_NAME)
    quotes = get_quotes(AUTHOR)
    num_quotes = len(quotes)
    if num_quotes > 0:
        print("Inserting {} quotes for {}".format(num_quotes ,AUTHOR))
        db.insert_quotes(quotes)
    else:
        print("No quotes for {}".format(AUTHOR))

main()

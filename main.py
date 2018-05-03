import requests
from bs4 import BeautifulSoup

AUTHOR = "Marcus Aurelius"
BASE_URL = "https://www.brainyquote.com/authors/"

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
    return list(map(lambda q: q.contents[0],quotes))

def main():
    """
    Main function that runs our stuff.
    """
    print(get_quotes(AUTHOR))

main()

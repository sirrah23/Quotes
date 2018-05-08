import requests
from bs4 import BeautifulSoup
from db import DBConn


class QuotesAPI:
    """
    Connect to the BrainyQuotes website and grab quotes for a given author.
    """

    def __init__(self):
        self.base_url = "https://www.brainyquote.com/authors/"

    def format_author(self, auth):
        """
        Given the name of an author, format it so that it can be appended to the
        end of a url
        """
        return auth.lower().replace(' ', '_')

    def build_url(self, auth):
        """
        Build a url pointing to the location of quotes associated with the given
        author.
        """
        return "{}{}".format(self.base_url, self.format_author(auth))

    def get_quotes(self, auth):
        """
        Scrape quotes from BrainyQuote for a given author.
        """
        url = self.build_url(auth)
        r = requests.get(url)
        if not r.status_code == requests.codes.ok:
            return []
        soup = BeautifulSoup(r.text, 'html.parser')
        quotes = soup.find_all('a', {'class': 'b-qt', 'title': 'view quote'})
        return list(map(lambda q: (auth, q.contents[0]), quotes))

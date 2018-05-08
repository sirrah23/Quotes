import textwrap
from db import DBConn
from api import QuotesAPI
import click

DB_NAME = 'quotes.db'

@click.group()
def cli():
    pass

@click.command()
def quote():
    """Get a random quote from the database."""

    def format_quote(q):
        """
        Given an author and a correspond quote, format it nicely.
        """
        quote_str = textwrap.fill(q["quote"], 50)  # Wrap the quote if it gets too long
        author_str = "\t\t-{}".format(q["author"])
        return "{}\n{}".format(quote_str, author_str)

    db = DBConn(DB_NAME)
    rand_quote = db.get_random_quote()
    if rand_quote:
        click.echo(format_quote(rand_quote))
    else:
        click.echo("No quotes to show...database is empty")

@click.command()
@click.argument("author")
def add(author):
    """Add quotes for an author to the database."""
    db = DBConn(DB_NAME)
    q_api = QuotesAPI()
    scraped_quotes = q_api.get_quotes(author)
    num_quotes = len(scraped_quotes)
    if num_quotes > 0:
        click.echo("Inserting {} quotes for {}".format(num_quotes ,author))
        db.insert_quotes(scraped_quotes)
    else:
        print("No quotes found for {}".format(author))

cli.add_command(quote)
cli.add_command(add)

if __name__ == "__main__":
    cli()

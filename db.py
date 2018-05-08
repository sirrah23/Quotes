import sqlite3

class DBConn:
    """
    The database connection object that can be used to read/write quotes
    from/to the database.
    """

    def __init__(self, name):
        self.name = name
        self.conn = None
        self._connect()
        self._create_tables()

    def __del__(self):
        self._disconnect()

    def _connect(self):
        self.conn = sqlite3.connect(self.name)

    def _disconnect(self):
        self.conn.close()

    def _create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS quote (author text, quote text)""")
        self.conn.commit()

    def insert_quotes(self, quotes):
        """
        Insert one or more quotes into the database for a given a list of (author,
        quote) tuples.
        """
        cursor = self.conn.cursor()
        cursor.executemany("""INSERT INTO quote (author, quote) VALUES (?, ?)""", quotes)
        self.conn.commit()

    def get_random_quote(self):
        """
        Grab a random quote from the database.
        """
        cursor = self.conn.cursor()
        cursor.execute("""SELECT * FROM quote ORDER BY RANDOM() LIMIT 1""")
        res = cursor.fetchone()
        return {"author": res[0], "quote": res[1]}

import sqlite3

class DBConn:

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
        cursor = self.conn.cursor()
        cursor.executemany("""INSERT INTO quote (author, quote) VALUES (?, ?)""", quotes)
        self.conn.commit()

from tkinter import *
from db import DBConn

DB_NAME = "../quotes.db"  #TODO: Make this configurable

class QuoteApp:

    def __init__(self, master, qdb, refresh_rate=10000):
        self.qdb = qdb
        self.master = master
        self.refresh_rate = refresh_rate
        self.message = None
        self.update_quote()
        frame = Frame(master, width=600, height=125, bg="", colormap="new")
        frame.pack(anchor="center")
        frame.pack_propagate(0)
        self.create_label()

    def update_quote(self):
        """
        Grab a random quote from the database for display to the user.
        """
        self.quote = self.qdb.get_random_quote()

    def get_display_msg(self):
        """
        Get the message to display to the user, whether it's a formatted quote
        or an error message.
        """
        if not self.quote:
            return "***NO QUOTES IN THE DATABASE***"
        else:
            return "{}\n\n\t\t-{}".format(self.quote["quote"], self.quote["author"])

    def create_label(self):
        """
        Create the label widget which contains the text that is displayed to
        the user.
        """
        if self.message:
            self.message.destroy()
        self.message = Label(self.master, wraplength=550, text=self.get_display_msg())
        self.message.place(relx=.1, rely=.5, anchor="nw")

    def refresh(self):
        """
        Display a new quote on the screen. 
        """
        self.update_quote()
        self.create_label()
        self.master.after(self.refresh_rate, self.refresh)


if __name__ == "__main__":
    # Establish a database connection
    qdb = DBConn(DB_NAME)
    # Create the main GUI 
    root = Tk()
    # Initialize the app
    app = QuoteApp(root, qdb)
    # Set up the code to refresh the quotes every X seconds
    app.refresh()
    # Run the GUI
    root.mainloop()

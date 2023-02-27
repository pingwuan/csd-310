""" 
    Title: pysports_queires.py
    Author: Alexander Taylor
    Date: 2/26/2023
    Description: Whatabook program
"""

#imports
import mysql.connector
from mysql.connector import errorcode

#database config
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

def show_menu():

def show_books(_cursor):

def show_locations(_cursor):

def validate_user():

def show_account_menu():

def show_wishlist(_cursor, _user_id):

def show_books_to_add(_cursor, _user_id):

def add_book_to_wishlist(_cursor, _user_id, _book_id):



# handle the error
except mysql.connector.errors.ProgrammingError as err:
    print(f"An error occurred: {err.msg}")

# finally block to close database
finally:

    db.close()
""" 
    Title: pysports_join_queries.py
    Author: Alexander Taylor
    Date: 2/15/2023
    Description: Test program for joining the player and team tables
"""

""" import statements """
import mysql.connector
from mysql.connector import errorcode


""" database config object """
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# try and catch blocks in the event of any sql errors
try:

    db = mysql.connector.connect(**config) # connect to the pysports database 

    cursor = db.cursor()

    # sql code and cursor object initialization
    sql_join = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id"
    cursor.execute(sql_join)

    # load data from cursor
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS --")
    
    # loop over the player data and display results 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press enter key to continue... ")


# handle the error
except mysql.connector.errors.ProgrammingError as err:
    print(f"An error occurred: {err.msg}")

# finally block to close database 
finally:

    db.close()
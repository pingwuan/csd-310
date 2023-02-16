""" 
    Title: pysports_update_and_delete.py
    Author: Alexander Taylor
    Date: 2/15/2023
    Description: Test program for inserting, updating, and deleting records from the pysports database
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

# function to execute sql commands and display results in terminal window.
def show_players(cursor, title):

    # INITIAL JOIN 
    sql_join = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id"
    cursor.execute(sql_join)
    players = cursor.fetchall()

    # format title for better display 
    print("\n  -- {} --".format(title))
    
    # loop over the player data and display results 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

# try and catch blocks in the event of any sql errors
try:

    db = mysql.connector.connect(**config) # connect to the pysports database 
    
    # define cursor
    cursor = db.cursor()

    # INSERT PLAYER SECTION
    sql_insert = "INSERT INTO player(first_name, last_name, team_id)""VALUES(%s, %s, %s)"
    add_player = (sql_insert)
    player_data = ("Smeagol", "Shire Folk", 1)
    cursor.execute(add_player, player_data)
    db.commit()
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    # UPDATE PLAYER SECTION 
    sql_update = "UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'"
    update_player = (sql_update)
    cursor.execute(update_player)
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    # DELETE PLAYER SECTION
    sql_delete = "DELETE FROM player WHERE first_name = 'Gollum'"
    delete_player = (sql_delete)
    cursor.execute(delete_player)
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n  Press enter key to continue... ")

# handle the error
except mysql.connector.errors.ProgrammingError as err:
    print(f"An error occurred: {err.msg}")

# finally block to close database
finally:

    db.close()
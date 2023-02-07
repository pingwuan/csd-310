""" 
    Title: pysports_queires.py
    Author: Alexander Taylor
    Date: 2/7/2023
    Description: Working with the pysports database
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


#try block for errors
try:
    db = mysql.connector.connect(**config) # connect to the pysports database 
    
    # output the connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    
    cursor = db.cursor()

    # select query from the team table 
    sql_team = "SELECT team_id, team_name, mascot FROM team"
    cursor.execute(sql_team)

    # generate teams list
    teams = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")
    
    # loop team data and print
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    # select query for the player table 
    sql_player = "SELECT player_id, first_name, last_name, team_id FROM player"
    cursor.execute(sql_player)

    # generate players list 
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING PLAYER RECORDS --")

    # loop player data and print
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()
"""
    Title: mongodb_test.py
    Author: Alexander Taylor
    Date: 1/27/2023
    Description: Test program for connecting to a MongoDB Atlas cluster
"""
    

"""import statements"""
from pymongo import MongoClient

# MongoDB Connection String
url = "mongodb+srv://admin:admin@cluster0.khvkhso.mongodb.net/?retryWrites=true&w=majority"

#Connect to MongoDB cluster
client = MongoClient(url)

#connect to pytech database
db = client.pytech

#show connected collections
print("\n -- Pytech Collection List --")
print(db.list_collection_names())

#show an exit message
input("\n\n  End of program, press enter key to exit... ")
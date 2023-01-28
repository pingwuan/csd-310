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

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# get the students collection 
students = db.students

# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# find document by student_id
tali = students.find_one({"student_id": "1008"})

# output the results 
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + tali["student_id"] + "\n  First Name: " + tali["first_name"] + "\n  Last Name: " + tali["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press enter key to continue...")

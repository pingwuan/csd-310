""" 
    Title: pytech_insert.py
    Author: Alexander Taylor
    Date: 01/27/2023
    Description: Test program for inserting new documents 
                 into the students collection 
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.khvkhso.mongodb.net/?retryWrites=true&w=majority"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

""" three student documents"""
# Liara Tsoni's data document 
liara = {
    "student_id": "1007",
    "first_name": "Liara",
    "last_name": "Tsoni",
    "enrollments": [
        {
            "term": "Fall",
            "gpa": "4.0",
            "start_date": "October 01, 2022",
            "end_date": "March 05, 2023",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Database Security",
                    "instructor": "Henry Le",
                    "grade": "A+"
                },
                {
                    "course_id": "CYBR420",
                    "description": "Cyber Investigations",
                    "instructor": "Anthony Geron",
                    "grade": "A+"
                }
            ]
        }
    ]

}

# Tali Zorah's data document 
tali = {
    "student_id": "1008",
    "first_name": "Tali",
    "last_name": "Zorah",
    "enrollments": [
        {
            "term": "Fall",
            "gpa": "4.0",
            "start_date": "October 01, 2022",
            "end_date": "March 05, 2023",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Database Security",
                    "instructor": "Henry Le",
                    "grade": "A+"
                },
                {
                    "course_id": "CYBR420",
                    "description": "Cyber Investigations",
                    "instructor": "Anthony Geron",
                    "grade": "A+"
                }
            ]
        }
    ]

}

# commander shepard's data document 
commander = {
    "student_id": "1009",
    "first_name": "Commander",
    "last_name": "Shepard",
    "enrollments": [
        {
            "term": "Fall",
            "gpa": "3.0",
            "start_date": "October 01, 2022",
            "end_date": "March 05, 2023",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Database Security",
                    "instructor": "Henry Le",
                    "grade": "C+"
                },
                {
                    "course_id": "CYBR420",
                    "description": "Cyber Investigations",
                    "instructor": "Anthony Geron",
                    "grade": "A-"
                }
            ]
        }
    ]

}


# get the students collection 
students = db.students

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
liara_student_id = students.insert_one(liara).inserted_id
print("  Inserted student record Liara T'shoni into the students collection with document_id " + str(liara_student_id))

tali_student_id = students.insert_one(tali).inserted_id
print("  Inserted student record Tali'zorah into the students collection with document_id " + str(tali_student_id))

commander_student_id = students.insert_one(commander).inserted_id
print("  Inserted student record Commander Shepard into the students collection with document_id " + str(commander_student_id))

input("\n\n  End of program, press enter key to exit... ")
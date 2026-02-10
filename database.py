import pymongo
if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/") #Defualt port for MongoDB is 27017
    print(client)
    db = client["Student_Performance_Database"]
    collection = db["Student_Performance_Collection"]
    student = [{
    "name": "Aman",
    "attendance": 80,
    "study_hours": 5,
    "internal_marks": 70,
    "result": 1},
    {"name": "Karamjass Kaur",
    "attendance": 85,
    "study_hours": 6,
    "internal_marks": 95,
    "result": 1},{"name": "Gurpreet Kaur",
    "attendance": 65,
    "study_hours": 7,
    "internal_marks": 65,
    "result": 2},{"name": "Simran Kaur",
    "attendance": 90,
    "study_hours": 8,
    "internal_marks": 85,
    "result": 1},{"name": "Harpreet Kaur",
    "attendance": 70,   
    "study_hours": 4,
    "internal_marks": 75,
    "result": 2}]
#insert_one() is used to insert one record in the collection
collection.insert_many(student) # Uesd to insert many records in the collection

print("Data inserted successfully")
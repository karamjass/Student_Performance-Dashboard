import pymongo
if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client["Student_Performance_Database"]
    collection = db["Student_Performance_Collection"]
    #Delete One
    rec ={"name" : "Aman"}
    collection.delete_one(rec)
from pymongo import MongoClient
from bson.objectid import ObjectId


if __name__ == "__main__":
    mongo = MongoClient(host='localhost', port=27017)

    # create a DB
    db = mongo.learn
    # get a reference to a collection
    collection = db.student

    """
    # Insert a new document
    a_doc = {
        'name': 'Piera Nassisi',
        'age': 23,
        'interests': ['Gym', "Gymnastic"]
    }
    collection.insert_one(a_doc)
    """

    object_id = ObjectId("624df55ac805794c31a28ceb")
    # collection.update_one({"_id": object_id}, {"$set": {'name': 'Maria Elena Oliva'}})
    student = collection.find_one({"_id": object_id})
    print(student)

    for student in collection.find({}):
        print(student)
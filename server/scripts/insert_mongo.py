import pymongo
import sys


username = sys.argv[1]
password = sys.argv[2]

client = pymongo.MongoClient("mongodb+srv://{}:{}@phoenixsix-x4wdj.gcp.mongodb.net/test".format(username,password))

resume_blob = {
    "resume": {
        "id": 12345,
        "rid": 56789,
        "tags": [{
            "content": "filter"
        }],
        "views": 1,
        "shares": 1,
        "url": "string",
        "valid": True,
        "vector": "      ",
        "source": " "
    }
}


db = client.test_database
db = client["test-database"]
collection = db.test_collection
collection = db["test-collection"]

resumes = db.resumes


resume_id = resumes.insert_one(resume_blob).inserted_id

import pprint

print("inserted blob: ")

pprint.pprint(resumes.find_one())

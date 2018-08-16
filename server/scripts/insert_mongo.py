import pymongo
import sys
import os

username = os.environ.get("MONGO_USERNAME")
password = os.environ.get("MONGO_PASSWORD")


username = "vib-alt"
password = "lollol123!"


client = pymongo.MongoClient("mongodb+srv://{}:{}@phoenixsix-x4wdj.gcp.mongodb.net/test".format(username,password))

with open("../resume_scraper/vp.pdf","rb") as f:
    data = f.read()

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
        "raw": data,
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

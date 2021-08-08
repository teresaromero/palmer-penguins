from os import abort as exit
from bson.objectid import ObjectId
from pymongo.database import Database
from app import app
from flask_pymongo import PyMongo
from config import MONGO_URI

mongo = PyMongo(app, uri=MONGO_URI, serverSelectionTimeoutMS=5000)
try:
    mongo.db.command('ping')
    app.logger.info("MongoDB connexion successful")
except Exception as e:
    app.logger.error(f"MongoDB connexion: {str(e)}")
    exit()


def findAll(coll: str, query={}, project=None, db: Database = mongo.db):
    collection = db[coll]
    return collection.find(query, project)


def findOne(coll: str, query={}, project=None, db: Database = mongo.db):
    collection = db[coll]
    return collection.find_one(query, project)


def findByIdAndUpdate(coll: str, id: str, set: dict, project=None, db: Database = mongo.db):
    collection = db[coll]
    query = {"_id": ObjectId(id)}
    raw_result = collection.update_one(query, {'$set': set})
    if raw_result.matched_count == 0:
        raise Exception("doc_not_found")
    if raw_result.modified_count == 0:
        raise Exception("doc_not_updated")
    return collection.find_one(query, project)


def validate_collection(collection: str):
    return collection in mongo.db.list_collection_names()

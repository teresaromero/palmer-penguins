from os import abort as exit

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

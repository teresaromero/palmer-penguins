from flask_pymongo import PyMongo
from config import MONGO_URI
from app import app
import os

mongo = None
try:
    mongo = PyMongo(app, uri=MONGO_URI, serverSelectionTimeoutMS=5000)

    mongo.db.command('ping')
    app.logger.info("MongoDB connexion successful")

except Exception as e:
    print(MONGO_URI)
    app.logger.error(str(e))
    os._exit(1)


def collection(name): return mongo.db[name]


def penguins_collection():
    return collection("kaggle-penguins-lter")

from flask_pymongo import PyMongo
from app import app

mongo = PyMongo(app)


def collection(name): return mongo.db[name]


penguins_collection = collection("kaggle-penguins-lter")

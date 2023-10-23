from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values(".env")

client = MongoClient(config["MONGODB_CONNECTION_URI"])

db = client.user_db

collection_name = db["user_collection"]
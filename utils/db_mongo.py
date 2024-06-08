from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGODB_URI)
mongo_db = client.get_database()

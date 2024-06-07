from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client.bibliotheque

livres = db.livres
adherents = db.adherents
prets = db.prets


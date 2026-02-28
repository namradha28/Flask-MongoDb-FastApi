from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["studentdb"]
collection = db["students"]
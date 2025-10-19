from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
DB_NAME = os.getenv("DB_NAME")

client = MongoClient(MONGODB_URL)
db = client[DB_NAME]

personajes_collection = db["personajes"]

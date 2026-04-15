from pymongo import MongoClient 
from sources.config.settings import settings 

def save_to_mongodb(document: dict) -> None :
    if not settings.MONGO_URI: 
        raise ValueError("MONGO_URI is missing in environment variables")
    
    client = MongoClient(settings.MONGO_URI)

    db = client["gold_db"] # database name: gold_db
    collection = db["prices"] #collection name : prices

    collection.insert_one(document)

    client.close()
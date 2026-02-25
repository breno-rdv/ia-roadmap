from pymongo import MongoClient
from bson.objectid import ObjectId
import json

# MongoDB connection
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "your_database_name"
COLLECTION_NAME = "your_collection_name"

def get_document_by_id(doc_id):
    """Retrieve a document from MongoDB by ID"""
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    
    try:
        # Convert string to ObjectId if needed
        if isinstance(doc_id, str):
            doc_id = ObjectId(doc_id)
        
        document = collection.find_one({"_id": doc_id})
        return document
    finally:
        client.close()

# Example usage
if __name__ == "__main__":
    doc_id = "your_document_id_here"
    result = get_document_by_id(doc_id)
    print(result)
import sys
import os
import queue
import pymongo
from pymongo import MongoClient
#-----------------------------------------------------------------------
# _DATABASE_URL = os.environ.get('DATABASE_URL')
_DATABASE_URL = "mongodb+srv://tigerplan333:TigerPlan123!@tigerplandata.yyrhywn.mongodb.net/"
print(_DATABASE_URL) 
_connection_pool = queue.Queue()

def _get_connection():
    try:
        conn = _connection_pool.get(block=False)
    except queue.Empty:
        conn = MongoClient(_DATABASE_URL)
    return conn

def _put_connection(conn):
    _connection_pool.put(conn)

#-----------------------------------------------------------------------
# Connect to MongoDB
def delete_dupilcates_from_collection(collection_name):
    try:
        # Get connection
        client = _get_connection()
        # Query database
        # Connect to MongoDB
        print("Connected to MongoDB successfully!")
        db = client['TigerPlanData']
        collection = db[collection_name]

        # Define aggregation pipeline to identify non-unique documents
        # Define aggregation pipeline to identify and retain unique courses
        # MongoDB aggregation pipeline to identify duplicate course_id values
        if collection_name == "CoursesData":
            pipeline = [
                {"$group": {
                    "_id": {"course_id": "$course_id", "subject": "$subject", "catalog_number": "$catalog_number"},
                    "ids": {"$push": "$_id"},  # Collect all document IDs into an array
                    "count": {"$sum": 1}
                }},
                {"$match": {
                    "count": {"$gt": 1}  # Find groups with more than one document (i.e., duplicates)
                }}
            ]
        else: 
        # MongoDB aggregation pipeline to identify duplicate course_id values
            pipeline = [
                {
                    '$group': {
                        '_id': '$id',
                        'count': {'$sum': 1}
                    }
                },
                {
                    '$match': {
                        'count': {'$gt': 1}  # Filter to include only course_id values with duplicates
                    }
                }
            ]

        # Execute aggregation pipeline to identify duplicate course_id values
        cursor = collection.aggregate(pipeline)

        # List to store additional documents to delete
        docs_to_delete = []

        # Iterate over cursor to collect documents with duplicate course_id
        for doc in cursor:
            
            course_id = doc['_id']['course_id']
            subject_name = doc['_id']['subject']
            catalog_num = doc['_id']['catalog_number']
            # Find all documents with the duplicate course_id
            duplicates = list(collection.find({'course_id': course_id, 'subject': subject_name, 'catalog_number': catalog_num}))
            # Skip the first document (keep one) and collect others for deletion
            if len(duplicates) > 1:
                docs_to_delete.extend(duplicates[1:])
        # Bulk delete operation to remove additional (duplicate) entries
        if docs_to_delete:
            ids_to_delete = [course['_id'] for course in docs_to_delete]
            result = collection.delete_many({'_id': {'$in': ids_to_delete}})
            for item in result: 
                for course in item:
                    print("Deleted ", course['subject'], course['catalog_number'], 'for term ', course['term_code'])
            # collection.bulk_write([pymongo.DeleteOne({'_id': doc['_id']}) for doc in docs_to_delete])
            print(f"Deleted {result.deleted_count} duplicate entries.")

    except Exception as e:
        print(f"Error removing duplicates: {e}")

    finally: 
        _put_connection(client)
 
# delete_dupilcates_from_collection("CoursesData")
client = _get_connection()
db = client["TigerPlanData"]
collection = db['CrossDump']
deleted = collection.delete_many({'term': '1252'})

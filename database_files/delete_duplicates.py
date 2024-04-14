import sys
import os
import queue
import pymongo
from pymongo import MongoClient
#-----------------------------------------------------------------------
_DATABASE_URL = os.getenv('DATABASE_URL')
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

try:
    # Get connection
    client = _get_connection()
    # Query database
    # Connect to MongoDB
    print("Connected to MongoDB successfully!")
    db = client['TigerPlanData']
    collection = db['CrossDump']

    # Define aggregation pipeline to identify non-unique documents
    # Define aggregation pipeline to identify and retain unique courses
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
        course_id = doc['_id']
        # Find all documents with the duplicate course_id
        duplicates = list(collection.find({'id': course_id}))
        # Skip the first document (keep one) and collect others for deletion
        if len(duplicates) > 1:
            docs_to_delete.extend(duplicates[1:])
    # Bulk delete operation to remove additional (duplicate) entries
    if docs_to_delete:
        result = collection.bulk_write([pymongo.DeleteOne({'_id': doc['_id']}) for doc in docs_to_delete])
        print(f"Deleted {result.deleted_count} duplicate entries.")

except Exception as e:
        print(f"Error removing duplicates: {e}")

finally: 
    _put_connection(client)
 
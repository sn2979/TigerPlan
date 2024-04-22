import sys
import os
import queue
from pymongo import MongoClient

# _DATABASE_URL = os.environ['DATABASE_URL'] # = mongodb+srv://tigerplan333:TigerPlan123!@tigerplandata.yyrhywn.mongodb.net/?retryWrites=true&w=majority&appName=TigerPlanData
_connection_pool = queue.Queue()

def _get_connection():
    try:
        conn = _connection_pool.get(block=False)
    except queue.Empty:
        # conn = MongoClient(_DATABASE_URL)
        conn = MongoClient("mongodb+srv://tigerplan333:TigerPlan123!@tigerplandata.yyrhywn.mongodb.net/?retryWrites=true&w=majority&appName=TigerPlanData")
    return conn

def _put_connection(conn):
    _connection_pool.put(conn)

#-----------------------------------------------------------------------
# Connect to MongoDB

try:
        # Get connection
        client = _get_connection()
        db = client['TigerPlanData']
        courses_data_collection = db['CoursesData']
        print("Connected to MongoDB successfully!")
        cross_dump_collection = db['CrossDump']
# Define the aggregation pipeline to group by course_id and collect titles
        pipeline = [
            {
                '$group': {
                    '_id': '$course_id',  # Group by unique course_id
                    'title': {'$first': '$title'}  # Get the first title encountered for each course_id
                }
            }
        ]

        # Execute the aggregation pipeline on the CoursesData collection
        cursor = courses_data_collection.aggregate(pipeline)

        # Iterate over the cursor and insert into CrossDump collection
        for doc in cursor:
            course_id = doc['_id']
            title = doc['title']

            # Insert document into CrossDump collection
            cross_dump_collection.update_many(
                {'id': course_id, 'title': {'$exists': False}},  # Match documents by course_id where title does not exist
                {'$set': {'title': title}},  # Set new title value
                upsert=False  # Do not insert a new document if no match is found
)
            print(f"added {title} for courseid {course_id}")
except Exception as ex:
        print(ex)
        sys.exit(1)
finally: 
        _put_connection(client)
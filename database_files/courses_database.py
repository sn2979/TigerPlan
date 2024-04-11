import sys
import os
import queue
from pymongo import MongoClient

#-----------------------------------------------------------------------
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
    client = _get_connection()
    db = client['TigerPlanData']
    courses_collection = db['CoursesData']
    print("Connected to MongoDB successfully!")
except Exception as e:
    print("Failed to connect to MongoDB:", e, file=sys.stderr)
    sys.exit(1)
finally:
    _put_connection(client)

def search_courses(search_query):
    # Define MongoDB query to search for courses
    query = {
        '$or': [
            {'subject': {'$regex': search_query, '$options': 'i'}},  # Case-insensitive regex match on subject
            {'catalog_number': {'$regex': search_query, '$options': 'i'}},  # Case-insensitive regex match on catalog_number
            {'title': {'$regex': search_query, '$options': 'i'}},  # Case-insensitive regex match on title
            {'subject': search_query[:3], 'catalog_number': search_query[3:]}  # Match combined subject+catalog_number (e.g., "COS126")
        ]
    }

    # Execute query and retrieve matching courses
    courses = list(courses_collection.find(query))

    # Dictionary to store unique courses and their cross-listings
    unique_courses_set = set()
    all_courses = []
    for course in courses:
        main_course = (course['subject'], course['catalog_number'])
        cross_listings = course.get('crosslistings', [])
        if main_course not in unique_courses_set:
            unique_courses_set.add(main_course)
            these_courses = []
            these_courses.append(main_course)
            for cross in cross_listings:
                cross_course = (cross['subject'], cross['catalog_number'])
                unique_courses_set.add(cross_course)  # Add cross-listed course
                these_courses.append(cross_course)
            all_courses.append(these_courses)
    # Convert dictionary values to list of lists

    return all_courses


# Example usage: Searching for courses matching a query
search_query = "ENV226"  # Example search query (can be any sequence of letters/numbers)
matching_courses = search_courses(search_query)
# Print matching courses
if matching_courses:
    print(f"Matching courses for query '{search_query}':")
    for course in matching_courses:
        print(course)
        # print(f"Subject: {course['subject']} | Catalog Number: {course['catalog_number']} | Title: {course['title']}")
else:
    print(f"No courses found for query '{search_query}'")

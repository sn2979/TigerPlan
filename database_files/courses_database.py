import sys
import os
import queue
from pymongo import MongoClient
import re

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
# Define a function to determine the sorting key
def sorting_key(course):
    # Extract the dept_num from the course dictionary
    dept_num = course['dept_num']
    
    # Regex pattern to match "Subject" or "Subject + ' ' + course_num"
    pattern = fr"{search_query}\s?\d*"

    # Check if the dept_num matches the regex pattern
    match = re.search(pattern, dept_num, re.IGNORECASE)
    
    # Return False if there is a match, so that matching items come first
    # Return True if there is no match, so that non-matching items come later
    return not bool(match)


def search_courses(search_query):
    if len(search_query) >= 3:
        try:
            # Get connection
            client = _get_connection()
            db = client['TigerPlanData']
            courses_collection = db['CoursesData']
            print("Connected to MongoDB successfully!")
            # Query database
            collation_options = {
                'locale': 'en',            # Specify locale (language)
                'strength': 1,             # Specify collation strength (1 for primary, i.e., case-insensitive)
                'caseLevel': False,        # Ignore case differences (case-insensitive)
                'numericOrdering': False,  # Treat numeric values as strings (e.g., "10" comes before "2")
                'alternate': 'shifted'  # Controls treatment of whitespace and punctuation
            }
            query = {
            '$or': [
                {'subject': search_query},  # Caseinsensitive regex match on subject
                {'subject': search_query[:3], 'catalog_number': {'$regex': f"^{search_query[3:]}", '$options': 'i'}}, # Match combined subject+catalog_number (e.g., "COS126")
                {'catalog_number': search_query},  # Case-insensitive sensitive match on catalog_number
                {'title':{'$regex': search_query, '$options': 'i'}}  # Case-insensitive regex match on title
            ]
        }
            projection = {
                'course_id': 1
            }

        # Execute the aggregation pipeline
            # Execute query and retrieve matching courses
            courses = courses_collection.find(query, projection=projection, collation=collation_options)
            course_ids_list = [course['course_id'] for course in courses]
            cross_courses_collection = db['CrossDump']
            # Prepare query to find documents with course_id in the provided list
            query = {'id': {'$in': course_ids_list}}
            # Execute query to find matching documents
            matching_courses = cross_courses_collection.find(query)
            all_courses = []
            for course in matching_courses:
                if course is not None:
                    all_courses.append({'dept_num': course['code'], 'title': course['title']})
            
        except Exception as e:
            print("Failed to connect to MongoDB:", e, file=sys.stderr)
            sys.exit(1)
        finally:
            _put_connection(client)
        all_courses.sort(key=sorting_key)
        return all_courses
    else:
        return None


# Example usage: Searching for courses matching a query
search_query = "spi"  # Example search query (can be any sequence of letters/numbers)
matching_courses = search_courses(search_query)
# Print matching courses
if matching_courses:
    print(f"Matching courses for query '{search_query}':")
    for course in matching_courses:
        print(course)
        # print(f"Subject: {course['subject']} | Catalog Number: {course['catalog_number']} | Title: {course['title']}")
else:
    print(matching_courses)
    print(f"No courses found for query '{search_query}'")

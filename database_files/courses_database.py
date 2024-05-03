import sys
import os
import queue
from pymongo import MongoClient
import re

#-----------------------------------------------------------------------
# _DATABASE_URL = os.environ.get('DATABASE_URL')
_DATABASE_URL = "mongodb+srv://tigerplan333:TigerPlan123!@tigerplandata.yyrhywn.mongodb.net/?retryWrites=true&w=majority&appName=TigerPlanData"
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
# Define a function to determine the sorting key
def sorting_key(course, search_query):
       # Extract the dept_num from the course dictionarys
    # print(search_query)
    dept_num = course['dept_num']
    # Remove extra spaces from the search query and escape special characters
    cleaned_search_query = re.sub(r'\s+', ' ', search_query.strip())
    escaped_search_query = re.escape(cleaned_search_query)
    # print(escaped_search_query)
    # Regex pattern to match "Subject" or "Subject + ' ' + course_num"
    pattern_startswith = fr"^{escaped_search_query}(\d*)\s*(.*)"
    pattern_contains = fr".*{escaped_search_query}.*"

    # Check if the dept_num matches the regex patterns
    match_startswith = re.search(pattern_startswith, dept_num, re.IGNORECASE)
    match_contains = re.search(pattern_contains, dept_num, re.IGNORECASE)
    
    if match_startswith:
        course_number = match_startswith.group(1)  # Extract course number
        course_suffix = match_startswith.group(2)  # Extract the rest after course number

        # Return a tuple to sort courses:
        # 0 - Courses that start with the search query
        # 0 - Priority for matches at the beginning of the dept_num
        # course_number (as int) - Sort by the course number (convert to integer)
        # course_suffix - Sort by the rest of the dept_num after course number
        return (0, 0, int(course_number) if course_number.isdigit() else 0, course_suffix)
    
    elif match_contains:
        # Return a tuple to sort courses:
        # 1 - Courses that contain the search query but do not start with it
        return (1, None, None, None)
    
    else:
        # Return a tuple to sort courses:
        # 2 - Courses that do not match the patterns
        return (2, None, None, None)

def search_courses(search_query):
    if len(search_query) == 0 or len(search_query) > 60:
        return None
    if re.match(r'^(?: )*$', search_query):
        return None
    try:
        # Get connection
        client = _get_connection()
        db = client['TigerPlanData']
        courses_collection = db['CrossDump']
        print("Connected to MongoDB successfully!")
        # Query database
        collation_options = {
            'locale': 'en',            # Specify locale (language)
            'strength': 1,             # Specify collation strength (1 for primary, i.e., case-insensitive)
            'caseLevel': False,        # Ignore case differences (case-insensitive)
            'numericOrdering': False,  # Treat numeric values as strings (e.g., "10" comes before "2")
            'alternate': 'shifted'  # Controls treatment of whitespace and punctuation
        }
        no_spaces_title = re.sub(r'\s+', ' ', search_query)
        no_spaces_dept_num = re.sub(r'\s+', '', search_query)
        escaped_no_spaces_dept_num = re.escape(no_spaces_dept_num)
        escaped_no_spaces_dept_num = "\s*".join(map(re.escape, escaped_no_spaces_dept_num))
        query = {
        '$or': [
            # {'subject': {'$regex': f"{escaped_query}", '$options': 'i'}},  # Caseinsensitive regex match on subject
            # {'subject': {'$regex': f"{escaped_query}", '$options': 'i'}}, # Match combined subject+catalog_number (e.g., "COS126")
            {'code': {'$regex': f"{escaped_no_spaces_dept_num}", '$options': 'i'}},  # Case-insensitive sensitive match on catalog_number
            {'title':{'$regex': re.escape(no_spaces_title), '$options': 'i'}}  # Case-insensitive regex match on title
        ]
    }
        # projection = {
        #     'course_id': 1
        # }
    # Execute the aggregation pipeline
        # Execute query and retrieve matching courses
        # courses = courses_collection.find(query, projection=projection, collation=collation_options)
        courses = courses_collection.find(query, collation=collation_options)

        # course_ids_list = [course['course_id'] for course in courses]
        # cross_courses_collection = db['CrossDump']
        # # Prepare query to find documents with course_id in the provided list
        # query = {'id': {'$in': course_ids_list}}
        # # Execute query to find matching documents
        # matching_courses = cross_courses_collection.find(query)
        # all_courses = []
        # for course in matching_courses:
        #     if course is not None:
        #         all_courses.append({'dept_num': course['code'], 'title': course['title']})
        all_courses = []
        for course in courses:
            if course is not None:
                # print(course)
                all_courses.append({'dept_num': course['code'], 'title': course['title']})
        
    except Exception as e:
        print("Failed to connect to MongoDB:", e, file=sys.stderr)
        sys.exit(1)
    finally:
        _put_connection(client)
    all_courses.sort(key=lambda course: sorting_key(course, search_query))
    return all_courses
    # else:
    #     return None


# Example usage: Searching for courses matching a query
# search_query = "soc"  # Example search query (can be any sequence of letters/numbers)
# matching_courses = search_courses(search_query)
# # Print matching courses
# if matching_courses:
#     print(f"Matching courses for query '{search_query}':")
#     for course in matching_courses:
#         print(course)
#         # print(f"Subject: {course['subject']} | Catalog Number: {course['catalog_number']} | Title: {course['title']}")
# else:
#     print(matching_courses)
#     print(f"No courses found for query '{search_query}'")

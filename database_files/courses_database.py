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
                'alternate': 'non-ignorable'  # Controls treatment of whitespace and punctuation
            }
            query = {
            '$or': [
                {'subject': search_query},  # Case-insensitive regex match on subject
                {'subject': search_query[:3], 'catalog_number': search_query[3:]}, # Match combined subject+catalog_number (e.g., "COS126")
                {'catalog_number': search_query},  # Case-insensitive regex match on catalog_number
                {'title':{'$regex': search_query, '$options': 'i'}}  # Case-insensitive regex match on title
            ]
        }
            projection = {
                'course_id': 1,
                'title': 1
            }

        # Aggregate pipeline to add priority field and sort results
            pipeline = [
                {'$match': query},  # Match documents based on the search query
                {'$addFields': {
                    'priority': {
                        '$switch': {
                            'branches': [
                                {'case': {'$eq': ['$subject', search_query]}, 'then': 1},
                                {'case': {'$eq': ['$subject', search_query[:3]]}, 'then': 2},
                                {'case': {'$eq': ['$catalog_number', search_query]}, 'then': 3},
                                {'case': {'$regexMatch': {'input': '$title', 'regex': search_query, 'options': 'i'}}, 'then': 4}
                            ],
                            'default': 0  # Default priority (should not happen)
                        }
                    }
                }},
                {'$sort': {'priority': 1}}  # Sort results by priority in ascending order
            ]

        # Execute the aggregation pipeline
            # Execute query and retrieve matching courses
            courses = courses_collection.aggregate(pipeline, collation=collation_options, allowDiskUse=True)
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
            # Dictionary to store unique courses and their cross-listings
            # unique_courseids_set = set()
            # for course in courses[:50]:
            #     courseid = course['course_id']
            #     # if courseid not in unique_courseids_set:
            #     #     unique_courseids_set.add(courseid)
            #     # these_courses = []
            #     cross_courses_collection = db['CrossDump']
            #     query = {'id': courseid}
            #     cross_course = cross_courses_collection.find_one(query)
            #     # if cross_course and cross_course is not None:
            #     #     these_courses.append(cross_course[0]['code'])
            #     #     for code in cross_course[0]['cross']:
            #     #         these_courses.append(code)
            #     #     result_string = ' / '.join(these_courses)
            #     #     title = course['title']
            #     if cross_course is not None:
            #         all_courses.append({'dept_num': cross_course['code'], 'title': course['title']})
        except Exception as e:
            print("Failed to connect to MongoDB:", e, file=sys.stderr)
            sys.exit(1)
        finally:
            _put_connection(client)
        return all_courses
    else:
        return None


# Example usage: Searching for courses matching a query
search_query = "COS"  # Example search query (can be any sequence of letters/numbers)
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

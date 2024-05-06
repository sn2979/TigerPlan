'''
File that adds all new courses both into the CoursesData databse
and into the CrossDump database
'''
import sys
import os
import queue
from pymongo import MongoClient
from req_lib import ReqLib

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

def get_all_subjects():
    subjects = ["AAS", "AFS", "AMS", "ANT", "AOS", "APC", "ARA", "ARC", 
             "ART", "ASA", "ASL", "AST", "ATL", "BCS", "BNG", "CBE", 
             "CDH", "CEE", "CGS", "CHI", "CHM", "CHV", "CLA", "CLG", 
             "COM", "COS", "CTL", "CWR", "DAN", "EAS", "ECE", "ECO", 
             "EAS", "ECE", "ECO", "ECS", "EEB", "EGR", "ENE", "ENG", 
             "ENT", "ENV", "EPS", "FIN", "FRE", "FRS", 
             "GEO", "GER", "GEZ", 
             "GHP", "GSS", "HEB", "HIN", "HIS", "HLS", "HOS", "HUM", 
             "ITA", "JDS", "JPN", "JRN", "KOR", "LAO", "LAS", "LAT", 
             "LCA", "LIN", "MAE", "MAT", "MED", "MOD", "MOG", "MOL", 
             "MPP", "MSE", "MTD", "MUS", "NES", "NEU", "ORF", "PAW", 
             "PER", "PHI", "PHY", "PLS", "POL", "POP", "POR", "PSY", 
             "QCB", "QSE", "REL", "RES", "RUS", "SAN", "SAS", "SLA", 
             "SML", "SOC", "SPA", "SPI", "STC", "SWA", "THR", "TPP", 
             "TRA", "TUR", "TWI", "UKR", "URB", "URD", "VIS", "WRI"]
    return subjects

def get_term_info_for_subject(term, subj):
    term_info = req_lib.getJSON(
        req_lib.configs.COURSE_COURSES,
        # To return a json version of the return value
        fmt="json",
        term=term, 
        subject=subj,
    )
    return term_info

def get_courses_json_list(term_info, subj):
    courses = []
    if term_info is not None:
        if term_info["term"] is not None:
            for term in term_info["term"]:
                if term['code'] is not None:
                    for subject in term["subjects"]:
                        subject_name = subject['code']
                        for course in subject["courses"]:
                            extracted_data = {
                            "term_code": term['code'],
                            "subject": subject_name,
                            "guid": course["guid"],
                            "course_id": course["course_id"],
                            "catalog_number": course["catalog_number"],
                            "title": course["title"],
                            "crosslistings": course['crosslistings']
                            }   
                            courses.append(extracted_data)
                    return courses
                else: 
                    return None
        else:
            return None
    else:
        return None
    
def input_all_items_into_db(data):
    try: 
        client = _get_connection()
        print("Connecting to database")
        db = client['TigerPlanData']
        collection = db['CoursesData']
        print(f"Connected to collection")
        collection.insert_many(data)

    except Exception as ex: 
        print("failed to insert items into database")
        print(ex, file=sys.stderr)
        sys.exit(1)
    finally:
        _put_connection(client)
    
if __name__ == "__main__":
    req_lib = ReqLib()

    subjs = get_all_subjects()
    new_term = 1252
    all_jsons = []
    new_courseids = set()
    client = _get_connection()
    db = client['TigerPlanData']
    for subj in subjs:
        print(f"Adding {subj} courses for term {new_term}")
        term_info = get_term_info_for_subject(new_term, subj)
        courses_json_list = get_courses_json_list(term_info, subj)
            # print(courses_json_list)
        if courses_json_list is not None:
            for course in courses_json_list:
                matching_course = list(db['CoursesData'].find({"subject": course['subject'], 
                                                              "catalog_number": course['catalog_number'],
                                                              "course_id": course['course_id']}))
                if len(matching_course) == 0:
                    new_courseids.add(course['course_id'])
                    print(f"added new courseid {course['course_id']}" )
                    all_jsons.append(course)
                else:
                    print(f"No new courses for {subj} in term {new_term}")
        else:
            print(f"No courses in {subj} in term {new_term}")
    input_all_items_into_db(all_jsons)

    # new_term = "1252"
    new_courseids = [course['course_id'] for course in list(db['CoursesData'].find({"term_code": new_term})) ]
    print(new_courseids)
    for new_courseid in new_courseids:
        matching_course_in_crossDump = list(db['CrossDump'].find({"id": new_courseid}))
        if len(matching_course_in_crossDump) == 0:
            matching_course_in_coursesData = db['CoursesData'].find_one({"course_id": new_courseid})
                # title = ""
            code = f"{matching_course_in_coursesData['subject']}" + ' ' + f"{matching_course_in_coursesData['catalog_number']}"            
            cross_lists = []
            for cross in matching_course_in_coursesData['crosslistings']:
                code += f" / {cross['subject']}" + " " + f"{cross['catalog_number']}"
            
            title = matching_course_in_coursesData['title']
            term = int(matching_course_in_coursesData['term_code'])
            db['CrossDump'].insert_one({'code': code, 'id': new_courseid, 'term': term, 'title': title})    
            print("added ", {'code': code, 'id': new_courseid, 'term': term, 'title': title})



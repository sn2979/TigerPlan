# 'Fall 2024': '1252',
# 'Fall 2023': '1242',
# 'Fall 2022': '1232',
# 'Fall 2021': '1222',
# 'Fall 2020': '1212',
# 'Spring 2024': '1244',
# 'Spring 2023': '1234',
# 'Spring 2022': '1224',
# 'Spring 2021': '1214'

#!/usr/bin/env python3
import sys
from pymongo import MongoClient
from req_lib import ReqLib
import json

def get_all_terms():
    terms = [1214, 1224, 1234, 1244, 1212, 1222, 1232, 1242, 1252]
    return terms

def get_all_subjects():
    subjects = ["AAS", "AFS", "AMS", "ANT", "AOS", "APC", "ARA", "ARC", 
             "ART", "ASA", "ASL", "AST", "ATL", "BCS", "BNG", "CBE", 
             "CDH", "CEE", "CGS", "CHI", "CHM", "CHV", "CLA", "CLG", 
             "COM", "COS", "CTL", "CWR", "DAN", "EAS", "ECE", "ECO", 
             "EAS", "ECE", "ECO", "ECS", "EEB", "EGR", "ENE", "ENG", 
             "ENT", "ENV", "EPS", "FIN", "FRE", "GEO", "GER", "GEZ", 
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
                        for course in subject["courses"]:
                            extracted_data = {
                            "term_code": term['code'],
                            "subject": subj,
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
        with MongoClient('mongodb+srv://tigerplan333:TigerPlan123!@tigerplandata.yyrhywn.mongodb.net/') as client:
            print("Connecting to database")
            db = client['TigerPlanData']
            collection = db['CoursesData']
            print(f"Connected to collection")
            collection.insert_many(data)
    except Exception as ex: 
        print("blah")
        print(ex, file=sys.stderr)
        sys.exit(1)

def input_term_subj_into_db(data):
    try: 
        with MongoClient('mongodb+srv://tigerplan333:TigerPlan123!@tigerplandata.yyrhywn.mongodb.net/') as client:
            print("Connecting to database")
            db = client['TigerPlanData']
            collection = db['CoursesData']
            print(f"Connected to collection")
            for item in data:
            # Check if a document with the same catalog_number exists for the dept_name
                existing_doc = collection.find_one({"subject": item["subject"], "catalog_number": item["catalog_number"]})
                if existing_doc is None:
            # Insert the document if it doesn't exist
                    collection.insert_one(item)
                else:
                    print(f"Document with catalog_number {item['catalog_number']} already exists for subject {item['subject']}")
    except Exception as ex: 
        print("blah")
        print(ex, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    req_lib = ReqLib()

    subjs = get_all_subjects()
    terms = get_all_terms()
    all_jsons = []
    for subj in subjs:
        for term in terms:
            print(f"Adding {subj} courses for term {term}")
            term_info = get_term_info_for_subject(term, subj)
            courses_json_list = get_courses_json_list(term_info, subj)
                # print(courses_json_list)
            if courses_json_list is not None:
                for course in courses_json_list:
                    all_jsons.append(course)
            else:
                print(f"No courses in {subj} in term {term}")
    input_all_items_into_db(all_jsons)
    # subj = "COS"
    # term = 1214
    # term_info = get_term_info_for_subject(term, subj)
    # if term_info is not None:
    #     courses_json_list = get_courses_json_list(term_info)
    #     if courses_json_list is not None:
    #         print(courses_json_list)
    #         # input_term_subj_into_db(courses_json_list)
    #     else: 
    #         print(f"No courses in {subj} in term {term}")

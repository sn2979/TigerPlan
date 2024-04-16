import sys
import os
import queue
from pymongo import MongoClient, DESCENDING

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
try:
    client = _get_connection()
    db = client['TigerPlanData']
    students_collection = db['StudentsData']
    print("Connected to MongoDB successfully!")
except Exception as e:
    print("Failed to connect to MongoDB:", e, file=sys.stderr)
    sys.exit(1)
finally:
    _put_connection(client)

# Function to handle student login
def handle_student_login(username):
    try:
        # Check if student exists in the database
        first_time = False
        existing_student = students_collection.find_one({"netID": username})
        print(existing_student)
        print("find one worked!")

        if existing_student is None:
            first_time = True
            print("Student doesn't exist!")
             # If student doesn't exist, create a new student document
            new_student = {
                "netID": username,
                "Name": "",
                "Major": "",
                "Classes": [],
                "Recommendations": []
            }   
            students_collection.insert_one(new_student)
            #print("insert one worked!")
        return (True, first_time)
    except Exception as e:
        print("An error occurred while handling student login:", e)
        return (False, False)

# Function to update student profile
def update_student_profile(username, name, major):
    try:
        existing_student = students_collection.find_one({"netID": username})
        if existing_student is None:
            raise Exception("Student not found")
        students_collection.update_one({"netID": username}, {"$set": {"Name": name, "Major": major}})
        return True
    except Exception as e:
        print("An error occurred while updating student profile:", e)
        return False
    
# Function to get student classes
def get_student_classes(username):
    try:
        existing_student = students_collection.find_one({"netID": username})
        if existing_student is None:
            raise Exception("Student not found")
        return existing_student.get("Classes", [])
    except Exception as e:
        print("An error occurred while getting student classes:", e)
        return []

def get_student_name(username):
    try:
        existing_student = students_collection.find_one({"netID": username})
        if existing_student is None:
            raise Exception("Student not found")
        return existing_student.get("Name", "")
    except Exception as e:
        print("An error occurred while getting student name:", e)
        return ""

def get_student_major(username):
    try:
        existing_student = students_collection.find_one({"netID": username})
        if existing_student is None:
            raise Exception("Student not found")
        return existing_student.get("Major", "")
    except Exception as e:
        print("An error occurred while getting student major:", e)
        return ""
    
# deprecated version
'''def update_student_classes(username, classes):
    try:
        existing_student = students_collection.find_one({"netID": username})
        if existing_student is None:
            raise Exception("Student not found")
        students_collection.update_one({"netID": username}, {"$set": {"Classes": classes}})
        return True
    except Exception as e:
        print("An error occurred while updating student classes:", e)
        return False'''

# Function to update student classes
def update_student_classes(username, classes_to_add=None, classes_to_remove=None):
    print(classes_to_remove)
    try:
        existing_student = students_collection.find_one({"netID": username})
        if existing_student is None:
            raise Exception("Student not found")
        
        update_query = {}
        
        if classes_to_add:
            update_query["$addToSet"] = {"Classes": {"$each": classes_to_add}}
        
        if classes_to_remove:
            update_query["$pull"] = {"Classes": {"id": {"$in": classes_to_remove}}}
            print(f"Removed classes with IDs: {classes_to_remove}")
        
        if update_query:
            students_collection.update_one({"netID": username}, update_query)
            print("updated classes")
            print(get_student_classes(username))
        
        return True
    except Exception as e:
        print("An error occurred while updating student classes:", e)
        return False

def get_student_coursenums(username):
    try:
        # Get a MongoDB connection
        client = _get_connection()
        db = client['TigerPlanData']
        students_collection = db['StudentsData']

        # Aggregation pipeline to retrieve course numbers for the specified student
        pipeline = [
            # Match the document for the specified student by netID
            {"$match": {"netID": username}},
            # Unwind the classes array to deconstruct the array into separate documents
            {"$unwind": "$Classes"},
            # Project to include only the coursenum field from each class object
            {"$project": {"_id": 0, "coursenum": "$Classes.coursenum"}}
        ]

        # Execute the aggregation pipeline
        result = list(students_collection.aggregate(pipeline))

        # Extract the list of coursenum values
        coursenum_list = [entry['coursenum'] for entry in result]

        return coursenum_list
    except Exception as e:
        print("An error occurred while getting student course numbers:", e)
        return []
    

# Example usage
def main():
    try:
        # Assuming username is retrieved after successful login
        # create a loop of usernames
        '''for i in range(1, 10):
            username = "student" + str(i)
            worked,_ = handle_student_login(username)
            if worked:
                print("Student login successful!")
                student_classes = get_student_classes(username)
                print("Classes for student:", student_classes)
            else:
                print("Student login failed!")
        # Update student classes
        update_student_classes("student2", ["COS 333", "COS 226", "COS 217"])
        student_classes = get_student_classes("student2")
        print("Updated classes for student:", student_classes)

        # Update student classes by removing some classes
        update_student_classes("student2", classes_to_remove=["COS 333"])
        student_classes = get_student_classes("student2")
        print("Updated classes for student:", student_classes)

        # Update student classes by adding some classes
        update_student_classes("student2", classes_to_add=["COS 333"])
        student_classes = get_student_classes("student2")
        print("Updated classes for student:", student_classes)'''
        username = "sn2979"
        # Get the list of coursenum values for the specified student
        student_coursenums = get_student_coursenums(username)
        print("Coursenums for student:", student_coursenums)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

import sys
from pymongo import MongoClient

try:
    client = MongoClient('mongodb+srv://tigerplan333:TigerPlan123!@tigerplandata.yyrhywn.mongodb.net/?retryWrites=true&w=majority&appName=TigerPlanData')
    db = client['TigerPlanData']
    students_collection = db['StudentsData']
    print("Connected to MongoDB successfully!")
except Exception as e:
    print("Failed to connect to MongoDB:", e, file=sys.stderr)
    sys.exit(1)

# Function to handle student login
def handle_student_login(username, name, major):
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
                "Name": name,
                "Major": major,
                "Classes": ["COS 333 <3 "],
                "Recommendations": []
            }   
            students_collection.insert_one(new_student)
            #print("insert one worked!")
        return (True, first_time)
    except Exception as e:
        print("An error occurred while handling student login:", e)
        return (False, False)

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
    
# Function to update student classes
def update_student_classes(username, classes):
    try:
        existing_student = students_collection.find_one({"netID": username})
        if existing_student is None:
            raise Exception("Student not found")
        students_collection.update_one({"netID": username}, {"$set": {"Classes": classes}})
        return True
    except Exception as e:
        print("An error occurred while updating student classes:", e)
        return False

# Example usage
def main():
    try:
        # Assuming username is retrieved after successful login
        # create a loop of usernames
        for i in range(1, 10):
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
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

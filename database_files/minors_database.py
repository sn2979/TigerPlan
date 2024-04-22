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
    minors_collection = db['MinorsData']
    print("Connected to MongoDB successfully!")
except Exception as e:
    print("Failed to connect to MongoDB:", e, file=sys.stderr)
    sys.exit(1)
finally:
    _put_connection(client)

# Function to get minor description
def get_desc(minorId):
    try:
        minor = minors_collection.find_one({"code": minorId})
        if minor is None:
            raise Exception("Minor not found")
        return minor.get("description", "")
    except Exception as e:
        print("An error occurred while getting minor description:", e)
        return ""

#Function to get minor URLs
def get_urls(minorId):
    try:
        minor = minors_collection.find_one({"code": minorId})
        if minor is None:
            raise Exception("Minor not found")
        return minor.get("urls", [])
    except Exception as e:
        print("An error occurred while getting minor description:", e)
        return []

#Function to get minor code
def get_code_from_name(name):
    try:
        print(name)
        minor = minors_collection.find_one({"name": name})
        if minor is None:
            raise Exception("Minor not found")
        return minor.get("code", "")
    except Exception as e:
        print("An error occurred while getting minor code:", e)
        return ""

#Function to get minor name
def get_name_from_code(code):
    try:
        print(code)
        minor = minors_collection.find_one({"code": code})
        if minor is None:
            raise Exception("Minor not found")
        return minor.get("name", "")
    except Exception as e:
        print("An error occurred while getting minor name:", e)
        return ""


# Example usage
def main():
    try:
        minorID = "COS"
        desc = get_desc(minorID)
        print(desc)
        
        name = get_name_from_code(minorID)
        id = get_code_from_name(name)

        print(name)
        print(id)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

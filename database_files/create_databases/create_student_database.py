# Consulted with ChatGPT: 
import os
import sys
from pymongo import MongoClient

try: 
    with MongoClient('mongodb+srv://tigerplan333:TigerPlan123!@tigerplandata.yyrhywn.mongodb.net/') as client:
        db = client['TigerPlanData']
        collection = db['StudentsData']
        print("Connected to MongoDB successfully!")
        collection.create_index("netID", unique=True)
        collection.create_index("Name")
        collection.create_index("Major")
        collection.create_index("Classes")
        collection.create_index("Recommendations")
        print("Created indices successfully!")
except Exception as ex: 
    print(ex, file=sys.stderr)
    sys.exit(1)

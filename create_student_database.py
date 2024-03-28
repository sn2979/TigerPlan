# Consulted with ChatGPT: 
import os
import sys
from pymongo import MongoClient

try: 
    with MongoClient('mongodb+srv://tigerplan333:TigerPlan123!@tigerplandata.yyrhywn.mongodb.net/') as client:
        db = client['TigerPlanData']
        db.create_collection('StudentsData')
    
except Exception as ex: 
    print(ex, file=sys.stderr)
    sys.exit(1)


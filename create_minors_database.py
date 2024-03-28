# Consulted with ChatGPT: 
import os
import sys
import yaml
from pymongo import MongoClient

# Parse YAML file
files = os.listdir('/Users/joshforworking/GitHub Projects/TigerPlan/minors')
data = []
for file in files:
    with open(f'/Users/joshforworking/GitHub Projects/TigerPlan/minors/{file}', 'r') as yaml_file:
        file_data = yaml.safe_load(yaml_file)
        data.append(file_data)

try: 
    with MongoClient('mongodb+srv://tigerplan333:TigerPlan123!@tigerplandata.yyrhywn.mongodb.net/') as client:
        db = client['TigerPlanData']
        collection = db['MinorsData']
        collection.insert_many(data)
except Exception as ex: 
    print(ex, file=sys.stderr)
    sys.exit(1)

# try:
#     # Connect to MongoDB
#         client = MongoClient('mongodb+srv://tigerplan333:TigerPlan123!@tigerplandata.jighe76.mongodb.net/?retryWrites=true&w=majority&appName=TigerPlanData')
#         db = client['TigerPlanData']
#         print("Successfully connected to MongoDB!")
        
#         # You can perform operations with the database here
#         # For example, you could create a collection:
#         # db.create_collection('MinorsData')
#         collection = db['MinorsData']
#         print("Collection created!")
#         print("Accessed collection")
#         collection.insert_many(data)
#         print("Inserted data into collection")
# except Exception as ex:
#     print(f"An error occurred: {ex}")
# finally:
#     # Close the MongoDB connection
#     client.close()
#     print("MongoDB connection closed.")
# #s Transform and insert data into MongoDB



# #In this example, replace 'data.yaml' with the path to your YAML file, 
# # 'mongodb://localhost:27017/' with the connection string for your 
# # MongoDB instance, 'mydatabase' with the name of your MongoDB database, 
# #and 'mycollection' with the name of the collection where you want to 
# # insert the data.

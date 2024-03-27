# Consulted with ChatGPT: 
import os
import yaml
from pymongo import MongoClient

# Parse YAML file
files = os.listdir('/Users/joshforworking/Downloads/minors')
data = []
for file in files:
    with open(f'/Users/joshforworking/Downloads/minors/{file}', 'r') as yaml_file:
        file_data = yaml.safe_load(yaml_file)
        data.append(file_data)

# Connect to MongoDB
client = MongoClient('mongodb+srv://jschoenberg:TigerPlan123!@tigerplantest1.lmveo2u.mongodb.net/?retryWrites=true&w=majority&appName=TigerPlanTest1')
db = client['TigerPlanTest1']

#s Transform and insert data into MongoDB
# db.create_collection('TestDB1AFS')
collection = db['MinorsData']
print(data)

collection.insert_many(data)

#In this example, replace 'data.yaml' with the path to your YAML file, 
# 'mongodb://localhost:27017/' with the connection string for your 
# MongoDB instance, 'mydatabase' with the name of your MongoDB database, 
#and 'mycollection' with the name of the collection where you want to 
# insert the data.

# Consulted with ChatGPT: 
import os
from pymongo import MongoClient

# Connect to MongoDB
try:
    client = MongoClient('mongodb+srv://jschoenberg:TigerPlan123!@tigerplantest1.lmveo2u.mongodb.net/?retryWrites=true&w=majority&appName=TigerPlanTest1')
    db = client['TigerPlanTest1']
except Exception as ex:
    print("Connection unsuccessful")
    
#s Transform and insert data into MongoDB
# db.create_collection('TestDB1AFS')
db.create_collection('StudentsData')

#In this example, replace 'data.yaml' with the path to your YAML file, 
# 'mongodb://localhost:27017/' with the connection string for your 
# MongoDB instance, 'mydatabase' with the name of your MongoDB database, 
#and 'mycollection' with the name of the collection where you want to 
# insert the data.

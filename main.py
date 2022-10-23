#!/usr/bin/python3

import sys
from pymongo import MongoClient


def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb://testuser:testpass@pi/test"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['test']


if __name__ == '__main__':
    
    c = get_database()
    print("database connected")
    collection_name = c["docs"]
    print("collection opened")
    item_details = collection_name.find()
    for item in item_details:
        # This does not give a very readable output
        print(item)

#!/usr/bin/python3

import sys
from pymongo import MongoClient


def get_database():
   CONNECTION_STRING = "mongodb://testuser:testpass@pi/test"
   client = MongoClient(CONNECTION_STRING)
   return client['test']


if __name__ == '__main__':
    
    c = get_database()
    print("database connected")
    collection_name = c["docs"]
    print("collection opened")
    item_details = collection_name.find()
    for item in item_details:
        print(item)

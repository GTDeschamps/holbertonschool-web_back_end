#!/usr/bin/env python3
"""Write a Python script that provides some stats
about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


if __name__ == "__main__":

    client = MongoClient('localhost', 27017)
    collection = client.logs.nginx

    total_log = collection.count_documents({})

    print("{} logs".format(total_log))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method" : method})
        print("\tmethod {}: {}".format(method, count))

    statut = collection.count_documents({"method" : "GET", "path": "/status"})
    print("{} status check".format(statut))

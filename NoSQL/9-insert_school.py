#!/usr/bin/env python3
"""Write a Python function that inserts a new document in a collection
based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    inserted_id = mongo_collection.insert_one(kwargs).inserted_id
    return inserted_id

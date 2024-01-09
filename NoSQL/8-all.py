#!/usr/bin/env python3
"""Write a Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """Method to list all documents in mongo_collection"""

    all_documents = []

    if mongo_collection.find():
        for documents in mongo_collection.find():
            all_documents.append(documents)

    return all_documents

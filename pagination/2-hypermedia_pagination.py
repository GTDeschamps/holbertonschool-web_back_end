#!/usr/bin/env python3
"""Implement a get_hyper method that takes the same arguments
as get_page and returns a dictionary
containing the following key-value pairs"""


import csv
import math
from typing import List

Server = __import__('1-simple_pagination').Server


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    assert isinstance(page, int) and page > 0
    "Page number must be an integer greater than 0"
    assert isinstance(page_size, int) and page_size > 0
    "Page size must be an integer greater than 0"

    data = []
    with open('Popular_Baby_Names.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        dataset = list(reader)

        start_index, end_index = index_range(page, page_size)
        if start_index >= len(dataset):
            return []
        elif end_index >= len(dataset):
            return dataset[start_index:]
        else:
            return dataset[start_index:end_index + 1]


def get_hyper(page=1, page_size=10):
    page_data = get_page(page, page_size)
    total_pages = math.ceil(len(page_data) / page_size)

    hyper_dict = {
        "page_size": len(page_data),
        "page": page,
        "data": page_data,
        "next_page": page + 1 if len(page_data) == page_size else None,
        "prev_page": page - 1 if page > 1 else None,
        "total_pages": total_pages
    }

    return hyper_dict

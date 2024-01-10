#!/usr/bin/env python3
"""Implement a method named get_page that takes two integer arguments page
with default value 1 and page_size with default value 10."""


import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

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

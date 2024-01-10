#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict[str, Union[int, List]]:
        assert index is None or (isinstance(index, int) and index >= 0)
        "Index must be a positive integer or None"
        assert isinstance(page_size, int) and page_size > 0
        "Page size must be an integer greater than 0"

        dataset = self.dataset()
        total_rows = len(dataset)

        if index is None:
            index = 0
        elif index >= total_rows:
            return {}

        start_index = index
        end_index = min(start_index + page_size - 1, total_rows - 1)

        if start_index >= total_rows:
            return {}
        else:
            return {
                "index": start_index,
                "next_index": end_index + 1
                if end_index < total_rows - 1 else None,
                "page_size": page_size,
                "data": dataset[start_index:end_index + 1]
            }

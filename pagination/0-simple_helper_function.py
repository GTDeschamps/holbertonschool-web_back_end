#!/usr/bin/env python3
"""
Write a function namedindex_range that takes two integer arguments:
page and page_size.
"""


import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """
    function index_range
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index

#!/usr/bin/env python3
"""module on pagination"""


def index_range(page, page_size):
    """a function that return a tuple of size
       two containing a start index and an end index """
    start_index = page_size * (page - 1)
    end_index = page * page_size
    return (start_index, end_index)

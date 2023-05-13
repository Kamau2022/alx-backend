#!/usr/bin/env python3
"""module on pagination"""

import csv
import math
from typing import List, Tuple


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """a function that return a tuple of size
           two containing a start index and an end index
        """
        start_index = page_size * (page - 1)
        end_index = page * page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """that takes two integer arguments page with default
           value 1 and page_size with default value 10.
        """
        index = self.index_range(page, page_size)
        value = self.dataset()
        items = []
        """assert type(page_size) is int and type(page) is int"""
        assert type(page_size) is int and page_size > 0
        assert type(page) is int and page > 0
        try:
            for x in range(index[0], index[1]):
                items.append(value[x])
            return items
        except IndexError:
            return []

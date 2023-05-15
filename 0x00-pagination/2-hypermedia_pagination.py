#!/usr/bin/env python3
"""
Module 1-simple_pagination
"""

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

        start_index = end_index - page_size
        return (start_index, end_index)

    def index_range(self, page: int, page_size: int) -> Tuple:
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
        assert type(page_size) is int and type(page) is int
        assert type(page_size) is int and page_size > 0
        assert type(page) is int and page > 0
        index = self.index_range(page, page_size)
        value = self.dataset()
        items = []
        try:
            for x in range(index[0], index[1]):
                items.append(value[x])
            return items
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Parameters
        ---------
        page: int
            the start of pagination
        page_size: int
            the maximum number of object returned

        Returns
        -------
        dict
            the appropriate page of the dataset or the correct list of row
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)
        new_dict = {"page_size": len(data) if page_size >= len(data)
                    else page_size,
                    "page": page,
                    "data": data,
                    "next_page": page + 1 if page + 1 <= total_pages else None,
                    "prev_page": page - 1 if page > 1 else None,
                    "total_pages": total_pages}
        return new_dict

#!/usr/bin/env python3
"""a module on catching
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """a class that inherits from BaseCaching class
    """
    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def put(self, key, item):
        """a function that assign to the dictionary self.cache_data
           the item value for the key
        """
        self.cache_data[key] = item
        return self.cache_data

    def get(self, key):
        """a function that return the value in self.cache_data
           linked to key
        """
        try:
            list_1 = self.cache_data[key]
            return list_1
        except KeyError:
            return None

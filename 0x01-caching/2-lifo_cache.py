#!/usr/bin/python3
"""a module on caching
"""
from collections import OrderedDict
BaseCaching = __import__('0-basic_cache').BaseCaching


class LIFOCache(BaseCaching):
    """a class that inherits from BaseCaching
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the
           item value for the key key
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-1]
                self.cache_data.pop(last_key)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """a function that return the value in self.cache_data
           linked to key
        """
        try:
            list_1 = self.cache_data[key]
            return list_1
        except KeyError:
            return None

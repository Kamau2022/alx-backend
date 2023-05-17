#!/usr/bin/python3
"""a module on caching
"""
BaseCaching = __import__('0-basic_cache').BaseCaching


class FIFOCache(BaseCaching):
    """a class that inherits from BaseCaching
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """assign to the dictionary self.cache_data the
           item value for the key key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        length = len(self.cache_data)
        first_key = list(self.cache_data.keys())[0]
        if length > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(first_key)
            print('DISCARD: {}'.format(first_key))
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

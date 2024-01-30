#!/usr/bin/env python3
""" Basic Cache """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCahcing and is a caching system
    """

    def __init__(self):
        """ Initializes BasicCache"""
        super().__init__()

    def put(self, key, item):
        """ Adds an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Gets an item by key """
        if key is not None or key not in self.cache_data:
            return self.cache_data[key]

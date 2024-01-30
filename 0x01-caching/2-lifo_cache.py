#!/usr/bin/env python3
""" LIFO Caching """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and is a caching system """
    def __init__(self):
        """ Initializes LIFOCache """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.stack.remove(key)
                else:
                    del self.cache_data[self.stack[BaseCaching.MAX_ITEMS - 1]]
                    discarded_key = self.stack.pop()
                    print(f"DISCARD: {discarded_key}")

            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """ Gets an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

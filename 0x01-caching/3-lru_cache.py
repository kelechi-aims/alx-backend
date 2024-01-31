#!/usr/bin/env python3
"""
LRU Caching
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
     class LRUCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Init method
        """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    self.key_order.remove(key)
                else:
                    lru_key = self.key_order.pop(0)
                    del self.cache_data[lru_key]
                    print("DISCARD:", lru_key)

            self.cache_data[key] = item
            self.key_order.append(key)

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        """
        if key in self.cache_data:
            self.key_order.remove(key)
            self.key_order.append(key)
            return self.cache_data[key]
        return None

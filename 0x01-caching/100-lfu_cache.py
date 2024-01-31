#!/usr/bin/env python3
""" LFU Caching """

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and is a caching system """

    def __init__(self):
        """ Initializes LFUCache """
        super().__init__()
        self.frequency_counter = defaultdict(int)

    def put(self, key, item):
        """ Add data to cache """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data[key] = item
                    self.frequency_counter[key] += 1
                    return
                # Find the item with the least frequency
                min_frequency = min(self.frequency_counter.values())
                discarded_key = [
                    k for k, v in self.frequency_counter.items()
                    if v == min_frequency]

                # if there's more than one item with the least
                # frequency, use LRU to discard the least recently used
                if len(discarded_key) > 1:
                    item_discarded = discarded_key[0]
                else:
                    item_discarded = discarded_key[0]
                del self.cache_data[item_discarded]
                print(f"DISCARD: {item_discarded}")
                del self.frequency_counter[item_discarded]

            # Add or update the item in the cache_data
            self.cache_data[key] = item
            # Increment the frequency counter for the key
            self.frequency_counter[key] += 1

    def get(self, key):
        """ Get a data from cache """
        if key in self.cache_data:
            # Increment the frequency counter for the accesses key
            self.frequency_counter[key] += 1
            return self.cache_data[key]
        return None

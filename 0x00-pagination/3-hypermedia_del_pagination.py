#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve hypermedia metadata for a page of data from the dataset.

        Args:
            page (int, optiona): The start index of the returned page.
            Default to None.
            page_size (int, optional): The number of items per page.
            Defualt to 10.

        Returns:
            Dict: A dictionary containing hypermedia metadata for
            the requested page
        """
        assert index is None or isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size >= 0

        dataset = self.indexed_dataset()
        if index is None:
            index = 0
        else:
            assert index < len(dataset)
        data = []
        next_index = index
        for i in range(page_size):
            if next_index not in dataset:
                next_index += 1
            data.append(dataset[next_index])
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }

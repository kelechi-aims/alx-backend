#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calulate the start and end indexes for pagination

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page

    Returns:
        tuple[int, int]: A tuple contaoining the start and end indexes.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of data from the dataset

        Args:
            page (int, optiona): The page number (1-indexed).
            page_size (int, optional): The number of items per page

        Returns:
            List[List]: A list containing the rows corresponding
            to the requested page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        if start_index >= len(dataset):
            return []
        end_index = min(end_index, len(dataset))
        return dataset[start_index:end_index]

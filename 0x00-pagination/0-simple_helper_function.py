#!/usr/bin/env python3
""" Simple helper function that calculates the start and
end indexes for pagination
"""
from typing import Tuple


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

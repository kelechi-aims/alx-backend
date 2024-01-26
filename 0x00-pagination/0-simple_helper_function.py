#!/usr/bin/python3
""" Simple helper function that calculates the start and end indexes for pagination
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calulate the start and end tindexes for pagination

    Args:
        page (int): The page numberT (i-indexed).
        page_size (int): The number of items per page

    Returns:
        tuple[int, int]: A tuple contaoining the start and end indexes.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index   

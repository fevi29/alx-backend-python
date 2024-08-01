#!/usr/bin/env python3
"""
It provides a function for returning the first element
    of a list, or None if the list is empty.
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Args:
        lst (Sequence object)
    Returns
        The value of the first element in lst of None if list is empty
    """
    if lst:
        return lst[0]
    else:
        return None

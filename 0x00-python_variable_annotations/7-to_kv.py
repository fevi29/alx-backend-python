#!/usr/bin/env python3
"""
It provides a function for creating a tuple with a string
    and the square of an int or float as a float.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
        k (str)
        v (int or float)
    Return:
        (tuple): a tuple of k and square of v
    """
    return k, v*v

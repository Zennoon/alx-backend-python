#!/usr/bin/env python3
"""
Contains:
    Function
    ========
    to_kv - accepts a string and an int or float and retuns a tuple
    containing the string, and the square of the int or float
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Accepts a string and an int or float and retuns a tuple
    containing the string, and the square of the int or float
    """
    return (k, float(v ** 2))

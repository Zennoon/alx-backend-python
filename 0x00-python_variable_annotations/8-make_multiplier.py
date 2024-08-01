#!/usr/bin/env python3
"""
Contains:
    Functions
    =========
    make_multiplier - accepts a float and returns a function that also
    accepts a float and returns the product of original float and its arg
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Accepts a float and returns a function that also accepts a float
    returns their product
    """
    def multiplier_func(n: float) -> float:
        return multiplier * n
    return multiplier_func

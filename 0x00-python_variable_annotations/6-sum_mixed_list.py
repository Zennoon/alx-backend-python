#!/usr/bin/env python3
"""
Contains:
    Functions
    =========
    sum_mixed_list - accepts a list of ints and floats and returns their sum
    (as a float)
"""
from typing import List


def sum_mixed_list(mxd_list: List[float | int]) -> float:
    """
    Accepts a list of ints and floats and returns their sum (as a float)
    """
    return float(sum(mxd_list))

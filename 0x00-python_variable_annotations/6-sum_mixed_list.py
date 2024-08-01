#!/usr/bin/env python3
"""
Contains:
    Functions
    =========
    sum_mixed_list - accepts a list of ints and floats and returns their sum
    (as a float)
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """
    Accepts a list of ints and floats and returns their sum (as a float)
    """
    return float(sum(mxd_lst))

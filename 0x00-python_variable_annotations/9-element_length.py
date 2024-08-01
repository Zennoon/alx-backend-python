#!/usr/bin/env python3
"""
Contains:
    Functions
    =========
    element_length - accepts a list of iterables and returns
    a list of tuples containing the iterable and its length
    for each item
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Accepts an iterable of sequences and returns
    a list of tuples containing the sequence and its length
    for each item
    """
    return [(i, len(i)) for i in lst]

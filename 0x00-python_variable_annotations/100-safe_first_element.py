#!/usr/bin/env python3
"""
Contains:
    Functions
    =========
    safe_first_element - function that accepts a sequence of unknown type
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[str, None]:
    if lst:
        return lst[0]
    else:
        return None

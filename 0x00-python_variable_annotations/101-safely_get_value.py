#!/usr/bin/env python3
"""
Contains:
    Functions
    =========
    safely_get_value
"""
from typing import Any, Mapping, TypeVar, Union

M = Mapping
T = TypeVar('T')
U_arg = Union[T, None]
U_return = Union[Any, T]


def safely_get_value(dct: M, key: Any, default: U_arg) -> U_return:
    """
    Function with a type variable used for annotating args and return types
    """
    if key in dct:
        return dct[key]
    else:
        return default

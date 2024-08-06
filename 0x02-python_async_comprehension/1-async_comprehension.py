#!/usr/bin/env python3
"""
Contains:
    Functions/Coroutines
    ====================
    async_comprehension - collects the 10 random numbers yielded
    by async_generator() and returns them as a list
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects the 10 random numbers yielded
    by async_generator() and returns them as a list
    """
    return [val async for val in async_generator()]

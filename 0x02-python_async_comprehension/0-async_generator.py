#!/usr/bin/env python3
"""
Contains:
    Functions/Coroutines
    ====================
    async_generator - An async generator that yields random
    values ten times and sleeps for a second
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Generates/yields a random value between 1 and 10 ten times
    and each time sleeps for 1 second
    """
    for i in range(10):
        await asyncio.wait([asyncio.sleep(1)])
        yield random.uniform(0, 10)

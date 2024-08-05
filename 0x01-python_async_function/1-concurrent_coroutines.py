#!/usr/bin/env python3
"""
Contains:
    Functions
    =========
    wait_n - an async coroutine to spawn calls to
    another coroutine a given number of times using
    asyncio's gather function
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Calls another coroutines n times passing the given max_delay value
    """
    return (await asyncio.gather(*(wait_random(max_delay) for _ in range(n))))

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
#!/usr/bin/env python3
"""
Contains:
    Functions
    =========
    task_wait_n - Identical to wait_n except it uses the
    task_wait_random (which returns a Task) instead of wait_random
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Identical to wait_n except it uses the
    task_wait_random (which returns a Task) instead of wait_random
    """
    """
    Calls another coroutines n times passing the given max_delay value
    """
    return [await res
            for res in asyncio.as_completed([task_wait_random(max_delay)
                                             for _ in range(n)])]

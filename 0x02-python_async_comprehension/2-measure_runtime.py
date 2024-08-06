#!/usr/bin/env python3
"""
Contains:
    Functions/Coroutines
    ====================
    measure_runtime - Measures the time taken to execute the
    async_comprehension coroutine 4 times
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the time taken to execute the
    async_comprehension coroutine 4 times
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return (time.perf_counter() - start)

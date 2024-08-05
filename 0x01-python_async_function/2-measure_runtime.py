#!/usr/bin/python3
"""
Contains:
    Functions
    =========
    measure_time - measures time per call to the async coroutine wait_n
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Calls wait_n with the given arguments and measures the
    average time it takes for wait_n to execute one wait_random
    call
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return ((end - start) / n)

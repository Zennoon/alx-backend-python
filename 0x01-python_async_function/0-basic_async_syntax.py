#!/usr/bin/env python3
"""
Contains:
    Functions
    =========
    wait_random - an async coroutine that accepts an integer
    and waits/sleeps for a random time between 0 and given integer
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Sleeps for a randomly generated float seconds between 0 and given integer
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return (rand)

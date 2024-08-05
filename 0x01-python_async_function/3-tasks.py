#!/usr/bin/env python3
"""
Contains:
    Functions
    =========
    task_wait_random - creates a task from the wait_random coroutine
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates a task by calling the wait_random function
    passing the given arg
    """
    return (asyncio.create_task(wait_random(max_delay)))

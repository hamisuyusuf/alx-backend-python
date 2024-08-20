#!/usr/bin python3

"""
    an asynchronous Python program
"""
import asyncio
import random


async def async_generator():
    """
        an asynchronous Python program that
        loops 10 times with a 1-second wait between iterations
        and yields a random number between 0 and 10,
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

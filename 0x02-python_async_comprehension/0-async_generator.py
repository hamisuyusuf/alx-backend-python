#!/usr/bin/env python3
"""
    Module 0-async_generator
    This module contains the async_generator coroutine.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields a random number
    between 0 and 10 after waiting 1 second.

    This coroutine will loop 10 times,
    each time asynchronously waiting for 1 second,
    then yielding a random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

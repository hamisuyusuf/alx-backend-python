#!/usr/bin/env python3
"""
    Module 0-basic_async_syntax
    This module contains the wait_random.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """an asynchronous coroutine that takes in an integer argument """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay

#!/usr/bin/env python3

"""
Module 0-basic_async_syntax.

This module contains the implementation of the wait_n function,
which spawns wait_random n times and returns a list of delays.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay value for wait_random.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

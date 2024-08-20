#!/usr/bin/env python3
"""
    Module 2-measure_runtime
    This module contains the measure_runtime coroutine.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel and measures the
    total runtime.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()  # Start the timer

    # Run four instances of async_comprehension in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()  # End the timer

    return end_time - start_time  # Return the total runtime

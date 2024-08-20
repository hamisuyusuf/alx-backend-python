#!/usr/bin/env python3
"""
    Module async_comprehension
    This module contains the async_comprehension coroutine which
    collects 10 random numbers using async comprehension.
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension from async_generator.

    This function asynchronously collects 10
    random numbers from the async_generator
    coroutine and returns them as a list of floats.

    Returns:
        List[float]: A list of 10 floating-point numbers
        collected asynchronously.
    """
    return [num async for num in async_generator()]

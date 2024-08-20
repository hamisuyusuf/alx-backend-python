#!/usr/bin python3

"""
    async_generator
"""

import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
        Use async comprehension to collect
        10 random numbers from async_generator
    """
    return [num async for num in async_generator()]

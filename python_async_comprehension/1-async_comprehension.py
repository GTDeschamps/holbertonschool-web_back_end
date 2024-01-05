#!/usr/bin/env python3
"""
Import async_generator from the previous task and then
write a coroutine called async_comprehension that takes no arguments.
The coroutine will collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers.
"""


from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    The async_comprehension coroutine uses an async comprehension to collect
    10 random numbers by iterating over the async_generator coroutine.
    Finally, it returns the list of 10 random numbers.
    """

    random_numbers = [number async for number in async_generator()]
    return random_numbers[:10]

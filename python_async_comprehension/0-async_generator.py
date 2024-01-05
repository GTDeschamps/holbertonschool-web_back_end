#!/usr/bin/env python3
"""
Write a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""


import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    This async_generator coroutine will yield a random float number
    between 0 and 10 every second, 10 times in total.

    You can use this coroutine by iterating over it
    in an asynchronous function.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

#!/usr/bin/env python3
"""Import async_comprehension from the previous file and write
a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.
"""

import typing
import asyncio
import random
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Now, regarding the total runtime being roughly 10 seconds when executing
    async_comprehension four times in parallel,
    it's because the async_comprehension coroutine generates 10 random numbers
    asynchronously, each taking around 1 second to generate due to the 1-second
    asynchronous delay in async_generator. Since async_comprehension is called
    four times concurrently using asyncio.gather,
    the overall time taken is around 10 seconds
    (approximately 4 times the 1-second delay for each execution).
    """

    start_time = time.time()
    # Execute async_comprehension four times in parallel using asyncio.gather

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime

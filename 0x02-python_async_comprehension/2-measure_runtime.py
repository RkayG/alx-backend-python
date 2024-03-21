#!/usr/bin/env python3
"""
fx measure_runtime should
measure the total runtime
and return it.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """return total time it takes
      run async_comprehension 4 times"""
    start: float = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    total: float = time.perf_counter() - start
    return total

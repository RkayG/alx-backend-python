#!/usr/bin/env python3
"""
async routine called wait_n that takes
 in 2 int arguments (in this order):
 n and max_delay. That spawns wait_random
n times with the specified max_delay.
"""
from typing import List
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times"""
    jobs = []
    delays = []

    for i in range(n):
        job = wait_random(max_delay)
        jobs.append(job)

    for job in asyncio.as_completed((jobs)):
        delay = await job
        delays.append(delay)

    return delays

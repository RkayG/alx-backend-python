#!/usr/bin/env python3
"""
Take the code from wait_n and alter
 it into a new function task_wait_n.
 The code is nearly identical to wait_n
 except task_wait_random is being called.
"""
from typing import List
import asyncio

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times"""
    jobs = []
    delays = []

    for i in range(n):
        job = task_wait_random(max_delay)
        jobs.append(job)

    for job in asyncio.as_completed((jobs)):
        delay = await job
        delays.append(delay)

    return delays

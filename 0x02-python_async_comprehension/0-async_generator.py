#!/usr/bin/env python3

"""
A coroutine called async_generator
that takes no arguments.
that will loop 10 times, each time
asynchronously wait 1 second, then
yield a random number between 0 and 10.
Use the random module.
"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator:
    """return random number after 1 second"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

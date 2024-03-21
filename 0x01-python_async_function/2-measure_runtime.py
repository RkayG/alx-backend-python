#!/usr/bin/env python3
"""
measures the total execution time
 for wait_n(n, max_delay), and
 returns total_time / n
"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """calculates time it takes to run once cycle wait_n"""
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    single_cycle: float = elapsed / n
    return single_cycle

#!/usr/bin/env python3

"""
function takes string and int
or float and returns a tuple
containing the string and the 
square of the int or float
"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """returns tuple containing k and square
    of v"""
    return (k, float(v * v))

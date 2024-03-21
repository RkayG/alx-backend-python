#!/usr/bin/env python3

"""
function which takes a
mix of int and floats and
returns their sum
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of ints and float
    in mxd_list"""
    sum: int = 0
    for x in mxd_lst:
        sum = sum + x
    return sum

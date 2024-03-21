#!/usr/bin/env python3

"""
annotate function
def element_length(lst):
    return [(i, len(i)) for i in lst]
"""
import typing


def element_length(
    lst: typing.Iterable[typing.Sequence],
) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """returns length of items in lst"""
    return [(i, len(i)) for i in lst]

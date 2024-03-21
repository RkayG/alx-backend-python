#!/usr/bin/env python3
"""
function with correct 
duck type annotation
"""

import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """return first elwment"""
    if lst:
        return lst[0]
    else:
        return None

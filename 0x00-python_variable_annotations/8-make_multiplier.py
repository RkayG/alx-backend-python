#!/usr/bin/env python3

"""
function takes a float
returns a function that multiplies
the float with another float
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns function that multiplies a float by
    multiplier"""

    def innerFx(x: float) -> float:
        """multiplies x by multiplier"""
        return multiplier * x

    return innerFx

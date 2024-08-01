#!/usr/bin/env python3
"""
This module provides a type-annotated function `make_multiplier` that takes a
float multiplier as an argument and returns a function. This returned function
takes a float as an argument and multiplies it by the initially provided
multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    Params:
    multiplier (float): The multiplier value for the returned function.

    Returns:
    Callable[[float], float]: A function that multiplies its input by the
    specified multiplier.
    """
    return lambda x: x * multiplier

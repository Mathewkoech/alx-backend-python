#!/usr/bin/env python3
"""
Method to Sum a list of float
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of float numbers.

    Parameters:
    input_list (List[float]): A list of float numbers.

    Returns:
    float: The sum of the numbers in the list.
    """
    return sum(input_list)

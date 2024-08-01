#!/usr/bin/env python3

"""
duck-typed annotations
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence, or None if the sequence is empty.

    Parameters:
    lst (Sequence[Any]): A sequence from which the first
    element is to be returned.

    Returns:
    Union[Any, None]: The first element of the sequence,
    or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

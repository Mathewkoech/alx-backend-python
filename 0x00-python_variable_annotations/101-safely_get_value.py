#!/usr/bin/env python3
"""
Module parameters and the return values, add type annotations to the function
"""

from typing import Mapping, Any, TypeVar, Union

V = TypeVar('V')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[V, None] = None) -> Union[Any, V]:
    """
    Returns the value for a given key from a dictionary.
    If the key is not found,returns a default value.

    Parameters:
    dct (Mapping): The dictionary from which to retrieve the value.
    key (Any): The key to look for in the dictionary.
    default (Union[V, None], optional): The default value to
    return if the key is not found.

    Returns:
    Union[Any, V]
    """
    if key in dct:
        return dct[key]
    else:
        return default

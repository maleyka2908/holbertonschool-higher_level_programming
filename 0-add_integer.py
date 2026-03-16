#!/usr/bin/python3
"""
This module defines an integer addition function.
It contains a single function: add_integer(a, b).
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a: first value.
        b: second value.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an int or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)

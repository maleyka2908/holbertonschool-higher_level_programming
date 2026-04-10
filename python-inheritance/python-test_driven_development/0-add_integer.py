#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: The first integer or float.
        b: The second integer or float (default 98).

    Raises:
        TypeError: If a or b are not integers or floats.

    Returns:
        The sum of a and b as an integer.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)

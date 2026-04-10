#!/usr/bin/python3
"""
This module provides a function that adds two integers.
It ensures that the inputs are either integers or floats before adding.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float (default is 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an integer or a float.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)

#!/usr/bin/python3
"""
This module provides a function for integer addition.
It ensures that inputs are valid integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two numbers and returns the result as an integer.

    Args:
        a: The first number (int or float).
        b: The second number (int or float), default is 98.

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

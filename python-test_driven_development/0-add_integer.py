#!/usr/bin/python3
"""
This module provides a function that adds two integers.
The function ensures types are valid and handles casting.
It is part of the Holberton project.
"""


def add_integer(a, b=98):
    """Adds two integers or floats (casted to integers).
    Returns the sum as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN, Infinity və ya Overflow yarada biləcək çox böyük float yoxlaması
    try:
        a = int(a)
    except (ValueError, OverflowError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (ValueError, OverflowError):
        raise TypeError("b must be an integer")

    return a + b

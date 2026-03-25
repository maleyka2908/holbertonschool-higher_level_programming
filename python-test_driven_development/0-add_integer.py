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

    # NaN və Infinity yoxlaması (çünki int() bunları çevirə bilmir)
    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

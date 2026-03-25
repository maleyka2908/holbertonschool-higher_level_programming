#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds 2 integers.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    # NaN və infinity yoxlaması
    if isinstance(a, float):
        if a != a or a in (float('inf'), float('-inf')):
            raise TypeError("a must be an integer")

    if isinstance(b, float):
        if b != b or b in (float('inf'), float('-inf')):
            raise TypeError("b must be an integer")

    return int(a) + int(b)

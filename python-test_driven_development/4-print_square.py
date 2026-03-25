#!/usr/bin/python3
"""
This module provides a function that prints a square.
The square is printed using the # character.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: The length of the square's side.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        if not isinstance(size, float):
            raise TypeError("size must be an integer")

    if isinstance(size, float):
        size = int(size)

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

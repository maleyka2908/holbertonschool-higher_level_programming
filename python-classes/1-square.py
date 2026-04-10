#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size of the square.
        """
        self.__size = size

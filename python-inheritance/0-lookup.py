#!/usr/bin/python3
"""
This module defines a lookup function.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to look into.

    Returns:
        list: A list of attributes and methods.
    """
    return dir(obj)

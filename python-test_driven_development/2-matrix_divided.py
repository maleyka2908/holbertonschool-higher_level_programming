#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists containing integers or floats.
        div: The number to divide the matrix elements by.

    Returns:
        A new matrix with the results rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # 1. Matrix validation (Type and structure)
    if not isinstance(matrix, list) or matrix == [] or not isinstance(matrix[0], list):
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    # 2. Row size validation
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # 3. Divisor validation (Type)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 4. Division by zero validation
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 5. Matrix division and rounding
    return [[round(element / div, 2) for element in row] for row in matrix]

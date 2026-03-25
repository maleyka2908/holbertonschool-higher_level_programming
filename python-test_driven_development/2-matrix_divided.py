#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
The matrix must be a list of lists of integers or floats.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix: A list of lists of integers or floats.
        div: The number to divide by.

    Returns:
        A new matrix with rounded results.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats.
        TypeError: If rows have different sizes.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(msg)

    return [[round(elem / div, 2) for elem in row] for row in matrix]

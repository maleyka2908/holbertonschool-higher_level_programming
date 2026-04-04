#!/usr/bin/python3
"""
This module provides a function 'matrix_divided' that divides
all elements of a matrix by a given divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): A list of lists of integers or floats.
        div (int/float): The number to divide by.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        list: A new matrix with all elements divided by div, rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Check if matrix is a list and not empty
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    # Check if every element in the matrix is a list and contains numbers
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError(msg)

    # Check if all rows have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new matrix with rounded values
    return [[round(val / div, 2) for val in row] for row in matrix]

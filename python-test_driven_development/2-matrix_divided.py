#!/usr/bin/python3
"""Module that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix."""
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(msg)
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError(msg)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(val / div, 2) for val in row] for row in matrix]

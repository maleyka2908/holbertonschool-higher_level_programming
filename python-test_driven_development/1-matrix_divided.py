#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not matrix:
        raise TypeError(msg)

    row_size = None

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)

        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(msg)

            # 🔥 NaN və inf yoxlama
            if isinstance(elem, float):
                if elem != elem or elem in (float('inf'), float('-inf')):
                    raise TypeError(msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 🔥 div üçün də yoxlama
    if isinstance(div, float):
        if div != div or div in (float('inf'), float('-inf')):
            raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]

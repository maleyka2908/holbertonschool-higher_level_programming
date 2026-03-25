#!/usr/bin/python3
"""
Module for matrix_divided method.
"""
import math

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Hər şeyi böl, inf/nan qalacaq, finite ədədləri round et
    result = []
    for row in matrix:
        new_row = []
        for x in row:
            val = x / div
            if not math.isnan(val) and not math.isinf(val):
                val = round(val, 2)
            new_row.append(val)
        result.append(new_row)
    return result

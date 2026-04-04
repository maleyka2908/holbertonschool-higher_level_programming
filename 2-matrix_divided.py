#!/usr/bin/python3
"""
Module for matrix division.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(msg)
    if not all(isinstance(row, list) for row in matrix) or matrix[0] == []:
        raise TypeError(msg)
    for row in matrix:
        if not all(isinstance(val, (int, float)) for val in row):
            raise TypeError(msg)
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("matrix must have each row with the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]

#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix with all elements divided by div.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # 1. Matris tip kontrolü
    if not isinstance(matrix, list) or matrix == [] or not matrix[0]:
        raise TypeError(msg)

    # 2. Satırların liste olup olmadığı ve içindeki elemanların tipi
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)

    # 3. Satır boyutlarının aynı olması (Rectangular check)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # 4. Div'in sayı olup olmadığı
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 5. Sıfıra bölme hatası
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 6. Bölme ve yuvarlama
    return [[round(x / div, 2) for x in row] for row in matrix]

#!/usr/bin/python3
"""
This module contains a function that returns Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the
    Pascal’s triangle of n.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: A list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        # Hər sətir 1 ilə başlayır
        row = [1]
        
        # Ortadakı elementləri hesabla
        for j in range(len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j + 1])
        
        # Hər sətir 1 ilə bitir
        row.append(1)
        triangle.append(row)

    return triangle

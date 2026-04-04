#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix.
    
    Args:
        matrix: list of lists of integers/floats
        div: number (integer or float) to divide by
        
    Returns:
        New matrix with elements divided by div, rounded to 2 decimal places
        
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If rows of matrix have different sizes
        TypeError: If div is not a number
        ZeroDivisionError: If div is 0
    """
    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if matrix is not empty
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all elements are lists and not empty
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if not row:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all elements are integers or floats
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all rows have the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Create new matrix with divided elements
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            # Divide and round to 2 decimal places
            result = round(element / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)
    
    return new_matrix

#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Matrisin hər bir elementinin kvadratını hesablayıb yeni matris qaytarır"""
    if matrix is None:
        return None

    # Yeni matris yaradırıq (List comprehension daxilində list comprehension)
    return [[x**2 for x in row] for row in matrix]

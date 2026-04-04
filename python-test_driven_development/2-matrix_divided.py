#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix containing integers or floats.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with elements divided and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows have different sizes.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # 1. Div kontrolünü matrisin hemen başında yap (Sayı kontrolü)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 2. Sıfıra bölme kontrolü
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 3. Matris genel yapı kontrolü
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(msg)

    # 4. Satırların kontrolü ve eleman tipleri
    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(msg)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    # 5. Satır boyutu kontrolü (Tüm satırlar ilk satırla aynı boyutta mı?)
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # 6. İşlem (round inf/nan durumlarını otomatik yönetir)
    return [[round(element / div, 2) for element in row] for row in matrix]
EOFcat << 'EOF' > 2-matrix_divided.py
#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix containing integers or floats.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with elements divided and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows have different sizes.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # 1. Div kontrolünü matrisin hemen başında yap (Sayı kontrolü)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 2. Sıfıra bölme kontrolü
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 3. Matris genel yapı kontrolü
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(msg)

    # 4. Satırların kontrolü ve eleman tipleri
    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(msg)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    # 5. Satır boyutu kontrolü (Tüm satırlar ilk satırla aynı boyutta mı?)
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # 6. İşlem (round inf/nan durumlarını otomatik yönetir)
    return [[round(element / div, 2) for element in row] for row in matrix]
EOFcat << 'EOF' > 2-matrix_divided.py
#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix containing integers or floats.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with elements divided and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows have different sizes.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # 1. Div kontrolünü matrisin hemen başında yap (Sayı kontrolü)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 2. Sıfıra bölme kontrolü
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 3. Matris genel yapı kontrolü
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(msg)

    # 4. Satırların kontrolü ve eleman tipleri
    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(msg)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    # 5. Satır boyutu kontrolü (Tüm satırlar ilk satırla aynı boyutta mı?)
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # 6. İşlem (round inf/nan durumlarını otomatik yönetir)
    return [[round(element / div, 2) for element in row] for row in matrix]

#!/usr/bin/python3
"""Module for matrix_divided function.
This module defines a function to divide all elements of a matrix.
It provides safe division and returns a new matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.
Args:
    matrix: list of lists of integers or floats.
    div: number used to divide each element.
Returns: a new matrix with elements divided and rounded to 2 decimals.
    """

    # Validate matrix type
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check empty or bad structure
    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate row size and element types
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Build and return new matrix
    return [[round(element / div, 2) for element in row] for row in matrix]

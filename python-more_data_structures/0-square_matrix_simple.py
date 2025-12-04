#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Return a new matrix with each value squared."""
    NewMatrix = []
    for row in matrix:
        Newrow = list(map(lambda x: x * x, row))
        NewMatrix.append(Newrow)
    return NewMatrix

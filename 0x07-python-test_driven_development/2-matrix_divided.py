#!/usr/bin/python3
"""
A function that divides the numbers of a matrix
"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix: list of a lists of integers or floats
        div: The number to divide the matrix's elements by

    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elements of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size

        ZeroDivisionError: If div is zero

    Returns:
        A new matrix with the result of the division

    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix of integers/floats")

    return ([[round(num / div, 2) for num in row] for row in matrix])

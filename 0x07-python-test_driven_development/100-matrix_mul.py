#!/usr/bin/python3
"""
A function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """"
    Args:
        m_a (list of lists of that are ints/floats): first matrix
        m_b (list of lists of that are ints/floats): second matrix
    Raises:
        TypeError: if m_a or m_b is not a list
        TypeError: if m_a or m_b is not a list of lists
        ValueError: if m_a or m_b is empty
        TypeError: if one element of those list of lists is not an integer or a float
        TypeError: if m_a or m_b is not a rectangle (all 'rows' should be of the same size) 
        ValueError: if m_a and m_b can't be multiplied

    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not all(type(row) is list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(type(row) is list for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if not all(type(num) in [int, float] for num in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(type(num) in [int, float] for num in row):
            raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]
    return (m_c)

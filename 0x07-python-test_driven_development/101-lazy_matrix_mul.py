#!/usr/bin/python3
"""
A function that multiplies 2 matrices using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices using NumPy
    Args:
        m_a (list of lists of ints or floats): first matrix
        m_b list of lists of ints or floats): second matrix
    Returns:
        the multiplied matrix
    """

    return (np.matmul(m_a, m_b))

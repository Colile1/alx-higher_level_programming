#!/usr/bin/python3
"""
A function that prints a square using #

"""


def print_square(size):
    """
    prints a square using #
    Args:
        size: the length of the square sides
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    Returns:
        None
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        print("#" * size)

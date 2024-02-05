#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Represents a square

    Attributes:
        __size (int): Length of a side of the square
    """

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The length of a side of the square

        Returns: None
        """
        self.__size = size

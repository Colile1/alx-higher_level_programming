#!/usr/bin/python3
"""Defines a class Square which represents a square"""


class Square:
    """Represents a square which is a shape with 4 equal sides and 4 90 degree angles

    Attributes:
        __size (int): length of a side of the square 
    """
    def __init__(self, size=0):
        """Initializes a new Square by setting the size attribute

        Args:
            size (int): The length of a side of the new square

        Returns:
            None
        """
        self.size = size

    def area(self):
        """Calculates and returns the area of the square

        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """Getter for the __size attribute

        Returns:
            The length of a side of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the __size attribute

        Args:
            value (int): The new length of a side for the square

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

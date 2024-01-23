#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Square class represents a square

    Attributes:
        __size (int): length of a side of the square
    """
    def __init__(self, size=0):
        """Initialize a new Square

        Args:
            size (int): length of the square's side

        Returns:
            None
        """
        self.size = size

    def area(self):
        """Calculate area of the square

        Returns:
            Area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """Get the length of the square's side

        Returns:
            Length of the square's side
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the length of the square's side

        Args:
            value (int): New length of the square's side

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

    def my_print(self):
        """Print the square

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))

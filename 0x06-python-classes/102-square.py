#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """This class represents a square

    Attributes:
        __size (int): length of a side of the square
    """
    def __init__(self, size=0):
        """Initialize a new Square

        Args:
            size (int): length of a side of the square

        Returns:
            None
        """
        self.size = size

    def area(self):
        """Calculate area of the square

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
            value (int): The length of a side for the square

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

    def __lt__(self, other):
        """Compare if square is less than another by area

        Args:
            other (Square): square to compare to

        Returns:
            True or False
        """
        return self.size < other.size

    def __le__(self, other):
        """Compare if square is less than or equal to another by area

        Args:
            other (Square): square to compare to

        Returns:
            True or False
        """
        return self.size <= other.size

    def __eq__(self, other):
        """Compare if square is equal to another by area

        Args:
            other (Square): square to compare to

        Returns:
            True or False
        """
        return self.size == other.size

    def __ne__(self, other):
        """Compare if square is not equal to another by area

        Args:
            other (Square): square to compare to

        Returns:
            True or False
        """
        return self.size != other.size

    def __ge__(self, other):
        """Compare if square is greater than or equal to another by area

        Args:
            other (Square): square to compare to

        Returns:
            True or False
        """
        return self.size >= other.size

    def __gt__(self, other):
        """Compare if square is greater than another by area

        Args:
            other (Square): square to compare to

        Returns:
            True or False
        """
        return self.size > other.size

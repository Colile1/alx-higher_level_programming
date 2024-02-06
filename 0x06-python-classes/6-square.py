#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """This class represents a square

    Attributes:
        __size (int): length of a side of the square
        __position (tuple): coordinates of the square in 2D space
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square

        Args:
            size (int): length of a side of the square
            position (tuple): coordinates of the square in 2D space

        Returns:
            None
        """
        self.size = size
        self.position = position

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
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for l in range(self.__size)]))

    @property
    def position(self):
        """Get the coordinates of the square

        Returns:
            The position of the square in 2D space
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the coordinates of the square

        Args:
            value (tuple): New coordinates of the square in 2D space

        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
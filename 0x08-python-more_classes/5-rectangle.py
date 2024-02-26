#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
"""


class Rectangle:
    """Rectangle class:
    Attributes:
        __width (int): width of the rectangle
        __height (int): height of the rectangle
    Methods:
        __init__(self, width=0, height=0)
        width(self) - getter
        width(self, value) - setter
        height(self) - getter
        height(self, value) - setter
        area(self) - calculates area
        perimeter(self) - calculates perimeter
        __str__(self) - prints rectangle with #
        __repr__(self)
        __del__(self) - prints message when deleting
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return (("#" * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")

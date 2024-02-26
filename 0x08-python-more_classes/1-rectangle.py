#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """
    Rectangle class

    Simple rectangle class with width and height attributes.

    Attributes:
        width (int): The width of the rectangle. Defaults to 0.
        height (int): The height of the rectangle. Defaults to 0.

    Methods:
        __init__(): Constructor, initializes width and height.
        @property width: Getter for width.
        @width.setter: Setter for width, checks type and value.
        @property height: Getter for height.
        @height.setter: Setter for height, checks type and value.
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

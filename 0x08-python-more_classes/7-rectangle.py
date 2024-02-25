#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by: (based on 6-rectangle.py)
"""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): Number of Rectangle instances.
        print_symbol (any): Symbol used for string representation. 

    Methods:
        __init__(self, width=0, height=0): Initialize a Rectangle.
        area(self): Calculate the area of the Rectangle.
        perimeter(self): Calculate the perimeter of the Rectangle.
        __str__(self): Return the string representation of the Rectangle.
        __repr__(self): Return the representation of the Rectangle.
        __del__(self): Print a message when a Rectangle is deleted.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Calculate the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the string representation of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = "\n".join([str(self.print_symbol) * self.__width
                          for i in range(self.__height)])
        return rect

    def __repr__(self):
        """Return the representation of the Rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when a Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1


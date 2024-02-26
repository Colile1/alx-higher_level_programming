#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by: (based on 5-rectangle.py)
"""


class Rectangle:
    """
    Rectangle class:
    Defines a rectangle with attributes like height, width, area, and perimeter
    Keeps track of number of Rectangle instances.
    Provides methods to get/set width and height.
    Contains methods to calculate area and perimeter.
    Implements __str__, __repr__, and __del__ methods.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize new Rectangle instance with given width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        Returns 0 if either width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return an informal string representation of the rectangle.
        Returns empty string if both width and height are 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """Return the official string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print message when a Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

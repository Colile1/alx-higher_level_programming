#!/usr/bin/python3
"""This code defines a class called MagicClass to represent a circle"""
import math


class MagicClass:
    """This class represents a circle"""
    def __init__(self, radius=0):
        """This method initializes the MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """This method calculates the area of the circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """This method calculates the circumference of the circle"""
        return 2 * math.pi * self.__radius

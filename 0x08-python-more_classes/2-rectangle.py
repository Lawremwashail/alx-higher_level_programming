#!/usr/bin/python3
"""Represents a rectangle."""


class Rectangle:
    """Represents the rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization for rectangle

    Args:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for width of the rectangle"""
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
        """Setter for the height if the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Represents the area of the rectangle and returns it"""

        return self.__width * self.__height

    def perimeter(self):
        """Represents and returns the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)

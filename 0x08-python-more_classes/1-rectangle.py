#!/usr/bin/python3
"""Represents a rectangle."""


class Rectange:
    """Represents the rectangle"""
    def __init__(self, width=0, height=0):
        """Initialization for rectangle
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        Raises:
            TypeError: If width and height are not an interger
            ValueError: If width and height are less than 0
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter/setter for width of the rectangle"""
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
        """Getter/setter for the height if the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

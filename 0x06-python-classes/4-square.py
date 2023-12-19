#!/usr/bin/python3
"""Class Module"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """"
        Initialization for square size
        Args:
            size (int): The size of one side of square
        """
        self.size = size

    @property
    def size(self):
        """
        Get or set the current size of the square
        Returns:
            TypeError: if size is not an integer
            ValueError: if value is less than 0
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the Area of the square"""
        return (self.__size ** 2)

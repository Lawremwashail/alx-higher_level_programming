#!/usr/bin/python3
"""Class module"""


class Square:
    """Defines a class"""
    def __init__(self, size=0):
        """
        Initialization of square and size
        Args:
            size (int): The size of one side
        Raises:
            TypeError if size is not an integer
            ValueError if value is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Area of the square.

        Returns:
            The Area of the sqaure.
        """

        return (self.__size * self.__size)

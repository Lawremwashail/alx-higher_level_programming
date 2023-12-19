#!/usr/bin/python3
"""Module for square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initialization for square
        Args:
            size (int): The lenght of side of the square

        Raises:
            TypeError: If size is not an interger
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

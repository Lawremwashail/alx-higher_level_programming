#!/usr/bin/python3
"""Module for square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initialization for square
        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            """Checks whether size is of type int and raises error if not"""
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

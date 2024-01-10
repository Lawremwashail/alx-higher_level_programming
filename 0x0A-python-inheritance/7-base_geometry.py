#!/usr/bin/python3
"""Represents a class"""


class BaseGeometry:
    """Defines the class"""
    def area(self):
        """Function for area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method to validate the value

        Args:
            name (str): The name given
            value (int): The value to validate

        Raise:
            TypeError: if not an int
            ValueError: if value not greater than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

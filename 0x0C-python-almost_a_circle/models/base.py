#!/usr/python3
"""Defines a base model class."""


class Base:
    """Base class"""
    __nb_objects = 0
    """Private class attribute"""

    def __init__(self, id=None):
        """Initializes the base class

        Args:
            id (int): The id of the Base class
        """

        if id not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

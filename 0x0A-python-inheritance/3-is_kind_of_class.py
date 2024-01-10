#!/usr/bin/python3
"""Function to check for object of class inherited for"""


def is_kind_of_class(obj, a_class):
    """Returns true if is an instance of inherited class
    Args:
        obj: object to check
        a_class (type): the class to check
    """
    return isinstance(obj, a_class)

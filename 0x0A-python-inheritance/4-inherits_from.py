#!/usr/bin/python3
"""Function to check for the inherited class"""


def inherits_from(obj, a_class):
    """Checks for inherited class instance
    Args:
        obj: object to check
        a_class (type): class to compare

    Return:
        True if object is of same class instance
    """
    return issubclass(type(obj), a_class)

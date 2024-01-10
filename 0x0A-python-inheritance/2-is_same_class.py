#!/usr/bin/python3
"""Function to return True for instance of same class"""


def is_same_class(obj, a_class):
    """checks for objects of smaeclass
    Args:
        obj: object to check
        a_class (type): class to compare with
    Return:
        True if matches the class and false otherwise
    """
    return type(obj) is a_class

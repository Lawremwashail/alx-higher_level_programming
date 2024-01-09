#!/usr/bin/python3
"""Function to return dictionary with simple data structure"""


def class_to_json(obj):
    """returns the dictionary form of a data structure"""
    return obj.__dict_

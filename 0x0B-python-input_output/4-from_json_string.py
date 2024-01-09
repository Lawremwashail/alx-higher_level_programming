#!/usr/bin/python3
"""Function to returns a python object from JSON """
import json


def from_json_string(my_str):
    """ returns Python object represented by a JSON string"""
    return json.loads(my_str)

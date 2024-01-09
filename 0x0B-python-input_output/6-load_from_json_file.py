#!/usr/bin/python3
"""Function to create object from JSON"""
import json


def load_from_json_file(filename):
    """Loads object from a JSON file"""
    with open(filename, 'r') as file:
        return json.load(file)

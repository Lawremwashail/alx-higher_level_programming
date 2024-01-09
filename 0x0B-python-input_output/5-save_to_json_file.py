#!/usr/bin/python3
"""Function for JSON file-writing"""
import json


def save_to_json_file(my_obj, filename):
    """oject writing to text file with JSON"""
    with open(filename, 'w', encoding='utf8') as file:
        return json.dump(my_obj, file)

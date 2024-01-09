#!/usr/bin/python3
"""Represents the student class"""


class Student:
    """Class for student"""
    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """function that retrieves a dictionary representation of a Student"""
        return self.__dict__

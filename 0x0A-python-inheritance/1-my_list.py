#!/usr/bin/python3
"""Represents a subclass myList"""


class myList(list):
    """class that inherits from the class List"""

    def print_sorted(self):
        """prints lists in a sorted order"""
        print(sorted(self))

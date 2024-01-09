#!/usr/bin/python3
"""Function to define text file reading"""


def read_file(filename=""):
    """"Prints the contents of utf8 textfile to stdout"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")

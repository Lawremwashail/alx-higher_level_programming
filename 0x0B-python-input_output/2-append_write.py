#!/usr/bin/python3
"""Function that appends a string to textfile"""


def append_write(filename="", text=""):
    """Appends a string/text to a UTF8 text file.
    Args:
        filename (str): The name of the file to append to.
        text (str): The text or string to append to the file.
    Return:
        The number of characters appended.
    """
    with open(filename, 'a', encoding='utf8') as file:
        return file.write(text)

#!/usr/bin/python3
"""Function that writes a string to textfile"""


def write_file(filename="", text=""):
    """Write a string/text to a UTF8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text or string to write to the file.
    Return:
        The number of characters written.
    """
    with open(filename, 'w' encoding='utf8') as file:
        char_nums = file.write(text)
        return char_nums

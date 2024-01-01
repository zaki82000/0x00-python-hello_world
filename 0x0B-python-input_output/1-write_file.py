#!/usr/bin/python3
"""not allowed to import any module"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)

    Return:
    returns the number of characters written
    """
    with open(filename, 'w') as file:
        return file.write(text)

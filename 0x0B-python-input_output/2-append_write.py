#!/usr/bin/python3
"""not allowed to import any module"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    
    Returns:
    returns the number of characters added
    """
    with open(filename, 'a') as file:
        return file.write(text)

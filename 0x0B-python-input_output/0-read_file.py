#!/usr/bin/python3
"""not allowed to import any module"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r',) as file:
        print(file.read(), end="")

#!/usr/bin/python3
"""
function that prints a square with the character #.
"""


def print_square(size):
    """
    function that prints a square with the character #.

    arg:
        size:  is the size length of the square

    raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0"
    """
    if not isinstance(size, int) or isinstance(size, float):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for rows in range(size):
            for columns in range(size):
                print("#", end="")
            print("")

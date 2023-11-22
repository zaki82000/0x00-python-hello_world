#!/usr/bin/python3
"""class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """class Square that defines a square by: (based on 1-square.py)

        Attributes:
            attribute1 (int): The value for attribute1.
        Methods:
            method1(): Private instance attribute: size
            method2():  defines a square by: (based on 1-square.py)
    """
    """Private instance attribute: size"""
    def __init__(self, size=0):

        """Constructor for Square.
        Args:
            attribute1 (int): The value for attribute1.
            """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size
            """Private instance attribute: size"""
    def area(self):
        return self._Square__size**2

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
        self.size = size

    def size(self):

        return self.size

    def size(self, value):

        """Constructor for Square.
        Args:
            attribute1 (int): The value for attribute1.
            """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = value
            """Private instance attribute: size"""

    def area(self):
        return self.size**2

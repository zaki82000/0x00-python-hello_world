#!/usr/bin/python3
"""not allowed to import any module"""


class Rectangle:
    """rectangle class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        """Private instance attribute: height and width """
    def width(self):
        """Private instance attribute: width: """
        return f"{self.__width}"

    def width(self, value):
        if value is int:
            return f"{self.__width}"
        elif value is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    def height(self):
        """Private instance attribute: height: """

        return f"{self.__height}"
        if value is int:
            return f"{self.__height}"
        elif value is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

#!/usr/bin/python3
"""not allowed to import any module"""


class Rectangle:
    """rectangle class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        """Private instance attribute: height and width """
    @property
    def width(self):
        """Private instance attribute: width: """
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Private instance attribute: height: """
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

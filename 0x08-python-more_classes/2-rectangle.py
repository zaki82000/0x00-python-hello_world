#!/usr/bin/python3
"""not allowed to import any module"""


class Rectangle:
    """rectangle class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        """Private instance attribute: height and width """

    @property
    def width(self):
        """Private instance attribute: width: """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Private instance attribute: width: """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):

        return 2 * (self.__width + self.__height)

#!/usr/bin/python3
"""not allowed to import any module"""


class Base:
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """class constructor"""
        if id is None:
            self.id = Base.__nb_objects + 1
            Base.__nb_objects += 1
        else:
            """
            otherwise, increment __nb_objects and
            assign the new value to the public instance attribute id
            """
            self.id = id

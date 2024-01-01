#!/usr/bin/python3
"""This module defines a Base class without importing any module."""


class Base:
    """Base class for managing objects."""

    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """Initialize a new instance of the Base class.

        Args:
            id (int, optional): The unique identifier. If not provided, a default
            identifier is generated using the class attribute __nb_objects.

        Returns:
            None
        """
        if id is None:
            self.id = Base.__nb_objects + 1
            Base.__nb_objects += 1
        else:
            """Otherwise, increment __nb_objects and assign the new value to the
            public instance attribute id.
            """
            self.id = id

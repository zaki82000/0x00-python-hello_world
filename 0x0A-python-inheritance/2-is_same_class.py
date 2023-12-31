#!/usr/bin/python3
"""not allowed to import any module"""


def is_same_class(obj, a_class):
    """function that returns True
    if the object is exactly an instance of the specified class"""
    return isinstance(obj, a_class) and a_class != object

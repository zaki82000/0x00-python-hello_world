#!/usr/bin/python3
"""
    This is add_integer function.
        Adds two number together.
            Return the sum of this numbers.
"""
def add_integer(a, b=98):
    """
    Adds two number together.
    """
    if isinstance(a, int): #:param a: must be an integer.
        if isinstance(b, int): #:param b: must be an integer.
            return a + b
        elif isinstance(b, float):
            return int(a + b)
        else:
            raise TypeError("b must be an integer")
    elif isinstance(a, float):
        return int(a + b)
    else:
        raise TypeError("a must be an integer")

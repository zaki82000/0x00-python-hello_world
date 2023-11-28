#!/usr/bin/python3
def add_integer(a, b=98):
    if isinstance(a, int):
        if isinstance(b, int):
            return a + b
        elif isinstance(b, float):
            return a + b
        else:
            raise TypeError("b must be an integer")
    elif isinstance(a, float):
        return a + b
    else:
        raise TypeError("a must be an integer")

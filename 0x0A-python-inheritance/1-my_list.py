#!/usr/bin/python3
"""not allowed to import any module"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):  # prints the list, but sorted
        sorted_list = sorted(self)
        print(sorted_list)

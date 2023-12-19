#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Use assertTrue to check to the largest number
        self.assertTrue(max_integer([1, 2, 3, 4]), 4)
    
    def test_empty_list(self):
        # Use assertIsNone to check if the list is empty
        self.assertIsNone(max_integer([]), None)
        # Use assertRaises to check raises (if element is not integer)
        with self.assertRaises(TypeError):
            max_integer([1, 'a', 3, 4])


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Use assertEqual to check the largest number
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        # Use assertEqual to check the largest number at beginning
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
    
    def test_max_in_middle(self):
        # Use assertEqual to check the largest number in middle
        self.assertEqual(max_integer([4, 3, 5, 2, 1]), 5)

    def test_one_negative_number(self):
        # Test one negative number in the list
        self.assertEqual(max_integer([-1, 1, 2, 3, 4]), 4)
    
    def test_only_negative_number(self):
        # Test only negative number in the list
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_one_negative_number(self):
        # Test ist of one element
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        # Use assertIsNone to check if the list is empty
        self.assertIsNone(max_integer([]), None)
        # Use assertRaises to check raises (if element is not integer)
        with self.assertRaises(TypeError):
            max_integer([1, 'a', 3, 4])
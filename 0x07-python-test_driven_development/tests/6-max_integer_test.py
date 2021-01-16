#!/usr/bin/python3
"""Unittest for the function max_integer(list=[])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests to get the max integer in a list"""

    def test_max_int_basic(self):
        """Tests for a normal list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_int_empty(self):
        """Tests if list is empty"""
        self.assertEqual(max_integer([]), None)

    def test_max_int_neg(self):
        """Tests if list has a negative integer"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_int_one(self):
        """Tests if list has only one value"""
        self.assertEqual(max_integer([1]), 1)

    def test_max_int_middle(self):
        """Tests if max integer is in the middle"""
        self.assertEqual(max_integer([1, 2, 5, 4, 3]), 5)

if __name__ == '__main__':
    unittest.main()

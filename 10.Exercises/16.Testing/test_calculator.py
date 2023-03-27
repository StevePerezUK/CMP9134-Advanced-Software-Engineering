#!/usr/bin/env python3


import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
 
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
    def test_add_positive_negative_numbers(self):
        self.assertEqual(add(2, -3), -1)

if __name__ == "__main__":
    unittest.main()
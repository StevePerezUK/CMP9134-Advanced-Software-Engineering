#!/usr/bin/env python3

from is_prime import is_prime as ip
import unittest


class TestIsPrime(unittest.TestCase):
    def test_simple_prime(self):
        self.assertTrue(ip(4))

    def test_simple_non_prime(self):
        self.assertTrue(ip(2))

    def test_simple_prime15(self):
        self.assertFalse(ip(15))
    
    def test_simple_prime45(self):
        self.assertFalse(ip(45))
    
    def test_simple_prime45(self):
        self.assertFalse(ip(47))

    def test_large_prime11587(self):
        self.assertTrue(ip(11587))

    def test_typeerror_1(self):
        with self.assertRaises(TypeError):
            ip(6.5)

    def test_typeerror_2(self):
        with self.assertRaises(TypeError):
            ip('six')

   
    def test_typeerror_3(self):
        with self.assertRaises(ValueError):
            ip(-7)

if __name__ == "__main__":
    unittest.main()


# 29_test_unittest_example.py
# Demonstrates use of Python's built-in unittest module.

import unittest

def multiply(a, b):
    return a * b

def is_even(n):
    return n % 2 == 0

class TestMathHelpers(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 99), 0)

    def test_is_even(self):
        for n in [0, 2, 4, 100]:
            self.assertTrue(is_even(n))
        for n in [1, 3, 5, 101]:
            self.assertFalse(is_even(n))

if __name__ == '__main__':
    unittest.main()

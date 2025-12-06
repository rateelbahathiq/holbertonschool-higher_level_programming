#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer."""

    def test_ordered_list(self):
        """Max at the end of an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max in the middle of an unordered list."""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_max_at_beginning(self):
        """Max at the beginning of the list."""
        self.assertEqual(max_integer([5, 1, 2, 3]), 5)

    def test_one_element_list(self):
        """List with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Empty list should return None."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """List with all negative numbers."""
        self.assertEqual(max_integer([-10, -5, -2, -8]), -2)

    def test_mixed_positive_negative(self):
        """List with both positive and negative numbers."""
        self.assertEqual(max_integer([-3, 10, -1, 4]), 10)

    def test_list_of_floats(self):
        """List of floats."""
        self.assertEqual(max_integer([1.5, 2.3, 0.7, 2.3]), 2.3)

    def test_list_of_ints_and_floats(self):
        """List containing both ints and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 2]), 3)

    def test_string(self):
        """String is treated as a list of chars; returns max char."""
        self.assertEqual(max_integer("Holberton"), 't')

    def test_list_of_strings(self):
        """List of strings: returns lexicographically greatest."""
        self.assertEqual(max_integer(["Holberton", "School", "Python"]), "School")

    def test_none_argument(self):
        """Passing None should raise a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_iterable(self):
        """Passing a non-iterable (e.g., int) should raise a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(5)


if __name__ == "__main__":
    unittest.main()

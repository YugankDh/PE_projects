"""
Unit Tests for Grade Calculator (Assignment 8)
9 comprehensive test cases covering average calculation, passing boundary, and grade ordering.
Supports testing either buggy_grade_calculator (RED) or fixed_grade_calculator (GREEN).
"""

import unittest
from fixed_grade_calculator import (
    calculate_average,
    is_passing,
    determine_letter_grade,
)


class TestGradeCalculator(unittest.TestCase):
    # Test 1-3: Average calculation
    def test_average_standard(self):
        self.assertAlmostEqual(calculate_average([80, 90, 100]), 90.0)

    def test_average_variable_length(self):
        self.assertAlmostEqual(calculate_average([60, 80]), 70.0)

    def test_average_empty(self):
        self.assertEqual(calculate_average([]), 0.0)

    # Test 4-6: Passing boundary
    def test_passing_above_boundary(self):
        self.assertTrue(is_passing(40.1, 40.0))

    def test_passing_exact_boundary(self):
        self.assertTrue(is_passing(40.0, 40.0))

    def test_passing_below_boundary(self):
        self.assertFalse(is_passing(39.9, 40.0))

    # Test 7-9: Grade ordering
    def test_grade_a(self):
        self.assertEqual(determine_letter_grade(95.0), "A")

    def test_grade_b(self):
        self.assertEqual(determine_letter_grade(82.0), "B")

    def test_grade_f(self):
        self.assertEqual(determine_letter_grade(32.0), "F")


if __name__ == "__main__":
    unittest.main()

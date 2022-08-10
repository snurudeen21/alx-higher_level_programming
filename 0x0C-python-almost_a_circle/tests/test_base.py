#!/usr/bin/python3
import unittest
from model_task_0 import square_area


class TestSquareArea(unittest.TestCase):
    def test_area(self):
        # Test area when length >= 0
        self.assertAlmostEqual(square_area(0), 0)
        self.assertAlmostEqual(square_area(4), 16)

    def test_value(self):
        # Ensure ValueError are raised when neccesary
        self.assertRaises(ValueError, square_area, -2)

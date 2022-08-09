#!/usr/bin/python3
import unittest
from Area import square_area


class TestSquareArea(unittest.TestCase):
    def test_area(self):
        # Test area when area >= 0
        self.assertAlmostEqual(square_area(1), 1)
        self.assertAlmostEqual(square_area(4), 16)
        self.assertAlmostEqual(square_area(0), 0)

    def test_value(self):
        # Raise value error when necesary
        self.assertRaises(ValueError, square_area, -2)

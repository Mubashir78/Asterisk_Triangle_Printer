import unittest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import Asterik_Triangle_Printer as triangle


class TestTrianglePrinter(unittest.TestCase):
    def test_valid_input(self):
        with patch("builtins.input", side_effect=["3", ""]):
            triangle.print_triangle()

    def test_zero_then_valid(self):
        with patch("builtins.input", side_effect=["0", "3", ""]):
            triangle.print_triangle()

    def test_invalid_then_valid(self):
        with patch("builtins.input", side_effect=["abc", "3", ""]):
            triangle.print_triangle()


if __name__ == "__main__":
    unittest.main()

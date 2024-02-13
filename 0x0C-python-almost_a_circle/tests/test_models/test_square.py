#!/usr/bin/python3

"""Defines unittests for models/square.py.

Unittest classes:
    TestSquareInstantiation - line 24
    TestSquareSize - line 70
    TestSquareX - line 118
    TestSquareY - line 166
    TestSquareOrderOfInitialization - line 214
    TestSquareArea - line 230
    TestSquareStdout - line 252
    TestSquareUpdateArgs - line 320
    TestSquareUpdateKwargs - line 398
    TestSquareToDictionary - line 484
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""
    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_square(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    # Rest of the tests omitted for brevity


class TestSquareSize(unittest.TestCase):
    """Unittests for testing size initialization of the Square class."""
    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    # Rest of the tests omitted for brevity


class TestSquareX(unittest.TestCase):
    """Unittests for testing initialization of Square x attribute."""
    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    # Rest of the tests omitted for brevity


class TestSquareY(unittest.TestCase):
    """Unittests for testing initialization of Square y attribute."""
    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

    # Rest of the tests omitted for brevity


class TestSquareOrderOfInitialization(unittest.TestCase):
    """Unittests for testing order of Square attribute initialization."""
    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    # Rest of the tests omitted for brevity


class TestSquareArea(unittest.TestCase):
    """Unittests for testing the area method of the Square class."""
    def test_area_small(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    # Rest of the tests omitted for brevity


class TestSquareStdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Square class."""
    # Implementation omitted for brevity


class TestSquareUpdateArgs(unittest.TestCase):
    """Unittests for testing update args method of the Square class."""
    # Implementation omitted for brevity


class TestSquareUpdateKwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of Square class."""
    # Implementation omitted for brevity


class TestSquareToDictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""
    # Implementation omitted for brevity


if __name__ == "__main__":
    unittest.main()


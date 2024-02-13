#!/usr/bin/python3
import sys
sys.path.append('models/base.py')

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """
    Test cases for Base class and its subclasses.

    Test methods:
        - test_base_instantiation: Test instantiation of Base class.
        - test_to_json_string: Test serialization to JSON string.
        - test_save_to_file: Test saving objects to file (JSON format).
        - test_from_json_string: Test loading objects from JSON string.
        - test_create: Test object creation from dictionary.
        - test_load_from_file: Test loading objects from file (JSON format).
        - test_save_to_file_csv: Test saving objects to file (CSV format).
        - test_load_from_file_csv: Test loading objects from file (CSV format).
    """

    def test_base_instantiation(self):
        """Test instantiation of Base class."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_to_json_string(self):
        """Test serialization to JSON string."""
        r = Rectangle(10, 7, 2, 8, 6)
        json_str = Base.to_json_string([r.to_dictionary()])
        self.assertIsInstance(json_str, str)
        self.assertGreater(len(json_str), 0)

    def test_save_to_file(self):
        """Test saving objects to file (JSON format)."""
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.isfile("Rectangle.json"))

    def test_from_json_string(self):
        """Test loading objects from JSON string."""
        json_str = '[{"id": 89, "width": 10, "height": 4}]'
        rect_list = Rectangle.from_json_string(json_str)
        self.assertIsInstance(rect_list, list)
        self.assertEqual(len(rect_list), 1)

    def test_create(self):
        """Test object creation from dictionary."""
        r = Rectangle(3, 5, 1, 2, 7)
        r_dict = r.to_dictionary()
        new_rect = Rectangle.create(**r_dict)
        self.assertNotEqual(r, new_rect)

    def test_load_from_file(self):
        """Test loading objects from file (JSON format)."""
        r = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r])
        rect_list = Rectangle.load_from_file()
        self.assertIsInstance(rect_list, list)
        self.assertEqual(len(rect_list), 1)


if __name__ == "__main__":
    unittest.main()


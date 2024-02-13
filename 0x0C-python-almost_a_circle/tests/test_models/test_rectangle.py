import io
import sys
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    Class for testing the Rectangle class.
    """

    def test_rectangle_creation(self):
        """
        Test creation of Rectangle objects.
        """
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

    def test_invalid_arguments(self):
        """
        Test invalid arguments for Rectangle constructor.
        """
        with self.assertRaises((TypeError, ValueError)):
            Rectangle()
            Rectangle(1)
            Rectangle(10, 2, 3, 4, 5, 6)
            Rectangle(10, 2, -1, 1)
            Rectangle(10, 2, 1, -1)
            Rectangle(10, 2, "invalid", 1)
            Rectangle(10, 2, 1, "invalid")

    def test_area(self):
        """
        Test calculation of area.
        """
        r = Rectangle(10, 2)
        self.assertEqual(r.area(), 20)

    def test_str_method(self):
        """
        Test string representation of Rectangle objects.
        """
        r = Rectangle(10, 2, 1, 1, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 10/2")

    def test_display(self):
        """
        Test display method.
        """
        r = Rectangle(2, 3, 0, 0, 0)
        capture = io.StringIO()
        sys.stdout = capture
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capture.getvalue(), "##\n##\n##\n")

    def test_update_args(self):
        """
        Test update method with positional arguments.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_kwargs(self):
        """
        Test update method with keyword arguments.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")

if __name__ == '__main__':
    unittest.main()


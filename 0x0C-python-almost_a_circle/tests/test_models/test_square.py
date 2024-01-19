#!/usr/bin/python3

import sys
import unittest
import inspect
import io
from contextlib import redirect_stdout
import pep8
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Class for testing Square class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Square, inspect.isfunction)

    def test_pep8_conformance_square(self):
        """
        Test that square.py file conforms to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_square(self):
        """
        Test that test_square.py file conforms to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exists
        """
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exists
        """
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documentation exists
        """
        for func in self.setup:
            self.assertTrue(func[1].__doc__ is not None and len(func[1]) >= 1)

    def test_square_init(self):
        """
        Test initialization of Square
        """
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_dictionary(self):
        """
        Tests for dictionary method
        """
        S = Square(100, 300, 400, 500)
        S_dict = S.to_dictionary()
        self.assertEqual(S_dict['size'], 100)
        self.assertEqual(S_dict['x'], 300)
        self.assertEqual(S_dict['y'], 400)
        self.assertEqual(S_dict['id'], 500)


if __name__ == '__main__':
    unittest.main()

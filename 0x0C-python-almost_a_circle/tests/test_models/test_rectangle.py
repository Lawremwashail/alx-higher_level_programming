#!/usr/bin/python3


import io
import sys
import unittest
import inspect
import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestModels(unittest.TestCase):
    """
    Class for testing Base class methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Base, inspect.isfunction)
        cls.rectangle_setup = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """Test that base.py file conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, "Style errors Found.")

    def test_pep8_conformance_test_base(self):
        """Test that test_base.py file conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0, "Style errors Found.")

    def test_module_docstring(self):
        """Tests if module docstring documentation exists and is non-empty"""
        self.assertTrue(len(Base.__doc__) > 0)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exists and is non-empty
        """
        self.assertTrue(len(TestBase.__doc__) > 0)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documentation exists and is non-empty
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) > 0)

    def test_attributes(self):
        r = Rectangle(8, 10, 3, 4, 1)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 1)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-8, 10, 3, 4, 1)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(8, -10, 3, 4, 1)

    def test_invalid_x(self):
        with self.assertRaises(ValueError):
            r = Rectangle(8, 10, -3, 4, 1)

    def test_invalid_y(self):
        with self.assertRaises(ValueError):
            r = Rectangle(8, 10, 3, -4, 1)

    def test_area(self):
        r = Rectangle(8, 10, 3, 4, 1)
        self.assertEqual(r.area(), 80)

    def test_display(self):
        """Arrange"""
        r = Rectangle(3, 2, 0, 0, 1)
        exp_output = "###\n###\n"

        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as \
                mock_stdout:
            r.display()
            """Assert"""
            self.assertEqual(mock_stdout.getvalue(), exp_output)

    def test_update(self):
        r = Rectangle(8, 10, 3, 4, 1)
        r.update(2, 8, 6, 4, 2)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 2)

    def test_to_dictionary(self):
        r = Rectangle(8, 10, 3, 4, 1)
        exp_dict = {'id': 1, 'width': 8, 'height': 10, 'x': 3, 'y': 4}
        self.assertEqual(r.to_dictionary(), exp_dict)

    def test_str_representation(self):
        r = Rectangle(8, 10, 3, 4, 1)
        exp_str = "[Rectangle] (1) 3/4 - 8/10"
        self.assertEqual(str(r), exp_str)


if __name__ == "__main__":
    unittest.main()

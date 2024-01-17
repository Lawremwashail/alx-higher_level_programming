#!/usr/bin/python3
"""Defines unittests for base.py."""

import sys
import os
import unittest
from models.base import Base
import unittest
sys.path.append("..")


class ClassBaseTests(unittest.TestCase):
    """Tests for the Base class"""

    def test_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        b6 = Base(39)
        b7 = Base(-7)
        b8 = Base(0)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)
        self.assertEqual(b6.id, 39)
        self.assertEqual(b7.id, -7)
        self.assertEqual(b8.id, 0)

    def test_to_json_string_empty(self):
        """Test for handling empty list"""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty(self):
        """converts list into JSON representation"""
        b1 = Base(1)
        b2 = Base(2)
        result = Base.to_json_string([b1, b2])
        expected_result = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(result, expected_result)

    def test_from_json_string_empty(self):
        """handles empty array from JSON and returns empty list"""
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_from_json_string_non_empty(self):
        """deserializes non empty JSON string into a list of Base"""
        json_str = '[{"id": 1}, {"id": 2}]'
        result = Base.from_json_string(json_str)
        expected_result = [Base(1), Base(2)]
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()

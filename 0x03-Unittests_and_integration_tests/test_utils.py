#!/usr/bin/env python3
"""
Contains:
    Classes
    =======
    TestAccessNestedMap - Parameterized unittests for the access_nested_map
    util function
"""
import unittest
from parameterized import parameterized

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Testcases for the accedd_nested_map function in the utils module"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """First test for access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 0),
        ({"a": 1}, ("a", "b"), 1)
    ])
    def test_access_nested_map_exception(self, nested_map, path, idx):
        """Tests that invalid arguments cause the function to raise an exception"""
        with self.assertRaises(KeyError, msg=path) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception).strip("'"), path[idx])



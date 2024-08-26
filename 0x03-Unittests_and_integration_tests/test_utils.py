#!/usr/bin/env python3
"""
Contains:
    Classes
    =======
    TestAccessNestedMap - Parameterized unittests for the access_nested_map
    util function
"""
import unittest
import unittest.mock
from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


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
        """
        Tests that invalid arguments cause the function
        to raise an exception
        """
        with self.assertRaises(KeyError, msg=path) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception).strip("'"), path[idx])


class TestGetJson(unittest.TestCase):
    """Testcases for the get_json util function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        with unittest.mock.patch("utils.requests") as requests_mock:
            get_return = unittest.mock.Mock()
            get_return.json.return_value = test_payload
            requests_mock.get.return_value = get_return
            self.assertEqual(get_json(test_url), test_payload)
            requests_mock.get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Testcases for the memoize decorator of the util class"""
    def test_memoize(self):
        """Tests that the memoize decorator works as expected"""
        class TestClass:
            """Testing class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with unittest.mock.patch.object(TestClass, "a_method") as a_method:
            test_object = TestClass()
            test_object.a_property()
            test_object.a_property()

            a_method.assert_called_once()

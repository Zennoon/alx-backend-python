#!/usr/bin/env python3
"""
Contains:
    Testcases for the GithubOrgClient Class of the client module
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Testcases for the GithubOrgClient class"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org, mock_get_json):
        """
        Tests the org method of the class
        """
        client = GithubOrgClient(org)
        client.org()

        mock_get_json.assert_called_once()

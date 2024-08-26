#!/usr/bin/env python3
"""
Contains:
    Testcases for the GithubOrgClient Class of the client module
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from unittest.mock import PropertyMock as PM

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

    def test_public_repos_url(self):
        """Tests the _public_repos_url property of the class"""
        with patch.object(GithubOrgClient, "org", new_callable=PM) as mock_org:
            mock_org.return_value = {"repos_url": None}
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, None)

#!/usr/bin/env python3
"""
Contains:
    Testcases for the GithubOrgClient Class of the client module
"""
import unittest
from parameterized import parameterized, parameterized_class
from typing import Dict
from unittest.mock import patch
from unittest.mock import MagicMock, Mock, PropertyMock

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Testcases for the GithubOrgClient class"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org: str, mock_get_json: MagicMock) -> None:
        """
        Tests the org method of the class
        """
        client = GithubOrgClient(org)
        client.org()

        mock_get_json.assert_called_once()

    def test_public_repos_url(self) -> None:
        """Tests the _public_repos_url property of the class"""
        with patch.object(GithubOrgClient, "org",
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": None}
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, None)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Tests the public_repos method of the class"""
        repos_json = [
            {
                "name": "Clipchart",
                "license": {
                    "key": "MIT"
                }
            },
            {
                "name": "Windows",
                "license": {
                    "key": "PRI"
                }
            },
            {
                "name": "Visual Studio Code"
            }
        ]
        mock_get_json.return_value = repos_json
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock
                ) as mock_pru:
            mock_pru.return_value = "some_url"

            client = GithubOrgClient("Microsoft")
            self.assertEqual(client.public_repos("MIT"), ["Clipchart"])

            mock_pru.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        (
            {
                "license": {"key": "my_license"}
            },
            "my_license",
            True
        ),
        (
            {
                "license": {"key": "other_license"}
            },
            "my_license",
            False
        )
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """
        Tests that the has_license method of the class behaves as expected
        """
        client = GithubOrgClient("NVIDIA")
        self.assertIs(client.has_license(repo, key), expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [
        tuple([fixture for fixture in TEST_PAYLOAD[0]])
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration testing of the public_repo method"""
    @classmethod
    def setUpClass(cls) -> None:
        """Defines code to be executed before any testing commences"""
        def payload_side_effect(url):
            """Selects the proper payload"""
            base_url = "https://api.github.com/orgs/google"
            mock = Mock()
            mock.json = Mock()
            if url == base_url:
                mock.json.return_value = cls.org_payload
            elif url == base_url + "/repos":
                mock.json.return_value = cls.repos_payload
            return mock

        cls.get_patcher = patch("requests.get", side_effect=payload_side_effect)
        cls.get_patcher.start()

    def test_public_repos(self):
        """Integration testing for the public_repos method"""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(),
            self.expected_repos
        )

    def test_public_repos_with_license(self):
        """
        Integration testing for the public_repos method with licenses
        """
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos("apache-2.0"),
            self.apache2_repos
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.get_patcher.stop()

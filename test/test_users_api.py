# coding: utf-8

"""
    Mosquito Alert API

    Introducing API v1 for Mosquito Alert platform, a project desgined to facilitate citizen science initiatives and enable collaboration among scientists, public health officials, and environmental managers in the investigation and control of disease-carrying mosquitoes.

    The version of the OpenAPI document: v1
    Contact: it@mosquitoalert.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from mosquito_alert.api.users_api import UsersApi


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UsersApi()

    def tearDown(self) -> None:
        pass

    def test_users_create(self) -> None:
        """Test case for users_create

        """
        pass

    def test_users_partial_update(self) -> None:
        """Test case for users_partial_update

        """
        pass

    def test_users_retrieve(self) -> None:
        """Test case for users_retrieve

        """
        pass

    def test_users_update(self) -> None:
        """Test case for users_update

        """
        pass


if __name__ == '__main__':
    unittest.main()

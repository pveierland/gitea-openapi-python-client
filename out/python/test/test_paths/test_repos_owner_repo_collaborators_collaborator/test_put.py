# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import openapi_client
from openapi_client.paths.repos_owner_repo_collaborators_collaborator import put  # noqa: E501
from openapi_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestReposOwnerRepoCollaboratorsCollaborator(ApiTestMixin, unittest.TestCase):
    """
    ReposOwnerRepoCollaboratorsCollaborator unit test stubs
        Add a collaborator to a repository  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204


if __name__ == '__main__':
    unittest.main()

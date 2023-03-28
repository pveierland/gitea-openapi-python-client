# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.0
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.activitypub_user_username.get import ActivitypubPerson
from openapi_client.paths.activitypub_user_username_inbox.post import ActivitypubPersonInbox


class ActivitypubApi(
    ActivitypubPerson,
    ActivitypubPersonInbox,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
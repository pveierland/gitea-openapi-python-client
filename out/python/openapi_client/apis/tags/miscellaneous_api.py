# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.0
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.nodeinfo.get import GetNodeInfo
from openapi_client.paths.signing_key_gpg.get import GetSigningKey
from openapi_client.paths.version.get import GetVersion
from openapi_client.paths.markdown.post import RenderMarkdown
from openapi_client.paths.markdown_raw.post import RenderMarkdownRaw


class MiscellaneousApi(
    GetNodeInfo,
    GetSigningKey,
    GetVersion,
    RenderMarkdown,
    RenderMarkdownRaw,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass

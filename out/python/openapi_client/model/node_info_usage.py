# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class NodeInfoUsage(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    NodeInfoUsage contains usage statistics for this server
    """


    class MetaOapg:
        
        class properties:
            localComments = schemas.Int64Schema
            localPosts = schemas.Int64Schema
        
            @staticmethod
            def users() -> typing.Type['NodeInfoUsageUsers']:
                return NodeInfoUsageUsers
            __annotations__ = {
                "localComments": localComments,
                "localPosts": localPosts,
                "users": users,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["localComments"]) -> MetaOapg.properties.localComments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["localPosts"]) -> MetaOapg.properties.localPosts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["users"]) -> 'NodeInfoUsageUsers': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["localComments", "localPosts", "users", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["localComments"]) -> typing.Union[MetaOapg.properties.localComments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["localPosts"]) -> typing.Union[MetaOapg.properties.localPosts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["users"]) -> typing.Union['NodeInfoUsageUsers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["localComments", "localPosts", "users", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        localComments: typing.Union[MetaOapg.properties.localComments, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        localPosts: typing.Union[MetaOapg.properties.localPosts, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        users: typing.Union['NodeInfoUsageUsers', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NodeInfoUsage':
        return super().__new__(
            cls,
            *_args,
            localComments=localComments,
            localPosts=localPosts,
            users=users,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.node_info_usage_users import NodeInfoUsageUsers

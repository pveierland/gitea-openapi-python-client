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


class CommitStats(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    CommitStats is statistics for a RepoCommit
    """


    class MetaOapg:
        
        class properties:
            additions = schemas.Int64Schema
            deletions = schemas.Int64Schema
            total = schemas.Int64Schema
            __annotations__ = {
                "additions": additions,
                "deletions": deletions,
                "total": total,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additions"]) -> MetaOapg.properties.additions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deletions"]) -> MetaOapg.properties.deletions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["additions", "deletions", "total", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additions"]) -> typing.Union[MetaOapg.properties.additions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deletions"]) -> typing.Union[MetaOapg.properties.deletions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> typing.Union[MetaOapg.properties.total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["additions", "deletions", "total", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        additions: typing.Union[MetaOapg.properties.additions, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        deletions: typing.Union[MetaOapg.properties.deletions, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CommitStats':
        return super().__new__(
            cls,
            *_args,
            additions=additions,
            deletions=deletions,
            total=total,
            _configuration=_configuration,
            **kwargs,
        )

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


class NodeInfoUsageUsers(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    NodeInfoUsageUsers contains statistics about the users of this server
    """


    class MetaOapg:
        
        class properties:
            activeHalfyear = schemas.Int64Schema
            activeMonth = schemas.Int64Schema
            total = schemas.Int64Schema
            __annotations__ = {
                "activeHalfyear": activeHalfyear,
                "activeMonth": activeMonth,
                "total": total,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activeHalfyear"]) -> MetaOapg.properties.activeHalfyear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activeMonth"]) -> MetaOapg.properties.activeMonth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["activeHalfyear", "activeMonth", "total", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activeHalfyear"]) -> typing.Union[MetaOapg.properties.activeHalfyear, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activeMonth"]) -> typing.Union[MetaOapg.properties.activeMonth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> typing.Union[MetaOapg.properties.total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["activeHalfyear", "activeMonth", "total", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        activeHalfyear: typing.Union[MetaOapg.properties.activeHalfyear, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        activeMonth: typing.Union[MetaOapg.properties.activeMonth, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NodeInfoUsageUsers':
        return super().__new__(
            cls,
            *_args,
            activeHalfyear=activeHalfyear,
            activeMonth=activeMonth,
            total=total,
            _configuration=_configuration,
            **kwargs,
        )

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


class MarkdownOption(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    MarkdownOption markdown options
    """


    class MetaOapg:
        
        class properties:
            Context = schemas.StrSchema
            Mode = schemas.StrSchema
            Text = schemas.StrSchema
            Wiki = schemas.BoolSchema
            __annotations__ = {
                "Context": Context,
                "Mode": Mode,
                "Text": Text,
                "Wiki": Wiki,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Context"]) -> MetaOapg.properties.Context: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Mode"]) -> MetaOapg.properties.Mode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Text"]) -> MetaOapg.properties.Text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Wiki"]) -> MetaOapg.properties.Wiki: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Context", "Mode", "Text", "Wiki", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Context"]) -> typing.Union[MetaOapg.properties.Context, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Mode"]) -> typing.Union[MetaOapg.properties.Mode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Text"]) -> typing.Union[MetaOapg.properties.Text, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Wiki"]) -> typing.Union[MetaOapg.properties.Wiki, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Context", "Mode", "Text", "Wiki", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Context: typing.Union[MetaOapg.properties.Context, str, schemas.Unset] = schemas.unset,
        Mode: typing.Union[MetaOapg.properties.Mode, str, schemas.Unset] = schemas.unset,
        Text: typing.Union[MetaOapg.properties.Text, str, schemas.Unset] = schemas.unset,
        Wiki: typing.Union[MetaOapg.properties.Wiki, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MarkdownOption':
        return super().__new__(
            cls,
            *_args,
            Context=Context,
            Mode=Mode,
            Text=Text,
            Wiki=Wiki,
            _configuration=_configuration,
            **kwargs,
        )

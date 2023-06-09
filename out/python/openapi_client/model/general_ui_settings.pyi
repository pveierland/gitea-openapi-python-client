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


class GeneralUISettings(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    GeneralUISettings contains global ui settings exposed by API
    """


    class MetaOapg:
        
        class properties:
            
            
            class allowed_reactions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'allowed_reactions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class custom_emojis(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'custom_emojis':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            default_theme = schemas.StrSchema
            __annotations__ = {
                "allowed_reactions": allowed_reactions,
                "custom_emojis": custom_emojis,
                "default_theme": default_theme,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowed_reactions"]) -> MetaOapg.properties.allowed_reactions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_emojis"]) -> MetaOapg.properties.custom_emojis: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_theme"]) -> MetaOapg.properties.default_theme: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["allowed_reactions", "custom_emojis", "default_theme", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowed_reactions"]) -> typing.Union[MetaOapg.properties.allowed_reactions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_emojis"]) -> typing.Union[MetaOapg.properties.custom_emojis, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_theme"]) -> typing.Union[MetaOapg.properties.default_theme, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["allowed_reactions", "custom_emojis", "default_theme", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        allowed_reactions: typing.Union[MetaOapg.properties.allowed_reactions, list, tuple, schemas.Unset] = schemas.unset,
        custom_emojis: typing.Union[MetaOapg.properties.custom_emojis, list, tuple, schemas.Unset] = schemas.unset,
        default_theme: typing.Union[MetaOapg.properties.default_theme, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GeneralUISettings':
        return super().__new__(
            cls,
            *_args,
            allowed_reactions=allowed_reactions,
            custom_emojis=custom_emojis,
            default_theme=default_theme,
            _configuration=_configuration,
            **kwargs,
        )

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


class OAuth2Application(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            client_id = schemas.StrSchema
            client_secret = schemas.StrSchema
            confidential_client = schemas.BoolSchema
            created = schemas.DateTimeSchema
            id = schemas.Int64Schema
            name = schemas.StrSchema
            
            
            class redirect_uris(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'redirect_uris':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "client_id": client_id,
                "client_secret": client_secret,
                "confidential_client": confidential_client,
                "created": created,
                "id": id,
                "name": name,
                "redirect_uris": redirect_uris,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_secret"]) -> MetaOapg.properties.client_secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["confidential_client"]) -> MetaOapg.properties.confidential_client: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirect_uris"]) -> MetaOapg.properties.redirect_uris: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["client_id", "client_secret", "confidential_client", "created", "id", "name", "redirect_uris", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> typing.Union[MetaOapg.properties.client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_secret"]) -> typing.Union[MetaOapg.properties.client_secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["confidential_client"]) -> typing.Union[MetaOapg.properties.confidential_client, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirect_uris"]) -> typing.Union[MetaOapg.properties.redirect_uris, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["client_id", "client_secret", "confidential_client", "created", "id", "name", "redirect_uris", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        client_id: typing.Union[MetaOapg.properties.client_id, str, schemas.Unset] = schemas.unset,
        client_secret: typing.Union[MetaOapg.properties.client_secret, str, schemas.Unset] = schemas.unset,
        confidential_client: typing.Union[MetaOapg.properties.confidential_client, bool, schemas.Unset] = schemas.unset,
        created: typing.Union[MetaOapg.properties.created, str, datetime, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        redirect_uris: typing.Union[MetaOapg.properties.redirect_uris, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OAuth2Application':
        return super().__new__(
            cls,
            *_args,
            client_id=client_id,
            client_secret=client_secret,
            confidential_client=confidential_client,
            created=created,
            id=id,
            name=name,
            redirect_uris=redirect_uris,
            _configuration=_configuration,
            **kwargs,
        )
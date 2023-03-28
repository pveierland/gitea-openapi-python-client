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


class CreateUserOption(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    CreateUserOption create user options
    """


    class MetaOapg:
        required = {
            "password",
            "email",
            "username",
        }
        
        class properties:
            email = schemas.StrSchema
            password = schemas.StrSchema
            username = schemas.StrSchema
            created_at = schemas.DateTimeSchema
            full_name = schemas.StrSchema
            login_name = schemas.StrSchema
            must_change_password = schemas.BoolSchema
            restricted = schemas.BoolSchema
            send_notify = schemas.BoolSchema
            source_id = schemas.Int64Schema
            visibility = schemas.StrSchema
            __annotations__ = {
                "email": email,
                "password": password,
                "username": username,
                "created_at": created_at,
                "full_name": full_name,
                "login_name": login_name,
                "must_change_password": must_change_password,
                "restricted": restricted,
                "send_notify": send_notify,
                "source_id": source_id,
                "visibility": visibility,
            }
    
    password: MetaOapg.properties.password
    email: MetaOapg.properties.email
    username: MetaOapg.properties.username
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["full_name"]) -> MetaOapg.properties.full_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["login_name"]) -> MetaOapg.properties.login_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["must_change_password"]) -> MetaOapg.properties.must_change_password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restricted"]) -> MetaOapg.properties.restricted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["send_notify"]) -> MetaOapg.properties.send_notify: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source_id"]) -> MetaOapg.properties.source_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visibility"]) -> MetaOapg.properties.visibility: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["email", "password", "username", "created_at", "full_name", "login_name", "must_change_password", "restricted", "send_notify", "source_id", "visibility", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["full_name"]) -> typing.Union[MetaOapg.properties.full_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["login_name"]) -> typing.Union[MetaOapg.properties.login_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["must_change_password"]) -> typing.Union[MetaOapg.properties.must_change_password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restricted"]) -> typing.Union[MetaOapg.properties.restricted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["send_notify"]) -> typing.Union[MetaOapg.properties.send_notify, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source_id"]) -> typing.Union[MetaOapg.properties.source_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visibility"]) -> typing.Union[MetaOapg.properties.visibility, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email", "password", "username", "created_at", "full_name", "login_name", "must_change_password", "restricted", "send_notify", "source_id", "visibility", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        password: typing.Union[MetaOapg.properties.password, str, ],
        email: typing.Union[MetaOapg.properties.email, str, ],
        username: typing.Union[MetaOapg.properties.username, str, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        full_name: typing.Union[MetaOapg.properties.full_name, str, schemas.Unset] = schemas.unset,
        login_name: typing.Union[MetaOapg.properties.login_name, str, schemas.Unset] = schemas.unset,
        must_change_password: typing.Union[MetaOapg.properties.must_change_password, bool, schemas.Unset] = schemas.unset,
        restricted: typing.Union[MetaOapg.properties.restricted, bool, schemas.Unset] = schemas.unset,
        send_notify: typing.Union[MetaOapg.properties.send_notify, bool, schemas.Unset] = schemas.unset,
        source_id: typing.Union[MetaOapg.properties.source_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        visibility: typing.Union[MetaOapg.properties.visibility, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateUserOption':
        return super().__new__(
            cls,
            *_args,
            password=password,
            email=email,
            username=username,
            created_at=created_at,
            full_name=full_name,
            login_name=login_name,
            must_change_password=must_change_password,
            restricted=restricted,
            send_notify=send_notify,
            source_id=source_id,
            visibility=visibility,
            _configuration=_configuration,
            **kwargs,
        )

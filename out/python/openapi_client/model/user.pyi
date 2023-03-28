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


class User(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    User represents a user
    """


    class MetaOapg:
        
        class properties:
            active = schemas.BoolSchema
            avatar_url = schemas.StrSchema
            created = schemas.DateTimeSchema
            description = schemas.StrSchema
            email = schemas.StrSchema
            followers_count = schemas.Int64Schema
            following_count = schemas.Int64Schema
            full_name = schemas.StrSchema
            id = schemas.Int64Schema
            is_admin = schemas.BoolSchema
            language = schemas.StrSchema
            last_login = schemas.DateTimeSchema
            location = schemas.StrSchema
            login = schemas.StrSchema
            login_name = schemas.StrSchema
            prohibit_login = schemas.BoolSchema
            restricted = schemas.BoolSchema
            starred_repos_count = schemas.Int64Schema
            visibility = schemas.StrSchema
            website = schemas.StrSchema
            __annotations__ = {
                "active": active,
                "avatar_url": avatar_url,
                "created": created,
                "description": description,
                "email": email,
                "followers_count": followers_count,
                "following_count": following_count,
                "full_name": full_name,
                "id": id,
                "is_admin": is_admin,
                "language": language,
                "last_login": last_login,
                "location": location,
                "login": login,
                "login_name": login_name,
                "prohibit_login": prohibit_login,
                "restricted": restricted,
                "starred_repos_count": starred_repos_count,
                "visibility": visibility,
                "website": website,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avatar_url"]) -> MetaOapg.properties.avatar_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["followers_count"]) -> MetaOapg.properties.followers_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["following_count"]) -> MetaOapg.properties.following_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["full_name"]) -> MetaOapg.properties.full_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_admin"]) -> MetaOapg.properties.is_admin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["language"]) -> MetaOapg.properties.language: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_login"]) -> MetaOapg.properties.last_login: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["login"]) -> MetaOapg.properties.login: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["login_name"]) -> MetaOapg.properties.login_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prohibit_login"]) -> MetaOapg.properties.prohibit_login: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restricted"]) -> MetaOapg.properties.restricted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["starred_repos_count"]) -> MetaOapg.properties.starred_repos_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visibility"]) -> MetaOapg.properties.visibility: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["active", "avatar_url", "created", "description", "email", "followers_count", "following_count", "full_name", "id", "is_admin", "language", "last_login", "location", "login", "login_name", "prohibit_login", "restricted", "starred_repos_count", "visibility", "website", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avatar_url"]) -> typing.Union[MetaOapg.properties.avatar_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["followers_count"]) -> typing.Union[MetaOapg.properties.followers_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["following_count"]) -> typing.Union[MetaOapg.properties.following_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["full_name"]) -> typing.Union[MetaOapg.properties.full_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_admin"]) -> typing.Union[MetaOapg.properties.is_admin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["language"]) -> typing.Union[MetaOapg.properties.language, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_login"]) -> typing.Union[MetaOapg.properties.last_login, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> typing.Union[MetaOapg.properties.location, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["login"]) -> typing.Union[MetaOapg.properties.login, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["login_name"]) -> typing.Union[MetaOapg.properties.login_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prohibit_login"]) -> typing.Union[MetaOapg.properties.prohibit_login, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restricted"]) -> typing.Union[MetaOapg.properties.restricted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["starred_repos_count"]) -> typing.Union[MetaOapg.properties.starred_repos_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visibility"]) -> typing.Union[MetaOapg.properties.visibility, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website"]) -> typing.Union[MetaOapg.properties.website, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["active", "avatar_url", "created", "description", "email", "followers_count", "following_count", "full_name", "id", "is_admin", "language", "last_login", "location", "login", "login_name", "prohibit_login", "restricted", "starred_repos_count", "visibility", "website", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        avatar_url: typing.Union[MetaOapg.properties.avatar_url, str, schemas.Unset] = schemas.unset,
        created: typing.Union[MetaOapg.properties.created, str, datetime, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        followers_count: typing.Union[MetaOapg.properties.followers_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        following_count: typing.Union[MetaOapg.properties.following_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        full_name: typing.Union[MetaOapg.properties.full_name, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        is_admin: typing.Union[MetaOapg.properties.is_admin, bool, schemas.Unset] = schemas.unset,
        language: typing.Union[MetaOapg.properties.language, str, schemas.Unset] = schemas.unset,
        last_login: typing.Union[MetaOapg.properties.last_login, str, datetime, schemas.Unset] = schemas.unset,
        location: typing.Union[MetaOapg.properties.location, str, schemas.Unset] = schemas.unset,
        login: typing.Union[MetaOapg.properties.login, str, schemas.Unset] = schemas.unset,
        login_name: typing.Union[MetaOapg.properties.login_name, str, schemas.Unset] = schemas.unset,
        prohibit_login: typing.Union[MetaOapg.properties.prohibit_login, bool, schemas.Unset] = schemas.unset,
        restricted: typing.Union[MetaOapg.properties.restricted, bool, schemas.Unset] = schemas.unset,
        starred_repos_count: typing.Union[MetaOapg.properties.starred_repos_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        visibility: typing.Union[MetaOapg.properties.visibility, str, schemas.Unset] = schemas.unset,
        website: typing.Union[MetaOapg.properties.website, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'User':
        return super().__new__(
            cls,
            *_args,
            active=active,
            avatar_url=avatar_url,
            created=created,
            description=description,
            email=email,
            followers_count=followers_count,
            following_count=following_count,
            full_name=full_name,
            id=id,
            is_admin=is_admin,
            language=language,
            last_login=last_login,
            location=location,
            login=login,
            login_name=login_name,
            prohibit_login=prohibit_login,
            restricted=restricted,
            starred_repos_count=starred_repos_count,
            visibility=visibility,
            website=website,
            _configuration=_configuration,
            **kwargs,
        )
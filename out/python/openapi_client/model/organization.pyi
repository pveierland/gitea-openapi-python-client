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


class Organization(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Organization represents an organization
    """


    class MetaOapg:
        
        class properties:
            avatar_url = schemas.StrSchema
            description = schemas.StrSchema
            full_name = schemas.StrSchema
            id = schemas.Int64Schema
            location = schemas.StrSchema
            name = schemas.StrSchema
            repo_admin_change_team_access = schemas.BoolSchema
            username = schemas.StrSchema
            visibility = schemas.StrSchema
            website = schemas.StrSchema
            __annotations__ = {
                "avatar_url": avatar_url,
                "description": description,
                "full_name": full_name,
                "id": id,
                "location": location,
                "name": name,
                "repo_admin_change_team_access": repo_admin_change_team_access,
                "username": username,
                "visibility": visibility,
                "website": website,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avatar_url"]) -> MetaOapg.properties.avatar_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["full_name"]) -> MetaOapg.properties.full_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["repo_admin_change_team_access"]) -> MetaOapg.properties.repo_admin_change_team_access: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visibility"]) -> MetaOapg.properties.visibility: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["avatar_url", "description", "full_name", "id", "location", "name", "repo_admin_change_team_access", "username", "visibility", "website", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avatar_url"]) -> typing.Union[MetaOapg.properties.avatar_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["full_name"]) -> typing.Union[MetaOapg.properties.full_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> typing.Union[MetaOapg.properties.location, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["repo_admin_change_team_access"]) -> typing.Union[MetaOapg.properties.repo_admin_change_team_access, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visibility"]) -> typing.Union[MetaOapg.properties.visibility, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website"]) -> typing.Union[MetaOapg.properties.website, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["avatar_url", "description", "full_name", "id", "location", "name", "repo_admin_change_team_access", "username", "visibility", "website", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        avatar_url: typing.Union[MetaOapg.properties.avatar_url, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        full_name: typing.Union[MetaOapg.properties.full_name, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        location: typing.Union[MetaOapg.properties.location, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        repo_admin_change_team_access: typing.Union[MetaOapg.properties.repo_admin_change_team_access, bool, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        visibility: typing.Union[MetaOapg.properties.visibility, str, schemas.Unset] = schemas.unset,
        website: typing.Union[MetaOapg.properties.website, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Organization':
        return super().__new__(
            cls,
            *_args,
            avatar_url=avatar_url,
            description=description,
            full_name=full_name,
            id=id,
            location=location,
            name=name,
            repo_admin_change_team_access=repo_admin_change_team_access,
            username=username,
            visibility=visibility,
            website=website,
            _configuration=_configuration,
            **kwargs,
        )

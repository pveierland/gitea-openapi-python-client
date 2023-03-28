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


class Release(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Release represents a repository release
    """


    class MetaOapg:
        
        class properties:
            
            
            class assets(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Attachment']:
                        return Attachment
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Attachment'], typing.List['Attachment']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'assets':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Attachment':
                    return super().__getitem__(i)
        
            @staticmethod
            def author() -> typing.Type['User']:
                return User
            body = schemas.StrSchema
            created_at = schemas.DateTimeSchema
            draft = schemas.BoolSchema
            html_url = schemas.StrSchema
            id = schemas.Int64Schema
            name = schemas.StrSchema
            prerelease = schemas.BoolSchema
            published_at = schemas.DateTimeSchema
            tag_name = schemas.StrSchema
            tarball_url = schemas.StrSchema
            target_commitish = schemas.StrSchema
            url = schemas.StrSchema
            zipball_url = schemas.StrSchema
            __annotations__ = {
                "assets": assets,
                "author": author,
                "body": body,
                "created_at": created_at,
                "draft": draft,
                "html_url": html_url,
                "id": id,
                "name": name,
                "prerelease": prerelease,
                "published_at": published_at,
                "tag_name": tag_name,
                "tarball_url": tarball_url,
                "target_commitish": target_commitish,
                "url": url,
                "zipball_url": zipball_url,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assets"]) -> MetaOapg.properties.assets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["author"]) -> 'User': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["draft"]) -> MetaOapg.properties.draft: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["html_url"]) -> MetaOapg.properties.html_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prerelease"]) -> MetaOapg.properties.prerelease: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["published_at"]) -> MetaOapg.properties.published_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag_name"]) -> MetaOapg.properties.tag_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tarball_url"]) -> MetaOapg.properties.tarball_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target_commitish"]) -> MetaOapg.properties.target_commitish: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zipball_url"]) -> MetaOapg.properties.zipball_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["assets", "author", "body", "created_at", "draft", "html_url", "id", "name", "prerelease", "published_at", "tag_name", "tarball_url", "target_commitish", "url", "zipball_url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assets"]) -> typing.Union[MetaOapg.properties.assets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["author"]) -> typing.Union['User', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["draft"]) -> typing.Union[MetaOapg.properties.draft, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["html_url"]) -> typing.Union[MetaOapg.properties.html_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prerelease"]) -> typing.Union[MetaOapg.properties.prerelease, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["published_at"]) -> typing.Union[MetaOapg.properties.published_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag_name"]) -> typing.Union[MetaOapg.properties.tag_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tarball_url"]) -> typing.Union[MetaOapg.properties.tarball_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target_commitish"]) -> typing.Union[MetaOapg.properties.target_commitish, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zipball_url"]) -> typing.Union[MetaOapg.properties.zipball_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["assets", "author", "body", "created_at", "draft", "html_url", "id", "name", "prerelease", "published_at", "tag_name", "tarball_url", "target_commitish", "url", "zipball_url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        assets: typing.Union[MetaOapg.properties.assets, list, tuple, schemas.Unset] = schemas.unset,
        author: typing.Union['User', schemas.Unset] = schemas.unset,
        body: typing.Union[MetaOapg.properties.body, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        draft: typing.Union[MetaOapg.properties.draft, bool, schemas.Unset] = schemas.unset,
        html_url: typing.Union[MetaOapg.properties.html_url, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        prerelease: typing.Union[MetaOapg.properties.prerelease, bool, schemas.Unset] = schemas.unset,
        published_at: typing.Union[MetaOapg.properties.published_at, str, datetime, schemas.Unset] = schemas.unset,
        tag_name: typing.Union[MetaOapg.properties.tag_name, str, schemas.Unset] = schemas.unset,
        tarball_url: typing.Union[MetaOapg.properties.tarball_url, str, schemas.Unset] = schemas.unset,
        target_commitish: typing.Union[MetaOapg.properties.target_commitish, str, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        zipball_url: typing.Union[MetaOapg.properties.zipball_url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Release':
        return super().__new__(
            cls,
            *_args,
            assets=assets,
            author=author,
            body=body,
            created_at=created_at,
            draft=draft,
            html_url=html_url,
            id=id,
            name=name,
            prerelease=prerelease,
            published_at=published_at,
            tag_name=tag_name,
            tarball_url=tarball_url,
            target_commitish=target_commitish,
            url=url,
            zipball_url=zipball_url,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.attachment import Attachment
from openapi_client.model.user import User
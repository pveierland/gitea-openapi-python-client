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


class WikiPage(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    WikiPage a wiki page
    """


    class MetaOapg:
        
        class properties:
            commit_count = schemas.Int64Schema
            content_base64 = schemas.StrSchema
            footer = schemas.StrSchema
            html_url = schemas.StrSchema
        
            @staticmethod
            def last_commit() -> typing.Type['WikiCommit']:
                return WikiCommit
            sidebar = schemas.StrSchema
            sub_url = schemas.StrSchema
            title = schemas.StrSchema
            __annotations__ = {
                "commit_count": commit_count,
                "content_base64": content_base64,
                "footer": footer,
                "html_url": html_url,
                "last_commit": last_commit,
                "sidebar": sidebar,
                "sub_url": sub_url,
                "title": title,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commit_count"]) -> MetaOapg.properties.commit_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content_base64"]) -> MetaOapg.properties.content_base64: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["footer"]) -> MetaOapg.properties.footer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["html_url"]) -> MetaOapg.properties.html_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_commit"]) -> 'WikiCommit': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sidebar"]) -> MetaOapg.properties.sidebar: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sub_url"]) -> MetaOapg.properties.sub_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["commit_count", "content_base64", "footer", "html_url", "last_commit", "sidebar", "sub_url", "title", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commit_count"]) -> typing.Union[MetaOapg.properties.commit_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content_base64"]) -> typing.Union[MetaOapg.properties.content_base64, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["footer"]) -> typing.Union[MetaOapg.properties.footer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["html_url"]) -> typing.Union[MetaOapg.properties.html_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_commit"]) -> typing.Union['WikiCommit', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sidebar"]) -> typing.Union[MetaOapg.properties.sidebar, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sub_url"]) -> typing.Union[MetaOapg.properties.sub_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["commit_count", "content_base64", "footer", "html_url", "last_commit", "sidebar", "sub_url", "title", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        commit_count: typing.Union[MetaOapg.properties.commit_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        content_base64: typing.Union[MetaOapg.properties.content_base64, str, schemas.Unset] = schemas.unset,
        footer: typing.Union[MetaOapg.properties.footer, str, schemas.Unset] = schemas.unset,
        html_url: typing.Union[MetaOapg.properties.html_url, str, schemas.Unset] = schemas.unset,
        last_commit: typing.Union['WikiCommit', schemas.Unset] = schemas.unset,
        sidebar: typing.Union[MetaOapg.properties.sidebar, str, schemas.Unset] = schemas.unset,
        sub_url: typing.Union[MetaOapg.properties.sub_url, str, schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WikiPage':
        return super().__new__(
            cls,
            *_args,
            commit_count=commit_count,
            content_base64=content_base64,
            footer=footer,
            html_url=html_url,
            last_commit=last_commit,
            sidebar=sidebar,
            sub_url=sub_url,
            title=title,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.wiki_commit import WikiCommit
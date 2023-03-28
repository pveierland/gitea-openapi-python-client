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


class Comment(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Comment represents a comment on a commit or issue
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
            body = schemas.StrSchema
            created_at = schemas.DateTimeSchema
            html_url = schemas.StrSchema
            id = schemas.Int64Schema
            issue_url = schemas.StrSchema
            original_author = schemas.StrSchema
            original_author_id = schemas.Int64Schema
            pull_request_url = schemas.StrSchema
            updated_at = schemas.DateTimeSchema
        
            @staticmethod
            def user() -> typing.Type['User']:
                return User
            __annotations__ = {
                "assets": assets,
                "body": body,
                "created_at": created_at,
                "html_url": html_url,
                "id": id,
                "issue_url": issue_url,
                "original_author": original_author,
                "original_author_id": original_author_id,
                "pull_request_url": pull_request_url,
                "updated_at": updated_at,
                "user": user,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assets"]) -> MetaOapg.properties.assets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["html_url"]) -> MetaOapg.properties.html_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issue_url"]) -> MetaOapg.properties.issue_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["original_author"]) -> MetaOapg.properties.original_author: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["original_author_id"]) -> MetaOapg.properties.original_author_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pull_request_url"]) -> MetaOapg.properties.pull_request_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'User': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["assets", "body", "created_at", "html_url", "id", "issue_url", "original_author", "original_author_id", "pull_request_url", "updated_at", "user", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assets"]) -> typing.Union[MetaOapg.properties.assets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["html_url"]) -> typing.Union[MetaOapg.properties.html_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issue_url"]) -> typing.Union[MetaOapg.properties.issue_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["original_author"]) -> typing.Union[MetaOapg.properties.original_author, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["original_author_id"]) -> typing.Union[MetaOapg.properties.original_author_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pull_request_url"]) -> typing.Union[MetaOapg.properties.pull_request_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union['User', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["assets", "body", "created_at", "html_url", "id", "issue_url", "original_author", "original_author_id", "pull_request_url", "updated_at", "user", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        assets: typing.Union[MetaOapg.properties.assets, list, tuple, schemas.Unset] = schemas.unset,
        body: typing.Union[MetaOapg.properties.body, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        html_url: typing.Union[MetaOapg.properties.html_url, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        issue_url: typing.Union[MetaOapg.properties.issue_url, str, schemas.Unset] = schemas.unset,
        original_author: typing.Union[MetaOapg.properties.original_author, str, schemas.Unset] = schemas.unset,
        original_author_id: typing.Union[MetaOapg.properties.original_author_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pull_request_url: typing.Union[MetaOapg.properties.pull_request_url, str, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        user: typing.Union['User', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Comment':
        return super().__new__(
            cls,
            *_args,
            assets=assets,
            body=body,
            created_at=created_at,
            html_url=html_url,
            id=id,
            issue_url=issue_url,
            original_author=original_author,
            original_author_id=original_author_id,
            pull_request_url=pull_request_url,
            updated_at=updated_at,
            user=user,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.attachment import Attachment
from openapi_client.model.user import User

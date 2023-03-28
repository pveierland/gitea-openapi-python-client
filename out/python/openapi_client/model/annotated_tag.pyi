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


class AnnotatedTag(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    AnnotatedTag represents an annotated tag
    """


    class MetaOapg:
        
        class properties:
            message = schemas.StrSchema
        
            @staticmethod
            def object() -> typing.Type['AnnotatedTagObject']:
                return AnnotatedTagObject
            sha = schemas.StrSchema
            tag = schemas.StrSchema
        
            @staticmethod
            def tagger() -> typing.Type['CommitUser']:
                return CommitUser
            url = schemas.StrSchema
        
            @staticmethod
            def verification() -> typing.Type['PayloadCommitVerification']:
                return PayloadCommitVerification
            __annotations__ = {
                "message": message,
                "object": object,
                "sha": sha,
                "tag": tag,
                "tagger": tagger,
                "url": url,
                "verification": verification,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> 'AnnotatedTagObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sha"]) -> MetaOapg.properties.sha: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag"]) -> MetaOapg.properties.tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tagger"]) -> 'CommitUser': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verification"]) -> 'PayloadCommitVerification': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["message", "object", "sha", "tag", "tagger", "url", "verification", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> typing.Union['AnnotatedTagObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sha"]) -> typing.Union[MetaOapg.properties.sha, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag"]) -> typing.Union[MetaOapg.properties.tag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tagger"]) -> typing.Union['CommitUser', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verification"]) -> typing.Union['PayloadCommitVerification', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message", "object", "sha", "tag", "tagger", "url", "verification", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        object: typing.Union['AnnotatedTagObject', schemas.Unset] = schemas.unset,
        sha: typing.Union[MetaOapg.properties.sha, str, schemas.Unset] = schemas.unset,
        tag: typing.Union[MetaOapg.properties.tag, str, schemas.Unset] = schemas.unset,
        tagger: typing.Union['CommitUser', schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        verification: typing.Union['PayloadCommitVerification', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AnnotatedTag':
        return super().__new__(
            cls,
            *_args,
            message=message,
            object=object,
            sha=sha,
            tag=tag,
            tagger=tagger,
            url=url,
            verification=verification,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.annotated_tag_object import AnnotatedTagObject
from openapi_client.model.commit_user import CommitUser
from openapi_client.model.payload_commit_verification import PayloadCommitVerification

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


class GitTreeResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    GitTreeResponse returns a git tree
    """


    class MetaOapg:
        
        class properties:
            page = schemas.Int64Schema
            sha = schemas.StrSchema
            total_count = schemas.Int64Schema
            
            
            class tree(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['GitEntry']:
                        return GitEntry
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['GitEntry'], typing.List['GitEntry']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tree':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'GitEntry':
                    return super().__getitem__(i)
            truncated = schemas.BoolSchema
            url = schemas.StrSchema
            __annotations__ = {
                "page": page,
                "sha": sha,
                "total_count": total_count,
                "tree": tree,
                "truncated": truncated,
                "url": url,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sha"]) -> MetaOapg.properties.sha: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_count"]) -> MetaOapg.properties.total_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tree"]) -> MetaOapg.properties.tree: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["truncated"]) -> MetaOapg.properties.truncated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["page", "sha", "total_count", "tree", "truncated", "url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> typing.Union[MetaOapg.properties.page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sha"]) -> typing.Union[MetaOapg.properties.sha, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_count"]) -> typing.Union[MetaOapg.properties.total_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tree"]) -> typing.Union[MetaOapg.properties.tree, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["truncated"]) -> typing.Union[MetaOapg.properties.truncated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["page", "sha", "total_count", "tree", "truncated", "url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        page: typing.Union[MetaOapg.properties.page, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sha: typing.Union[MetaOapg.properties.sha, str, schemas.Unset] = schemas.unset,
        total_count: typing.Union[MetaOapg.properties.total_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tree: typing.Union[MetaOapg.properties.tree, list, tuple, schemas.Unset] = schemas.unset,
        truncated: typing.Union[MetaOapg.properties.truncated, bool, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GitTreeResponse':
        return super().__new__(
            cls,
            *_args,
            page=page,
            sha=sha,
            total_count=total_count,
            tree=tree,
            truncated=truncated,
            url=url,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.git_entry import GitEntry

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


class Issue(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Issue represents an issue in a repository
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
            def assignee() -> typing.Type['User']:
                return User
            
            
            class assignees(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['User']:
                        return User
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['User'], typing.List['User']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'assignees':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'User':
                    return super().__getitem__(i)
            body = schemas.StrSchema
            closed_at = schemas.DateTimeSchema
            comments = schemas.Int64Schema
            created_at = schemas.DateTimeSchema
            due_date = schemas.DateTimeSchema
            html_url = schemas.StrSchema
            id = schemas.Int64Schema
            is_locked = schemas.BoolSchema
            
            
            class labels(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Label']:
                        return Label
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Label'], typing.List['Label']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'labels':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Label':
                    return super().__getitem__(i)
        
            @staticmethod
            def milestone() -> typing.Type['Milestone']:
                return Milestone
            number = schemas.Int64Schema
            original_author = schemas.StrSchema
            original_author_id = schemas.Int64Schema
        
            @staticmethod
            def pull_request() -> typing.Type['PullRequestMeta']:
                return PullRequestMeta
            ref = schemas.StrSchema
        
            @staticmethod
            def repository() -> typing.Type['RepositoryMeta']:
                return RepositoryMeta
            state = schemas.StrSchema
            title = schemas.StrSchema
            updated_at = schemas.DateTimeSchema
            url = schemas.StrSchema
        
            @staticmethod
            def user() -> typing.Type['User']:
                return User
            __annotations__ = {
                "assets": assets,
                "assignee": assignee,
                "assignees": assignees,
                "body": body,
                "closed_at": closed_at,
                "comments": comments,
                "created_at": created_at,
                "due_date": due_date,
                "html_url": html_url,
                "id": id,
                "is_locked": is_locked,
                "labels": labels,
                "milestone": milestone,
                "number": number,
                "original_author": original_author,
                "original_author_id": original_author_id,
                "pull_request": pull_request,
                "ref": ref,
                "repository": repository,
                "state": state,
                "title": title,
                "updated_at": updated_at,
                "url": url,
                "user": user,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assets"]) -> MetaOapg.properties.assets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignee"]) -> 'User': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignees"]) -> MetaOapg.properties.assignees: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["closed_at"]) -> MetaOapg.properties.closed_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comments"]) -> MetaOapg.properties.comments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["due_date"]) -> MetaOapg.properties.due_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["html_url"]) -> MetaOapg.properties.html_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_locked"]) -> MetaOapg.properties.is_locked: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labels"]) -> MetaOapg.properties.labels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["milestone"]) -> 'Milestone': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["original_author"]) -> MetaOapg.properties.original_author: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["original_author_id"]) -> MetaOapg.properties.original_author_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pull_request"]) -> 'PullRequestMeta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ref"]) -> MetaOapg.properties.ref: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["repository"]) -> 'RepositoryMeta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'User': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["assets", "assignee", "assignees", "body", "closed_at", "comments", "created_at", "due_date", "html_url", "id", "is_locked", "labels", "milestone", "number", "original_author", "original_author_id", "pull_request", "ref", "repository", "state", "title", "updated_at", "url", "user", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assets"]) -> typing.Union[MetaOapg.properties.assets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignee"]) -> typing.Union['User', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignees"]) -> typing.Union[MetaOapg.properties.assignees, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["closed_at"]) -> typing.Union[MetaOapg.properties.closed_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comments"]) -> typing.Union[MetaOapg.properties.comments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["due_date"]) -> typing.Union[MetaOapg.properties.due_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["html_url"]) -> typing.Union[MetaOapg.properties.html_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_locked"]) -> typing.Union[MetaOapg.properties.is_locked, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["labels"]) -> typing.Union[MetaOapg.properties.labels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["milestone"]) -> typing.Union['Milestone', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> typing.Union[MetaOapg.properties.number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["original_author"]) -> typing.Union[MetaOapg.properties.original_author, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["original_author_id"]) -> typing.Union[MetaOapg.properties.original_author_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pull_request"]) -> typing.Union['PullRequestMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ref"]) -> typing.Union[MetaOapg.properties.ref, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["repository"]) -> typing.Union['RepositoryMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union['User', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["assets", "assignee", "assignees", "body", "closed_at", "comments", "created_at", "due_date", "html_url", "id", "is_locked", "labels", "milestone", "number", "original_author", "original_author_id", "pull_request", "ref", "repository", "state", "title", "updated_at", "url", "user", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        assets: typing.Union[MetaOapg.properties.assets, list, tuple, schemas.Unset] = schemas.unset,
        assignee: typing.Union['User', schemas.Unset] = schemas.unset,
        assignees: typing.Union[MetaOapg.properties.assignees, list, tuple, schemas.Unset] = schemas.unset,
        body: typing.Union[MetaOapg.properties.body, str, schemas.Unset] = schemas.unset,
        closed_at: typing.Union[MetaOapg.properties.closed_at, str, datetime, schemas.Unset] = schemas.unset,
        comments: typing.Union[MetaOapg.properties.comments, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        due_date: typing.Union[MetaOapg.properties.due_date, str, datetime, schemas.Unset] = schemas.unset,
        html_url: typing.Union[MetaOapg.properties.html_url, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        is_locked: typing.Union[MetaOapg.properties.is_locked, bool, schemas.Unset] = schemas.unset,
        labels: typing.Union[MetaOapg.properties.labels, list, tuple, schemas.Unset] = schemas.unset,
        milestone: typing.Union['Milestone', schemas.Unset] = schemas.unset,
        number: typing.Union[MetaOapg.properties.number, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        original_author: typing.Union[MetaOapg.properties.original_author, str, schemas.Unset] = schemas.unset,
        original_author_id: typing.Union[MetaOapg.properties.original_author_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pull_request: typing.Union['PullRequestMeta', schemas.Unset] = schemas.unset,
        ref: typing.Union[MetaOapg.properties.ref, str, schemas.Unset] = schemas.unset,
        repository: typing.Union['RepositoryMeta', schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        user: typing.Union['User', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Issue':
        return super().__new__(
            cls,
            *_args,
            assets=assets,
            assignee=assignee,
            assignees=assignees,
            body=body,
            closed_at=closed_at,
            comments=comments,
            created_at=created_at,
            due_date=due_date,
            html_url=html_url,
            id=id,
            is_locked=is_locked,
            labels=labels,
            milestone=milestone,
            number=number,
            original_author=original_author,
            original_author_id=original_author_id,
            pull_request=pull_request,
            ref=ref,
            repository=repository,
            state=state,
            title=title,
            updated_at=updated_at,
            url=url,
            user=user,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.attachment import Attachment
from openapi_client.model.label import Label
from openapi_client.model.milestone import Milestone
from openapi_client.model.pull_request_meta import PullRequestMeta
from openapi_client.model.repository_meta import RepositoryMeta
from openapi_client.model.user import User

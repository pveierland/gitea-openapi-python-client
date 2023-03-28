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


class EditPullRequestOption(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    EditPullRequestOption options when modify pull request
    """


    class MetaOapg:
        
        class properties:
            allow_maintainer_edit = schemas.BoolSchema
            assignee = schemas.StrSchema
            
            
            class assignees(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'assignees':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            base = schemas.StrSchema
            body = schemas.StrSchema
            due_date = schemas.DateTimeSchema
            
            
            class labels(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.Int64Schema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'labels':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            milestone = schemas.Int64Schema
            state = schemas.StrSchema
            title = schemas.StrSchema
            unset_due_date = schemas.BoolSchema
            __annotations__ = {
                "allow_maintainer_edit": allow_maintainer_edit,
                "assignee": assignee,
                "assignees": assignees,
                "base": base,
                "body": body,
                "due_date": due_date,
                "labels": labels,
                "milestone": milestone,
                "state": state,
                "title": title,
                "unset_due_date": unset_due_date,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_maintainer_edit"]) -> MetaOapg.properties.allow_maintainer_edit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignee"]) -> MetaOapg.properties.assignee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignees"]) -> MetaOapg.properties.assignees: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["base"]) -> MetaOapg.properties.base: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["due_date"]) -> MetaOapg.properties.due_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labels"]) -> MetaOapg.properties.labels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["milestone"]) -> MetaOapg.properties.milestone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unset_due_date"]) -> MetaOapg.properties.unset_due_date: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["allow_maintainer_edit", "assignee", "assignees", "base", "body", "due_date", "labels", "milestone", "state", "title", "unset_due_date", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_maintainer_edit"]) -> typing.Union[MetaOapg.properties.allow_maintainer_edit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignee"]) -> typing.Union[MetaOapg.properties.assignee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignees"]) -> typing.Union[MetaOapg.properties.assignees, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["base"]) -> typing.Union[MetaOapg.properties.base, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> typing.Union[MetaOapg.properties.body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["due_date"]) -> typing.Union[MetaOapg.properties.due_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["labels"]) -> typing.Union[MetaOapg.properties.labels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["milestone"]) -> typing.Union[MetaOapg.properties.milestone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unset_due_date"]) -> typing.Union[MetaOapg.properties.unset_due_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["allow_maintainer_edit", "assignee", "assignees", "base", "body", "due_date", "labels", "milestone", "state", "title", "unset_due_date", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        allow_maintainer_edit: typing.Union[MetaOapg.properties.allow_maintainer_edit, bool, schemas.Unset] = schemas.unset,
        assignee: typing.Union[MetaOapg.properties.assignee, str, schemas.Unset] = schemas.unset,
        assignees: typing.Union[MetaOapg.properties.assignees, list, tuple, schemas.Unset] = schemas.unset,
        base: typing.Union[MetaOapg.properties.base, str, schemas.Unset] = schemas.unset,
        body: typing.Union[MetaOapg.properties.body, str, schemas.Unset] = schemas.unset,
        due_date: typing.Union[MetaOapg.properties.due_date, str, datetime, schemas.Unset] = schemas.unset,
        labels: typing.Union[MetaOapg.properties.labels, list, tuple, schemas.Unset] = schemas.unset,
        milestone: typing.Union[MetaOapg.properties.milestone, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        unset_due_date: typing.Union[MetaOapg.properties.unset_due_date, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EditPullRequestOption':
        return super().__new__(
            cls,
            *_args,
            allow_maintainer_edit=allow_maintainer_edit,
            assignee=assignee,
            assignees=assignees,
            base=base,
            body=body,
            due_date=due_date,
            labels=labels,
            milestone=milestone,
            state=state,
            title=title,
            unset_due_date=unset_due_date,
            _configuration=_configuration,
            **kwargs,
        )
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


class EditRepoOption(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    EditRepoOption options when editing a repository's properties
    """


    class MetaOapg:
        
        class properties:
            allow_manual_merge = schemas.BoolSchema
            allow_merge_commits = schemas.BoolSchema
            allow_rebase = schemas.BoolSchema
            allow_rebase_explicit = schemas.BoolSchema
            allow_rebase_update = schemas.BoolSchema
            allow_squash_merge = schemas.BoolSchema
            archived = schemas.BoolSchema
            autodetect_manual_merge = schemas.BoolSchema
            default_allow_maintainer_edit = schemas.BoolSchema
            default_branch = schemas.StrSchema
            default_delete_branch_after_merge = schemas.BoolSchema
            default_merge_style = schemas.StrSchema
            description = schemas.StrSchema
            enable_prune = schemas.BoolSchema
        
            @staticmethod
            def external_tracker() -> typing.Type['ExternalTracker']:
                return ExternalTracker
        
            @staticmethod
            def external_wiki() -> typing.Type['ExternalWiki']:
                return ExternalWiki
            has_issues = schemas.BoolSchema
            has_projects = schemas.BoolSchema
            has_pull_requests = schemas.BoolSchema
            has_wiki = schemas.BoolSchema
            ignore_whitespace_conflicts = schemas.BoolSchema
        
            @staticmethod
            def internal_tracker() -> typing.Type['InternalTracker']:
                return InternalTracker
            mirror_interval = schemas.StrSchema
            name = schemas.StrSchema
            private = schemas.BoolSchema
            template = schemas.BoolSchema
            website = schemas.StrSchema
            __annotations__ = {
                "allow_manual_merge": allow_manual_merge,
                "allow_merge_commits": allow_merge_commits,
                "allow_rebase": allow_rebase,
                "allow_rebase_explicit": allow_rebase_explicit,
                "allow_rebase_update": allow_rebase_update,
                "allow_squash_merge": allow_squash_merge,
                "archived": archived,
                "autodetect_manual_merge": autodetect_manual_merge,
                "default_allow_maintainer_edit": default_allow_maintainer_edit,
                "default_branch": default_branch,
                "default_delete_branch_after_merge": default_delete_branch_after_merge,
                "default_merge_style": default_merge_style,
                "description": description,
                "enable_prune": enable_prune,
                "external_tracker": external_tracker,
                "external_wiki": external_wiki,
                "has_issues": has_issues,
                "has_projects": has_projects,
                "has_pull_requests": has_pull_requests,
                "has_wiki": has_wiki,
                "ignore_whitespace_conflicts": ignore_whitespace_conflicts,
                "internal_tracker": internal_tracker,
                "mirror_interval": mirror_interval,
                "name": name,
                "private": private,
                "template": template,
                "website": website,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_manual_merge"]) -> MetaOapg.properties.allow_manual_merge: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_merge_commits"]) -> MetaOapg.properties.allow_merge_commits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_rebase"]) -> MetaOapg.properties.allow_rebase: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_rebase_explicit"]) -> MetaOapg.properties.allow_rebase_explicit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_rebase_update"]) -> MetaOapg.properties.allow_rebase_update: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_squash_merge"]) -> MetaOapg.properties.allow_squash_merge: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["archived"]) -> MetaOapg.properties.archived: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autodetect_manual_merge"]) -> MetaOapg.properties.autodetect_manual_merge: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_allow_maintainer_edit"]) -> MetaOapg.properties.default_allow_maintainer_edit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_branch"]) -> MetaOapg.properties.default_branch: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_delete_branch_after_merge"]) -> MetaOapg.properties.default_delete_branch_after_merge: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_merge_style"]) -> MetaOapg.properties.default_merge_style: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_prune"]) -> MetaOapg.properties.enable_prune: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_tracker"]) -> 'ExternalTracker': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_wiki"]) -> 'ExternalWiki': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_issues"]) -> MetaOapg.properties.has_issues: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_projects"]) -> MetaOapg.properties.has_projects: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_pull_requests"]) -> MetaOapg.properties.has_pull_requests: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_wiki"]) -> MetaOapg.properties.has_wiki: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ignore_whitespace_conflicts"]) -> MetaOapg.properties.ignore_whitespace_conflicts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["internal_tracker"]) -> 'InternalTracker': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mirror_interval"]) -> MetaOapg.properties.mirror_interval: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["private"]) -> MetaOapg.properties.private: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["template"]) -> MetaOapg.properties.template: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["allow_manual_merge", "allow_merge_commits", "allow_rebase", "allow_rebase_explicit", "allow_rebase_update", "allow_squash_merge", "archived", "autodetect_manual_merge", "default_allow_maintainer_edit", "default_branch", "default_delete_branch_after_merge", "default_merge_style", "description", "enable_prune", "external_tracker", "external_wiki", "has_issues", "has_projects", "has_pull_requests", "has_wiki", "ignore_whitespace_conflicts", "internal_tracker", "mirror_interval", "name", "private", "template", "website", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_manual_merge"]) -> typing.Union[MetaOapg.properties.allow_manual_merge, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_merge_commits"]) -> typing.Union[MetaOapg.properties.allow_merge_commits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_rebase"]) -> typing.Union[MetaOapg.properties.allow_rebase, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_rebase_explicit"]) -> typing.Union[MetaOapg.properties.allow_rebase_explicit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_rebase_update"]) -> typing.Union[MetaOapg.properties.allow_rebase_update, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_squash_merge"]) -> typing.Union[MetaOapg.properties.allow_squash_merge, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["archived"]) -> typing.Union[MetaOapg.properties.archived, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autodetect_manual_merge"]) -> typing.Union[MetaOapg.properties.autodetect_manual_merge, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_allow_maintainer_edit"]) -> typing.Union[MetaOapg.properties.default_allow_maintainer_edit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_branch"]) -> typing.Union[MetaOapg.properties.default_branch, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_delete_branch_after_merge"]) -> typing.Union[MetaOapg.properties.default_delete_branch_after_merge, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_merge_style"]) -> typing.Union[MetaOapg.properties.default_merge_style, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_prune"]) -> typing.Union[MetaOapg.properties.enable_prune, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_tracker"]) -> typing.Union['ExternalTracker', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_wiki"]) -> typing.Union['ExternalWiki', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_issues"]) -> typing.Union[MetaOapg.properties.has_issues, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_projects"]) -> typing.Union[MetaOapg.properties.has_projects, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_pull_requests"]) -> typing.Union[MetaOapg.properties.has_pull_requests, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_wiki"]) -> typing.Union[MetaOapg.properties.has_wiki, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ignore_whitespace_conflicts"]) -> typing.Union[MetaOapg.properties.ignore_whitespace_conflicts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["internal_tracker"]) -> typing.Union['InternalTracker', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mirror_interval"]) -> typing.Union[MetaOapg.properties.mirror_interval, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["private"]) -> typing.Union[MetaOapg.properties.private, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["template"]) -> typing.Union[MetaOapg.properties.template, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website"]) -> typing.Union[MetaOapg.properties.website, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["allow_manual_merge", "allow_merge_commits", "allow_rebase", "allow_rebase_explicit", "allow_rebase_update", "allow_squash_merge", "archived", "autodetect_manual_merge", "default_allow_maintainer_edit", "default_branch", "default_delete_branch_after_merge", "default_merge_style", "description", "enable_prune", "external_tracker", "external_wiki", "has_issues", "has_projects", "has_pull_requests", "has_wiki", "ignore_whitespace_conflicts", "internal_tracker", "mirror_interval", "name", "private", "template", "website", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        allow_manual_merge: typing.Union[MetaOapg.properties.allow_manual_merge, bool, schemas.Unset] = schemas.unset,
        allow_merge_commits: typing.Union[MetaOapg.properties.allow_merge_commits, bool, schemas.Unset] = schemas.unset,
        allow_rebase: typing.Union[MetaOapg.properties.allow_rebase, bool, schemas.Unset] = schemas.unset,
        allow_rebase_explicit: typing.Union[MetaOapg.properties.allow_rebase_explicit, bool, schemas.Unset] = schemas.unset,
        allow_rebase_update: typing.Union[MetaOapg.properties.allow_rebase_update, bool, schemas.Unset] = schemas.unset,
        allow_squash_merge: typing.Union[MetaOapg.properties.allow_squash_merge, bool, schemas.Unset] = schemas.unset,
        archived: typing.Union[MetaOapg.properties.archived, bool, schemas.Unset] = schemas.unset,
        autodetect_manual_merge: typing.Union[MetaOapg.properties.autodetect_manual_merge, bool, schemas.Unset] = schemas.unset,
        default_allow_maintainer_edit: typing.Union[MetaOapg.properties.default_allow_maintainer_edit, bool, schemas.Unset] = schemas.unset,
        default_branch: typing.Union[MetaOapg.properties.default_branch, str, schemas.Unset] = schemas.unset,
        default_delete_branch_after_merge: typing.Union[MetaOapg.properties.default_delete_branch_after_merge, bool, schemas.Unset] = schemas.unset,
        default_merge_style: typing.Union[MetaOapg.properties.default_merge_style, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        enable_prune: typing.Union[MetaOapg.properties.enable_prune, bool, schemas.Unset] = schemas.unset,
        external_tracker: typing.Union['ExternalTracker', schemas.Unset] = schemas.unset,
        external_wiki: typing.Union['ExternalWiki', schemas.Unset] = schemas.unset,
        has_issues: typing.Union[MetaOapg.properties.has_issues, bool, schemas.Unset] = schemas.unset,
        has_projects: typing.Union[MetaOapg.properties.has_projects, bool, schemas.Unset] = schemas.unset,
        has_pull_requests: typing.Union[MetaOapg.properties.has_pull_requests, bool, schemas.Unset] = schemas.unset,
        has_wiki: typing.Union[MetaOapg.properties.has_wiki, bool, schemas.Unset] = schemas.unset,
        ignore_whitespace_conflicts: typing.Union[MetaOapg.properties.ignore_whitespace_conflicts, bool, schemas.Unset] = schemas.unset,
        internal_tracker: typing.Union['InternalTracker', schemas.Unset] = schemas.unset,
        mirror_interval: typing.Union[MetaOapg.properties.mirror_interval, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        private: typing.Union[MetaOapg.properties.private, bool, schemas.Unset] = schemas.unset,
        template: typing.Union[MetaOapg.properties.template, bool, schemas.Unset] = schemas.unset,
        website: typing.Union[MetaOapg.properties.website, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EditRepoOption':
        return super().__new__(
            cls,
            *_args,
            allow_manual_merge=allow_manual_merge,
            allow_merge_commits=allow_merge_commits,
            allow_rebase=allow_rebase,
            allow_rebase_explicit=allow_rebase_explicit,
            allow_rebase_update=allow_rebase_update,
            allow_squash_merge=allow_squash_merge,
            archived=archived,
            autodetect_manual_merge=autodetect_manual_merge,
            default_allow_maintainer_edit=default_allow_maintainer_edit,
            default_branch=default_branch,
            default_delete_branch_after_merge=default_delete_branch_after_merge,
            default_merge_style=default_merge_style,
            description=description,
            enable_prune=enable_prune,
            external_tracker=external_tracker,
            external_wiki=external_wiki,
            has_issues=has_issues,
            has_projects=has_projects,
            has_pull_requests=has_pull_requests,
            has_wiki=has_wiki,
            ignore_whitespace_conflicts=ignore_whitespace_conflicts,
            internal_tracker=internal_tracker,
            mirror_interval=mirror_interval,
            name=name,
            private=private,
            template=template,
            website=website,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.external_tracker import ExternalTracker
from openapi_client.model.external_wiki import ExternalWiki
from openapi_client.model.internal_tracker import InternalTracker
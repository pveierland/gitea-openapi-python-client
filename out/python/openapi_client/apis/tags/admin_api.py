# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.0
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.admin_unadopted_owner_repo.post import AdminAdoptRepository
from openapi_client.paths.admin_hooks.post import AdminCreateHook
from openapi_client.paths.admin_users_username_orgs.post import AdminCreateOrg
from openapi_client.paths.admin_users_username_keys.post import AdminCreatePublicKey
from openapi_client.paths.admin_users_username_repos.post import AdminCreateRepo
from openapi_client.paths.admin_users.post import AdminCreateUser
from openapi_client.paths.admin_cron.get import AdminCronList
from openapi_client.paths.admin_cron_task.post import AdminCronRun
from openapi_client.paths.amdin_hooks_id.delete import AdminDeleteHook
from openapi_client.paths.admin_unadopted_owner_repo.delete import AdminDeleteUnadoptedRepository
from openapi_client.paths.admin_users_username.delete import AdminDeleteUser
from openapi_client.paths.admin_users_username_keys_id.delete import AdminDeleteUserPublicKey
from openapi_client.paths.admin_hooks_id.patch import AdminEditHook
from openapi_client.paths.admin_users_username.patch import AdminEditUser
from openapi_client.paths.admin_orgs.get import AdminGetAllOrgs
from openapi_client.paths.admin_users.get import AdminGetAllUsers
from openapi_client.paths.admin_hooks_id.get import AdminGetHook
from openapi_client.paths.admin_hooks.get import AdminListHooks
from openapi_client.paths.admin_unadopted.get import AdminUnadoptedList


class AdminApi(
    AdminAdoptRepository,
    AdminCreateHook,
    AdminCreateOrg,
    AdminCreatePublicKey,
    AdminCreateRepo,
    AdminCreateUser,
    AdminCronList,
    AdminCronRun,
    AdminDeleteHook,
    AdminDeleteUnadoptedRepository,
    AdminDeleteUser,
    AdminDeleteUserPublicKey,
    AdminEditHook,
    AdminEditUser,
    AdminGetAllOrgs,
    AdminGetAllUsers,
    AdminGetHook,
    AdminListHooks,
    AdminUnadoptedList,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass

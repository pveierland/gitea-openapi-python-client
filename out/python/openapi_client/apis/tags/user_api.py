# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.0
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.user_repos.post import CreateCurrentUserRepo
from openapi_client.paths.user_settings.get import GetUserSettings
from openapi_client.paths.user_gpg_key_token.get import GetVerificationToken
from openapi_client.paths.user_settings.patch import UpdateUserSettings
from openapi_client.paths.user_emails.post import UserAddEmail
from openapi_client.paths.users_username_following_target.get import UserCheckFollowing
from openapi_client.paths.user_applications_oauth2.post import UserCreateOAuth2Application
from openapi_client.paths.users_username_tokens.post import UserCreateToken
from openapi_client.paths.user_following_username.get import UserCurrentCheckFollowing
from openapi_client.paths.user_starred_owner_repo.get import UserCurrentCheckStarring
from openapi_client.paths.user_following_username.delete import UserCurrentDeleteFollow
from openapi_client.paths.user_gpg_keys_id.delete import UserCurrentDeleteGpgKey
from openapi_client.paths.user_keys_id.delete import UserCurrentDeleteKey
from openapi_client.paths.user_starred_owner_repo.delete import UserCurrentDeleteStar
from openapi_client.paths.user_gpg_keys_id.get import UserCurrentGetGpgKey
from openapi_client.paths.user_keys_id.get import UserCurrentGetKey
from openapi_client.paths.user_followers.get import UserCurrentListFollowers
from openapi_client.paths.user_following.get import UserCurrentListFollowing
from openapi_client.paths.user_gpg_keys.get import UserCurrentListGpgKeys
from openapi_client.paths.user_keys.get import UserCurrentListKeys
from openapi_client.paths.user_repos.get import UserCurrentListRepos
from openapi_client.paths.user_starred.get import UserCurrentListStarred
from openapi_client.paths.user_subscriptions.get import UserCurrentListSubscriptions
from openapi_client.paths.user_gpg_keys.post import UserCurrentPostGpgKey
from openapi_client.paths.user_keys.post import UserCurrentPostKey
from openapi_client.paths.user_following_username.put import UserCurrentPutFollow
from openapi_client.paths.user_starred_owner_repo.put import UserCurrentPutStar
from openapi_client.paths.user_times.get import UserCurrentTrackedTimes
from openapi_client.paths.users_username_tokens_token.delete import UserDeleteAccessToken
from openapi_client.paths.user_emails.delete import UserDeleteEmail
from openapi_client.paths.user_applications_oauth2_id.delete import UserDeleteOAuth2Application
from openapi_client.paths.users_username.get import UserGet
from openapi_client.paths.user.get import UserGetCurrent
from openapi_client.paths.users_username_heatmap.get import UserGetHeatmapData
from openapi_client.paths.user_applications_oauth2_id.get import UserGetOAuth2Application
from openapi_client.paths.user_applications_oauth2.get import UserGetOauth2Application
from openapi_client.paths.user_stopwatches.get import UserGetStopWatches
from openapi_client.paths.users_username_tokens.get import UserGetTokens
from openapi_client.paths.user_emails.get import UserListEmails
from openapi_client.paths.users_username_followers.get import UserListFollowers
from openapi_client.paths.users_username_following.get import UserListFollowing
from openapi_client.paths.users_username_gpg_keys.get import UserListGpgKeys
from openapi_client.paths.users_username_keys.get import UserListKeys
from openapi_client.paths.users_username_repos.get import UserListRepos
from openapi_client.paths.users_username_starred.get import UserListStarred
from openapi_client.paths.users_username_subscriptions.get import UserListSubscriptions
from openapi_client.paths.user_teams.get import UserListTeams
from openapi_client.paths.users_search.get import UserSearch
from openapi_client.paths.user_applications_oauth2_id.patch import UserUpdateOAuth2Application
from openapi_client.paths.user_gpg_key_verify.post import UserVerifyGpgKey


class UserApi(
    CreateCurrentUserRepo,
    GetUserSettings,
    GetVerificationToken,
    UpdateUserSettings,
    UserAddEmail,
    UserCheckFollowing,
    UserCreateOAuth2Application,
    UserCreateToken,
    UserCurrentCheckFollowing,
    UserCurrentCheckStarring,
    UserCurrentDeleteFollow,
    UserCurrentDeleteGpgKey,
    UserCurrentDeleteKey,
    UserCurrentDeleteStar,
    UserCurrentGetGpgKey,
    UserCurrentGetKey,
    UserCurrentListFollowers,
    UserCurrentListFollowing,
    UserCurrentListGpgKeys,
    UserCurrentListKeys,
    UserCurrentListRepos,
    UserCurrentListStarred,
    UserCurrentListSubscriptions,
    UserCurrentPostGpgKey,
    UserCurrentPostKey,
    UserCurrentPutFollow,
    UserCurrentPutStar,
    UserCurrentTrackedTimes,
    UserDeleteAccessToken,
    UserDeleteEmail,
    UserDeleteOAuth2Application,
    UserGet,
    UserGetCurrent,
    UserGetHeatmapData,
    UserGetOAuth2Application,
    UserGetOauth2Application,
    UserGetStopWatches,
    UserGetTokens,
    UserListEmails,
    UserListFollowers,
    UserListFollowing,
    UserListGpgKeys,
    UserListKeys,
    UserListRepos,
    UserListStarred,
    UserListSubscriptions,
    UserListTeams,
    UserSearch,
    UserUpdateOAuth2Application,
    UserVerifyGpgKey,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
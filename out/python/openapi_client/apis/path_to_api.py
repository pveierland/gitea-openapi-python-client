import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.activitypub_user_username import ActivitypubUserUsername
from openapi_client.apis.paths.activitypub_user_username_inbox import ActivitypubUserUsernameInbox
from openapi_client.apis.paths.admin_cron import AdminCron
from openapi_client.apis.paths.admin_cron_task import AdminCronTask
from openapi_client.apis.paths.admin_hooks import AdminHooks
from openapi_client.apis.paths.admin_hooks_id import AdminHooksId
from openapi_client.apis.paths.admin_orgs import AdminOrgs
from openapi_client.apis.paths.admin_unadopted import AdminUnadopted
from openapi_client.apis.paths.admin_unadopted_owner_repo import AdminUnadoptedOwnerRepo
from openapi_client.apis.paths.admin_users import AdminUsers
from openapi_client.apis.paths.admin_users_username import AdminUsersUsername
from openapi_client.apis.paths.admin_users_username_keys import AdminUsersUsernameKeys
from openapi_client.apis.paths.admin_users_username_keys_id import AdminUsersUsernameKeysId
from openapi_client.apis.paths.admin_users_username_orgs import AdminUsersUsernameOrgs
from openapi_client.apis.paths.admin_users_username_repos import AdminUsersUsernameRepos
from openapi_client.apis.paths.amdin_hooks_id import AmdinHooksId
from openapi_client.apis.paths.markdown import Markdown
from openapi_client.apis.paths.markdown_raw import MarkdownRaw
from openapi_client.apis.paths.nodeinfo import Nodeinfo
from openapi_client.apis.paths.notifications import Notifications
from openapi_client.apis.paths.notifications_new import NotificationsNew
from openapi_client.apis.paths.notifications_threads_id import NotificationsThreadsId
from openapi_client.apis.paths.org_org_repos import OrgOrgRepos
from openapi_client.apis.paths.orgs import Orgs
from openapi_client.apis.paths.orgs_org import OrgsOrg
from openapi_client.apis.paths.orgs_org_hooks import OrgsOrgHooks
from openapi_client.apis.paths.orgs_org_hooks_id import OrgsOrgHooksId
from openapi_client.apis.paths.orgs_org_labels import OrgsOrgLabels
from openapi_client.apis.paths.orgs_org_labels_id import OrgsOrgLabelsId
from openapi_client.apis.paths.orgs_org_members import OrgsOrgMembers
from openapi_client.apis.paths.orgs_org_members_username import OrgsOrgMembersUsername
from openapi_client.apis.paths.orgs_org_public_members import OrgsOrgPublicMembers
from openapi_client.apis.paths.orgs_org_public_members_username import OrgsOrgPublicMembersUsername
from openapi_client.apis.paths.orgs_org_repos import OrgsOrgRepos
from openapi_client.apis.paths.orgs_org_teams import OrgsOrgTeams
from openapi_client.apis.paths.orgs_org_teams_search import OrgsOrgTeamsSearch
from openapi_client.apis.paths.packages_owner import PackagesOwner
from openapi_client.apis.paths.packages_owner_type_name_version import PackagesOwnerTypeNameVersion
from openapi_client.apis.paths.packages_owner_type_name_version_files import PackagesOwnerTypeNameVersionFiles
from openapi_client.apis.paths.repos_issues_search import ReposIssuesSearch
from openapi_client.apis.paths.repos_migrate import ReposMigrate
from openapi_client.apis.paths.repos_search import ReposSearch
from openapi_client.apis.paths.repos_owner_repo import ReposOwnerRepo
from openapi_client.apis.paths.repos_owner_repo_archive_archive import ReposOwnerRepoArchiveArchive
from openapi_client.apis.paths.repos_owner_repo_assignees import ReposOwnerRepoAssignees
from openapi_client.apis.paths.repos_owner_repo_branch_protections import ReposOwnerRepoBranchProtections
from openapi_client.apis.paths.repos_owner_repo_branch_protections_name import ReposOwnerRepoBranchProtectionsName
from openapi_client.apis.paths.repos_owner_repo_branches import ReposOwnerRepoBranches
from openapi_client.apis.paths.repos_owner_repo_branches_branch import ReposOwnerRepoBranchesBranch
from openapi_client.apis.paths.repos_owner_repo_collaborators import ReposOwnerRepoCollaborators
from openapi_client.apis.paths.repos_owner_repo_collaborators_collaborator import ReposOwnerRepoCollaboratorsCollaborator
from openapi_client.apis.paths.repos_owner_repo_collaborators_collaborator_permission import ReposOwnerRepoCollaboratorsCollaboratorPermission
from openapi_client.apis.paths.repos_owner_repo_commits import ReposOwnerRepoCommits
from openapi_client.apis.paths.repos_owner_repo_commits_ref_status import ReposOwnerRepoCommitsRefStatus
from openapi_client.apis.paths.repos_owner_repo_commits_ref_statuses import ReposOwnerRepoCommitsRefStatuses
from openapi_client.apis.paths.repos_owner_repo_contents import ReposOwnerRepoContents
from openapi_client.apis.paths.repos_owner_repo_contents_filepath import ReposOwnerRepoContentsFilepath
from openapi_client.apis.paths.repos_owner_repo_diffpatch import ReposOwnerRepoDiffpatch
from openapi_client.apis.paths.repos_owner_repo_editorconfig_filepath import ReposOwnerRepoEditorconfigFilepath
from openapi_client.apis.paths.repos_owner_repo_forks import ReposOwnerRepoForks
from openapi_client.apis.paths.repos_owner_repo_git_blobs_sha import ReposOwnerRepoGitBlobsSha
from openapi_client.apis.paths.repos_owner_repo_git_commits_sha import ReposOwnerRepoGitCommitsSha
from openapi_client.apis.paths.repos_owner_repo_git_commits_sha_diff_type import ReposOwnerRepoGitCommitsShaDiffType
from openapi_client.apis.paths.repos_owner_repo_git_notes_sha import ReposOwnerRepoGitNotesSha
from openapi_client.apis.paths.repos_owner_repo_git_refs import ReposOwnerRepoGitRefs
from openapi_client.apis.paths.repos_owner_repo_git_refs_ref import ReposOwnerRepoGitRefsRef
from openapi_client.apis.paths.repos_owner_repo_git_tags_sha import ReposOwnerRepoGitTagsSha
from openapi_client.apis.paths.repos_owner_repo_git_trees_sha import ReposOwnerRepoGitTreesSha
from openapi_client.apis.paths.repos_owner_repo_hooks import ReposOwnerRepoHooks
from openapi_client.apis.paths.repos_owner_repo_hooks_git import ReposOwnerRepoHooksGit
from openapi_client.apis.paths.repos_owner_repo_hooks_git_id import ReposOwnerRepoHooksGitId
from openapi_client.apis.paths.repos_owner_repo_hooks_id import ReposOwnerRepoHooksId
from openapi_client.apis.paths.repos_owner_repo_hooks_id_tests import ReposOwnerRepoHooksIdTests
from openapi_client.apis.paths.repos_owner_repo_issue_templates import ReposOwnerRepoIssueTemplates
from openapi_client.apis.paths.repos_owner_repo_issues import ReposOwnerRepoIssues
from openapi_client.apis.paths.repos_owner_repo_issues_comments import ReposOwnerRepoIssuesComments
from openapi_client.apis.paths.repos_owner_repo_issues_comments_id import ReposOwnerRepoIssuesCommentsId
from openapi_client.apis.paths.repos_owner_repo_issues_comments_id_assets import ReposOwnerRepoIssuesCommentsIdAssets
from openapi_client.apis.paths.repos_owner_repo_issues_comments_id_assets_attachment_id import ReposOwnerRepoIssuesCommentsIdAssetsAttachmentId
from openapi_client.apis.paths.repos_owner_repo_issues_comments_id_reactions import ReposOwnerRepoIssuesCommentsIdReactions
from openapi_client.apis.paths.repos_owner_repo_issues_index import ReposOwnerRepoIssuesIndex
from openapi_client.apis.paths.repos_owner_repo_issues_index_assets import ReposOwnerRepoIssuesIndexAssets
from openapi_client.apis.paths.repos_owner_repo_issues_index_assets_attachment_id import ReposOwnerRepoIssuesIndexAssetsAttachmentId
from openapi_client.apis.paths.repos_owner_repo_issues_index_comments import ReposOwnerRepoIssuesIndexComments
from openapi_client.apis.paths.repos_owner_repo_issues_index_comments_id import ReposOwnerRepoIssuesIndexCommentsId
from openapi_client.apis.paths.repos_owner_repo_issues_index_deadline import ReposOwnerRepoIssuesIndexDeadline
from openapi_client.apis.paths.repos_owner_repo_issues_index_labels import ReposOwnerRepoIssuesIndexLabels
from openapi_client.apis.paths.repos_owner_repo_issues_index_labels_id import ReposOwnerRepoIssuesIndexLabelsId
from openapi_client.apis.paths.repos_owner_repo_issues_index_reactions import ReposOwnerRepoIssuesIndexReactions
from openapi_client.apis.paths.repos_owner_repo_issues_index_stopwatch_delete import ReposOwnerRepoIssuesIndexStopwatchDelete
from openapi_client.apis.paths.repos_owner_repo_issues_index_stopwatch_start import ReposOwnerRepoIssuesIndexStopwatchStart
from openapi_client.apis.paths.repos_owner_repo_issues_index_stopwatch_stop import ReposOwnerRepoIssuesIndexStopwatchStop
from openapi_client.apis.paths.repos_owner_repo_issues_index_subscriptions import ReposOwnerRepoIssuesIndexSubscriptions
from openapi_client.apis.paths.repos_owner_repo_issues_index_subscriptions_check import ReposOwnerRepoIssuesIndexSubscriptionsCheck
from openapi_client.apis.paths.repos_owner_repo_issues_index_subscriptions_user import ReposOwnerRepoIssuesIndexSubscriptionsUser
from openapi_client.apis.paths.repos_owner_repo_issues_index_timeline import ReposOwnerRepoIssuesIndexTimeline
from openapi_client.apis.paths.repos_owner_repo_issues_index_times import ReposOwnerRepoIssuesIndexTimes
from openapi_client.apis.paths.repos_owner_repo_issues_index_times_id import ReposOwnerRepoIssuesIndexTimesId
from openapi_client.apis.paths.repos_owner_repo_keys import ReposOwnerRepoKeys
from openapi_client.apis.paths.repos_owner_repo_keys_id import ReposOwnerRepoKeysId
from openapi_client.apis.paths.repos_owner_repo_labels import ReposOwnerRepoLabels
from openapi_client.apis.paths.repos_owner_repo_labels_id import ReposOwnerRepoLabelsId
from openapi_client.apis.paths.repos_owner_repo_languages import ReposOwnerRepoLanguages
from openapi_client.apis.paths.repos_owner_repo_media_filepath import ReposOwnerRepoMediaFilepath
from openapi_client.apis.paths.repos_owner_repo_milestones import ReposOwnerRepoMilestones
from openapi_client.apis.paths.repos_owner_repo_milestones_id import ReposOwnerRepoMilestonesId
from openapi_client.apis.paths.repos_owner_repo_mirror_sync import ReposOwnerRepoMirrorSync
from openapi_client.apis.paths.repos_owner_repo_notifications import ReposOwnerRepoNotifications
from openapi_client.apis.paths.repos_owner_repo_pulls import ReposOwnerRepoPulls
from openapi_client.apis.paths.repos_owner_repo_pulls_index import ReposOwnerRepoPullsIndex
from openapi_client.apis.paths.repos_owner_repo_pulls_index_diff_type import ReposOwnerRepoPullsIndexDiffType
from openapi_client.apis.paths.repos_owner_repo_pulls_index_commits import ReposOwnerRepoPullsIndexCommits
from openapi_client.apis.paths.repos_owner_repo_pulls_index_files import ReposOwnerRepoPullsIndexFiles
from openapi_client.apis.paths.repos_owner_repo_pulls_index_merge import ReposOwnerRepoPullsIndexMerge
from openapi_client.apis.paths.repos_owner_repo_pulls_index_requested_reviewers import ReposOwnerRepoPullsIndexRequestedReviewers
from openapi_client.apis.paths.repos_owner_repo_pulls_index_reviews import ReposOwnerRepoPullsIndexReviews
from openapi_client.apis.paths.repos_owner_repo_pulls_index_reviews_id import ReposOwnerRepoPullsIndexReviewsId
from openapi_client.apis.paths.repos_owner_repo_pulls_index_reviews_id_comments import ReposOwnerRepoPullsIndexReviewsIdComments
from openapi_client.apis.paths.repos_owner_repo_pulls_index_reviews_id_dismissals import ReposOwnerRepoPullsIndexReviewsIdDismissals
from openapi_client.apis.paths.repos_owner_repo_pulls_index_reviews_id_undismissals import ReposOwnerRepoPullsIndexReviewsIdUndismissals
from openapi_client.apis.paths.repos_owner_repo_pulls_index_update import ReposOwnerRepoPullsIndexUpdate
from openapi_client.apis.paths.repos_owner_repo_push_mirrors import ReposOwnerRepoPushMirrors
from openapi_client.apis.paths.repos_owner_repo_push_mirrors_sync import ReposOwnerRepoPushMirrorsSync
from openapi_client.apis.paths.repos_owner_repo_push_mirrors_name import ReposOwnerRepoPushMirrorsName
from openapi_client.apis.paths.repos_owner_repo_raw_filepath import ReposOwnerRepoRawFilepath
from openapi_client.apis.paths.repos_owner_repo_releases import ReposOwnerRepoReleases
from openapi_client.apis.paths.repos_owner_repo_releases_latest import ReposOwnerRepoReleasesLatest
from openapi_client.apis.paths.repos_owner_repo_releases_tags_tag import ReposOwnerRepoReleasesTagsTag
from openapi_client.apis.paths.repos_owner_repo_releases_id import ReposOwnerRepoReleasesId
from openapi_client.apis.paths.repos_owner_repo_releases_id_assets import ReposOwnerRepoReleasesIdAssets
from openapi_client.apis.paths.repos_owner_repo_releases_id_assets_attachment_id import ReposOwnerRepoReleasesIdAssetsAttachmentId
from openapi_client.apis.paths.repos_owner_repo_reviewers import ReposOwnerRepoReviewers
from openapi_client.apis.paths.repos_owner_repo_signing_key_gpg import ReposOwnerRepoSigningKeyGpg
from openapi_client.apis.paths.repos_owner_repo_stargazers import ReposOwnerRepoStargazers
from openapi_client.apis.paths.repos_owner_repo_statuses_sha import ReposOwnerRepoStatusesSha
from openapi_client.apis.paths.repos_owner_repo_subscribers import ReposOwnerRepoSubscribers
from openapi_client.apis.paths.repos_owner_repo_subscription import ReposOwnerRepoSubscription
from openapi_client.apis.paths.repos_owner_repo_tags import ReposOwnerRepoTags
from openapi_client.apis.paths.repos_owner_repo_tags_tag import ReposOwnerRepoTagsTag
from openapi_client.apis.paths.repos_owner_repo_teams import ReposOwnerRepoTeams
from openapi_client.apis.paths.repos_owner_repo_teams_team import ReposOwnerRepoTeamsTeam
from openapi_client.apis.paths.repos_owner_repo_times import ReposOwnerRepoTimes
from openapi_client.apis.paths.repos_owner_repo_times_user import ReposOwnerRepoTimesUser
from openapi_client.apis.paths.repos_owner_repo_topics import ReposOwnerRepoTopics
from openapi_client.apis.paths.repos_owner_repo_topics_topic import ReposOwnerRepoTopicsTopic
from openapi_client.apis.paths.repos_owner_repo_transfer import ReposOwnerRepoTransfer
from openapi_client.apis.paths.repos_owner_repo_transfer_accept import ReposOwnerRepoTransferAccept
from openapi_client.apis.paths.repos_owner_repo_transfer_reject import ReposOwnerRepoTransferReject
from openapi_client.apis.paths.repos_owner_repo_wiki_new import ReposOwnerRepoWikiNew
from openapi_client.apis.paths.repos_owner_repo_wiki_page_page_name import ReposOwnerRepoWikiPagePageName
from openapi_client.apis.paths.repos_owner_repo_wiki_pages import ReposOwnerRepoWikiPages
from openapi_client.apis.paths.repos_owner_repo_wiki_revisions_page_name import ReposOwnerRepoWikiRevisionsPageName
from openapi_client.apis.paths.repos_template_owner_template_repo_generate import ReposTemplateOwnerTemplateRepoGenerate
from openapi_client.apis.paths.repositories_id import RepositoriesId
from openapi_client.apis.paths.settings_api import SettingsApi
from openapi_client.apis.paths.settings_attachment import SettingsAttachment
from openapi_client.apis.paths.settings_repository import SettingsRepository
from openapi_client.apis.paths.settings_ui import SettingsUi
from openapi_client.apis.paths.signing_key_gpg import SigningKeyGpg
from openapi_client.apis.paths.teams_id import TeamsId
from openapi_client.apis.paths.teams_id_members import TeamsIdMembers
from openapi_client.apis.paths.teams_id_members_username import TeamsIdMembersUsername
from openapi_client.apis.paths.teams_id_repos import TeamsIdRepos
from openapi_client.apis.paths.teams_id_repos_org_repo import TeamsIdReposOrgRepo
from openapi_client.apis.paths.topics_search import TopicsSearch
from openapi_client.apis.paths.user import User
from openapi_client.apis.paths.user_applications_oauth2 import UserApplicationsOauth2
from openapi_client.apis.paths.user_applications_oauth2_id import UserApplicationsOauth2Id
from openapi_client.apis.paths.user_emails import UserEmails
from openapi_client.apis.paths.user_followers import UserFollowers
from openapi_client.apis.paths.user_following import UserFollowing
from openapi_client.apis.paths.user_following_username import UserFollowingUsername
from openapi_client.apis.paths.user_gpg_key_token import UserGpgKeyToken
from openapi_client.apis.paths.user_gpg_key_verify import UserGpgKeyVerify
from openapi_client.apis.paths.user_gpg_keys import UserGpgKeys
from openapi_client.apis.paths.user_gpg_keys_id import UserGpgKeysId
from openapi_client.apis.paths.user_keys import UserKeys
from openapi_client.apis.paths.user_keys_id import UserKeysId
from openapi_client.apis.paths.user_orgs import UserOrgs
from openapi_client.apis.paths.user_repos import UserRepos
from openapi_client.apis.paths.user_settings import UserSettings
from openapi_client.apis.paths.user_starred import UserStarred
from openapi_client.apis.paths.user_starred_owner_repo import UserStarredOwnerRepo
from openapi_client.apis.paths.user_stopwatches import UserStopwatches
from openapi_client.apis.paths.user_subscriptions import UserSubscriptions
from openapi_client.apis.paths.user_teams import UserTeams
from openapi_client.apis.paths.user_times import UserTimes
from openapi_client.apis.paths.users_search import UsersSearch
from openapi_client.apis.paths.users_username import UsersUsername
from openapi_client.apis.paths.users_username_followers import UsersUsernameFollowers
from openapi_client.apis.paths.users_username_following import UsersUsernameFollowing
from openapi_client.apis.paths.users_username_following_target import UsersUsernameFollowingTarget
from openapi_client.apis.paths.users_username_gpg_keys import UsersUsernameGpgKeys
from openapi_client.apis.paths.users_username_heatmap import UsersUsernameHeatmap
from openapi_client.apis.paths.users_username_keys import UsersUsernameKeys
from openapi_client.apis.paths.users_username_orgs import UsersUsernameOrgs
from openapi_client.apis.paths.users_username_orgs_org_permissions import UsersUsernameOrgsOrgPermissions
from openapi_client.apis.paths.users_username_repos import UsersUsernameRepos
from openapi_client.apis.paths.users_username_starred import UsersUsernameStarred
from openapi_client.apis.paths.users_username_subscriptions import UsersUsernameSubscriptions
from openapi_client.apis.paths.users_username_tokens import UsersUsernameTokens
from openapi_client.apis.paths.users_username_tokens_token import UsersUsernameTokensToken
from openapi_client.apis.paths.version import Version

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACTIVITYPUB_USER_USERNAME: ActivitypubUserUsername,
        PathValues.ACTIVITYPUB_USER_USERNAME_INBOX: ActivitypubUserUsernameInbox,
        PathValues.ADMIN_CRON: AdminCron,
        PathValues.ADMIN_CRON_TASK: AdminCronTask,
        PathValues.ADMIN_HOOKS: AdminHooks,
        PathValues.ADMIN_HOOKS_ID: AdminHooksId,
        PathValues.ADMIN_ORGS: AdminOrgs,
        PathValues.ADMIN_UNADOPTED: AdminUnadopted,
        PathValues.ADMIN_UNADOPTED_OWNER_REPO: AdminUnadoptedOwnerRepo,
        PathValues.ADMIN_USERS: AdminUsers,
        PathValues.ADMIN_USERS_USERNAME: AdminUsersUsername,
        PathValues.ADMIN_USERS_USERNAME_KEYS: AdminUsersUsernameKeys,
        PathValues.ADMIN_USERS_USERNAME_KEYS_ID: AdminUsersUsernameKeysId,
        PathValues.ADMIN_USERS_USERNAME_ORGS: AdminUsersUsernameOrgs,
        PathValues.ADMIN_USERS_USERNAME_REPOS: AdminUsersUsernameRepos,
        PathValues.AMDIN_HOOKS_ID: AmdinHooksId,
        PathValues.MARKDOWN: Markdown,
        PathValues.MARKDOWN_RAW: MarkdownRaw,
        PathValues.NODEINFO: Nodeinfo,
        PathValues.NOTIFICATIONS: Notifications,
        PathValues.NOTIFICATIONS_NEW: NotificationsNew,
        PathValues.NOTIFICATIONS_THREADS_ID: NotificationsThreadsId,
        PathValues.ORG_ORG_REPOS: OrgOrgRepos,
        PathValues.ORGS: Orgs,
        PathValues.ORGS_ORG: OrgsOrg,
        PathValues.ORGS_ORG_HOOKS: OrgsOrgHooks,
        PathValues.ORGS_ORG_HOOKS_ID: OrgsOrgHooksId,
        PathValues.ORGS_ORG_LABELS: OrgsOrgLabels,
        PathValues.ORGS_ORG_LABELS_ID: OrgsOrgLabelsId,
        PathValues.ORGS_ORG_MEMBERS: OrgsOrgMembers,
        PathValues.ORGS_ORG_MEMBERS_USERNAME: OrgsOrgMembersUsername,
        PathValues.ORGS_ORG_PUBLIC_MEMBERS: OrgsOrgPublicMembers,
        PathValues.ORGS_ORG_PUBLIC_MEMBERS_USERNAME: OrgsOrgPublicMembersUsername,
        PathValues.ORGS_ORG_REPOS: OrgsOrgRepos,
        PathValues.ORGS_ORG_TEAMS: OrgsOrgTeams,
        PathValues.ORGS_ORG_TEAMS_SEARCH: OrgsOrgTeamsSearch,
        PathValues.PACKAGES_OWNER: PackagesOwner,
        PathValues.PACKAGES_OWNER_TYPE_NAME_VERSION: PackagesOwnerTypeNameVersion,
        PathValues.PACKAGES_OWNER_TYPE_NAME_VERSION_FILES: PackagesOwnerTypeNameVersionFiles,
        PathValues.REPOS_ISSUES_SEARCH: ReposIssuesSearch,
        PathValues.REPOS_MIGRATE: ReposMigrate,
        PathValues.REPOS_SEARCH: ReposSearch,
        PathValues.REPOS_OWNER_REPO: ReposOwnerRepo,
        PathValues.REPOS_OWNER_REPO_ARCHIVE_ARCHIVE: ReposOwnerRepoArchiveArchive,
        PathValues.REPOS_OWNER_REPO_ASSIGNEES: ReposOwnerRepoAssignees,
        PathValues.REPOS_OWNER_REPO_BRANCH_PROTECTIONS: ReposOwnerRepoBranchProtections,
        PathValues.REPOS_OWNER_REPO_BRANCH_PROTECTIONS_NAME: ReposOwnerRepoBranchProtectionsName,
        PathValues.REPOS_OWNER_REPO_BRANCHES: ReposOwnerRepoBranches,
        PathValues.REPOS_OWNER_REPO_BRANCHES_BRANCH: ReposOwnerRepoBranchesBranch,
        PathValues.REPOS_OWNER_REPO_COLLABORATORS: ReposOwnerRepoCollaborators,
        PathValues.REPOS_OWNER_REPO_COLLABORATORS_COLLABORATOR: ReposOwnerRepoCollaboratorsCollaborator,
        PathValues.REPOS_OWNER_REPO_COLLABORATORS_COLLABORATOR_PERMISSION: ReposOwnerRepoCollaboratorsCollaboratorPermission,
        PathValues.REPOS_OWNER_REPO_COMMITS: ReposOwnerRepoCommits,
        PathValues.REPOS_OWNER_REPO_COMMITS_REF_STATUS: ReposOwnerRepoCommitsRefStatus,
        PathValues.REPOS_OWNER_REPO_COMMITS_REF_STATUSES: ReposOwnerRepoCommitsRefStatuses,
        PathValues.REPOS_OWNER_REPO_CONTENTS: ReposOwnerRepoContents,
        PathValues.REPOS_OWNER_REPO_CONTENTS_FILEPATH: ReposOwnerRepoContentsFilepath,
        PathValues.REPOS_OWNER_REPO_DIFFPATCH: ReposOwnerRepoDiffpatch,
        PathValues.REPOS_OWNER_REPO_EDITORCONFIG_FILEPATH: ReposOwnerRepoEditorconfigFilepath,
        PathValues.REPOS_OWNER_REPO_FORKS: ReposOwnerRepoForks,
        PathValues.REPOS_OWNER_REPO_GIT_BLOBS_SHA: ReposOwnerRepoGitBlobsSha,
        PathValues.REPOS_OWNER_REPO_GIT_COMMITS_SHA: ReposOwnerRepoGitCommitsSha,
        PathValues.REPOS_OWNER_REPO_GIT_COMMITS_SHA_DIFF_TYPE: ReposOwnerRepoGitCommitsShaDiffType,
        PathValues.REPOS_OWNER_REPO_GIT_NOTES_SHA: ReposOwnerRepoGitNotesSha,
        PathValues.REPOS_OWNER_REPO_GIT_REFS: ReposOwnerRepoGitRefs,
        PathValues.REPOS_OWNER_REPO_GIT_REFS_REF: ReposOwnerRepoGitRefsRef,
        PathValues.REPOS_OWNER_REPO_GIT_TAGS_SHA: ReposOwnerRepoGitTagsSha,
        PathValues.REPOS_OWNER_REPO_GIT_TREES_SHA: ReposOwnerRepoGitTreesSha,
        PathValues.REPOS_OWNER_REPO_HOOKS: ReposOwnerRepoHooks,
        PathValues.REPOS_OWNER_REPO_HOOKS_GIT: ReposOwnerRepoHooksGit,
        PathValues.REPOS_OWNER_REPO_HOOKS_GIT_ID: ReposOwnerRepoHooksGitId,
        PathValues.REPOS_OWNER_REPO_HOOKS_ID: ReposOwnerRepoHooksId,
        PathValues.REPOS_OWNER_REPO_HOOKS_ID_TESTS: ReposOwnerRepoHooksIdTests,
        PathValues.REPOS_OWNER_REPO_ISSUE_TEMPLATES: ReposOwnerRepoIssueTemplates,
        PathValues.REPOS_OWNER_REPO_ISSUES: ReposOwnerRepoIssues,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS: ReposOwnerRepoIssuesComments,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS_ID: ReposOwnerRepoIssuesCommentsId,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS_ID_ASSETS: ReposOwnerRepoIssuesCommentsIdAssets,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS_ID_ASSETS_ATTACHMENT_ID: ReposOwnerRepoIssuesCommentsIdAssetsAttachmentId,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS_ID_REACTIONS: ReposOwnerRepoIssuesCommentsIdReactions,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX: ReposOwnerRepoIssuesIndex,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_ASSETS: ReposOwnerRepoIssuesIndexAssets,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_ASSETS_ATTACHMENT_ID: ReposOwnerRepoIssuesIndexAssetsAttachmentId,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_COMMENTS: ReposOwnerRepoIssuesIndexComments,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_COMMENTS_ID: ReposOwnerRepoIssuesIndexCommentsId,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_DEADLINE: ReposOwnerRepoIssuesIndexDeadline,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_LABELS: ReposOwnerRepoIssuesIndexLabels,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_LABELS_ID: ReposOwnerRepoIssuesIndexLabelsId,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_REACTIONS: ReposOwnerRepoIssuesIndexReactions,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_STOPWATCH_DELETE: ReposOwnerRepoIssuesIndexStopwatchDelete,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_STOPWATCH_START: ReposOwnerRepoIssuesIndexStopwatchStart,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_STOPWATCH_STOP: ReposOwnerRepoIssuesIndexStopwatchStop,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_SUBSCRIPTIONS: ReposOwnerRepoIssuesIndexSubscriptions,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_SUBSCRIPTIONS_CHECK: ReposOwnerRepoIssuesIndexSubscriptionsCheck,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_SUBSCRIPTIONS_USER: ReposOwnerRepoIssuesIndexSubscriptionsUser,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_TIMELINE: ReposOwnerRepoIssuesIndexTimeline,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_TIMES: ReposOwnerRepoIssuesIndexTimes,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_TIMES_ID: ReposOwnerRepoIssuesIndexTimesId,
        PathValues.REPOS_OWNER_REPO_KEYS: ReposOwnerRepoKeys,
        PathValues.REPOS_OWNER_REPO_KEYS_ID: ReposOwnerRepoKeysId,
        PathValues.REPOS_OWNER_REPO_LABELS: ReposOwnerRepoLabels,
        PathValues.REPOS_OWNER_REPO_LABELS_ID: ReposOwnerRepoLabelsId,
        PathValues.REPOS_OWNER_REPO_LANGUAGES: ReposOwnerRepoLanguages,
        PathValues.REPOS_OWNER_REPO_MEDIA_FILEPATH: ReposOwnerRepoMediaFilepath,
        PathValues.REPOS_OWNER_REPO_MILESTONES: ReposOwnerRepoMilestones,
        PathValues.REPOS_OWNER_REPO_MILESTONES_ID: ReposOwnerRepoMilestonesId,
        PathValues.REPOS_OWNER_REPO_MIRRORSYNC: ReposOwnerRepoMirrorSync,
        PathValues.REPOS_OWNER_REPO_NOTIFICATIONS: ReposOwnerRepoNotifications,
        PathValues.REPOS_OWNER_REPO_PULLS: ReposOwnerRepoPulls,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX: ReposOwnerRepoPullsIndex,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_DIFF_TYPE: ReposOwnerRepoPullsIndexDiffType,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_COMMITS: ReposOwnerRepoPullsIndexCommits,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_FILES: ReposOwnerRepoPullsIndexFiles,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_MERGE: ReposOwnerRepoPullsIndexMerge,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REQUESTED_REVIEWERS: ReposOwnerRepoPullsIndexRequestedReviewers,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS: ReposOwnerRepoPullsIndexReviews,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS_ID: ReposOwnerRepoPullsIndexReviewsId,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS_ID_COMMENTS: ReposOwnerRepoPullsIndexReviewsIdComments,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS_ID_DISMISSALS: ReposOwnerRepoPullsIndexReviewsIdDismissals,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS_ID_UNDISMISSALS: ReposOwnerRepoPullsIndexReviewsIdUndismissals,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_UPDATE: ReposOwnerRepoPullsIndexUpdate,
        PathValues.REPOS_OWNER_REPO_PUSH_MIRRORS: ReposOwnerRepoPushMirrors,
        PathValues.REPOS_OWNER_REPO_PUSH_MIRRORSSYNC: ReposOwnerRepoPushMirrorsSync,
        PathValues.REPOS_OWNER_REPO_PUSH_MIRRORS_NAME: ReposOwnerRepoPushMirrorsName,
        PathValues.REPOS_OWNER_REPO_RAW_FILEPATH: ReposOwnerRepoRawFilepath,
        PathValues.REPOS_OWNER_REPO_RELEASES: ReposOwnerRepoReleases,
        PathValues.REPOS_OWNER_REPO_RELEASES_LATEST: ReposOwnerRepoReleasesLatest,
        PathValues.REPOS_OWNER_REPO_RELEASES_TAGS_TAG: ReposOwnerRepoReleasesTagsTag,
        PathValues.REPOS_OWNER_REPO_RELEASES_ID: ReposOwnerRepoReleasesId,
        PathValues.REPOS_OWNER_REPO_RELEASES_ID_ASSETS: ReposOwnerRepoReleasesIdAssets,
        PathValues.REPOS_OWNER_REPO_RELEASES_ID_ASSETS_ATTACHMENT_ID: ReposOwnerRepoReleasesIdAssetsAttachmentId,
        PathValues.REPOS_OWNER_REPO_REVIEWERS: ReposOwnerRepoReviewers,
        PathValues.REPOS_OWNER_REPO_SIGNINGKEY_GPG: ReposOwnerRepoSigningKeyGpg,
        PathValues.REPOS_OWNER_REPO_STARGAZERS: ReposOwnerRepoStargazers,
        PathValues.REPOS_OWNER_REPO_STATUSES_SHA: ReposOwnerRepoStatusesSha,
        PathValues.REPOS_OWNER_REPO_SUBSCRIBERS: ReposOwnerRepoSubscribers,
        PathValues.REPOS_OWNER_REPO_SUBSCRIPTION: ReposOwnerRepoSubscription,
        PathValues.REPOS_OWNER_REPO_TAGS: ReposOwnerRepoTags,
        PathValues.REPOS_OWNER_REPO_TAGS_TAG: ReposOwnerRepoTagsTag,
        PathValues.REPOS_OWNER_REPO_TEAMS: ReposOwnerRepoTeams,
        PathValues.REPOS_OWNER_REPO_TEAMS_TEAM: ReposOwnerRepoTeamsTeam,
        PathValues.REPOS_OWNER_REPO_TIMES: ReposOwnerRepoTimes,
        PathValues.REPOS_OWNER_REPO_TIMES_USER: ReposOwnerRepoTimesUser,
        PathValues.REPOS_OWNER_REPO_TOPICS: ReposOwnerRepoTopics,
        PathValues.REPOS_OWNER_REPO_TOPICS_TOPIC: ReposOwnerRepoTopicsTopic,
        PathValues.REPOS_OWNER_REPO_TRANSFER: ReposOwnerRepoTransfer,
        PathValues.REPOS_OWNER_REPO_TRANSFER_ACCEPT: ReposOwnerRepoTransferAccept,
        PathValues.REPOS_OWNER_REPO_TRANSFER_REJECT: ReposOwnerRepoTransferReject,
        PathValues.REPOS_OWNER_REPO_WIKI_NEW: ReposOwnerRepoWikiNew,
        PathValues.REPOS_OWNER_REPO_WIKI_PAGE_PAGE_NAME: ReposOwnerRepoWikiPagePageName,
        PathValues.REPOS_OWNER_REPO_WIKI_PAGES: ReposOwnerRepoWikiPages,
        PathValues.REPOS_OWNER_REPO_WIKI_REVISIONS_PAGE_NAME: ReposOwnerRepoWikiRevisionsPageName,
        PathValues.REPOS_TEMPLATE_OWNER_TEMPLATE_REPO_GENERATE: ReposTemplateOwnerTemplateRepoGenerate,
        PathValues.REPOSITORIES_ID: RepositoriesId,
        PathValues.SETTINGS_API: SettingsApi,
        PathValues.SETTINGS_ATTACHMENT: SettingsAttachment,
        PathValues.SETTINGS_REPOSITORY: SettingsRepository,
        PathValues.SETTINGS_UI: SettingsUi,
        PathValues.SIGNINGKEY_GPG: SigningKeyGpg,
        PathValues.TEAMS_ID: TeamsId,
        PathValues.TEAMS_ID_MEMBERS: TeamsIdMembers,
        PathValues.TEAMS_ID_MEMBERS_USERNAME: TeamsIdMembersUsername,
        PathValues.TEAMS_ID_REPOS: TeamsIdRepos,
        PathValues.TEAMS_ID_REPOS_ORG_REPO: TeamsIdReposOrgRepo,
        PathValues.TOPICS_SEARCH: TopicsSearch,
        PathValues.USER: User,
        PathValues.USER_APPLICATIONS_OAUTH2: UserApplicationsOauth2,
        PathValues.USER_APPLICATIONS_OAUTH2_ID: UserApplicationsOauth2Id,
        PathValues.USER_EMAILS: UserEmails,
        PathValues.USER_FOLLOWERS: UserFollowers,
        PathValues.USER_FOLLOWING: UserFollowing,
        PathValues.USER_FOLLOWING_USERNAME: UserFollowingUsername,
        PathValues.USER_GPG_KEY_TOKEN: UserGpgKeyToken,
        PathValues.USER_GPG_KEY_VERIFY: UserGpgKeyVerify,
        PathValues.USER_GPG_KEYS: UserGpgKeys,
        PathValues.USER_GPG_KEYS_ID: UserGpgKeysId,
        PathValues.USER_KEYS: UserKeys,
        PathValues.USER_KEYS_ID: UserKeysId,
        PathValues.USER_ORGS: UserOrgs,
        PathValues.USER_REPOS: UserRepos,
        PathValues.USER_SETTINGS: UserSettings,
        PathValues.USER_STARRED: UserStarred,
        PathValues.USER_STARRED_OWNER_REPO: UserStarredOwnerRepo,
        PathValues.USER_STOPWATCHES: UserStopwatches,
        PathValues.USER_SUBSCRIPTIONS: UserSubscriptions,
        PathValues.USER_TEAMS: UserTeams,
        PathValues.USER_TIMES: UserTimes,
        PathValues.USERS_SEARCH: UsersSearch,
        PathValues.USERS_USERNAME: UsersUsername,
        PathValues.USERS_USERNAME_FOLLOWERS: UsersUsernameFollowers,
        PathValues.USERS_USERNAME_FOLLOWING: UsersUsernameFollowing,
        PathValues.USERS_USERNAME_FOLLOWING_TARGET: UsersUsernameFollowingTarget,
        PathValues.USERS_USERNAME_GPG_KEYS: UsersUsernameGpgKeys,
        PathValues.USERS_USERNAME_HEATMAP: UsersUsernameHeatmap,
        PathValues.USERS_USERNAME_KEYS: UsersUsernameKeys,
        PathValues.USERS_USERNAME_ORGS: UsersUsernameOrgs,
        PathValues.USERS_USERNAME_ORGS_ORG_PERMISSIONS: UsersUsernameOrgsOrgPermissions,
        PathValues.USERS_USERNAME_REPOS: UsersUsernameRepos,
        PathValues.USERS_USERNAME_STARRED: UsersUsernameStarred,
        PathValues.USERS_USERNAME_SUBSCRIPTIONS: UsersUsernameSubscriptions,
        PathValues.USERS_USERNAME_TOKENS: UsersUsernameTokens,
        PathValues.USERS_USERNAME_TOKENS_TOKEN: UsersUsernameTokensToken,
        PathValues.VERSION: Version,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACTIVITYPUB_USER_USERNAME: ActivitypubUserUsername,
        PathValues.ACTIVITYPUB_USER_USERNAME_INBOX: ActivitypubUserUsernameInbox,
        PathValues.ADMIN_CRON: AdminCron,
        PathValues.ADMIN_CRON_TASK: AdminCronTask,
        PathValues.ADMIN_HOOKS: AdminHooks,
        PathValues.ADMIN_HOOKS_ID: AdminHooksId,
        PathValues.ADMIN_ORGS: AdminOrgs,
        PathValues.ADMIN_UNADOPTED: AdminUnadopted,
        PathValues.ADMIN_UNADOPTED_OWNER_REPO: AdminUnadoptedOwnerRepo,
        PathValues.ADMIN_USERS: AdminUsers,
        PathValues.ADMIN_USERS_USERNAME: AdminUsersUsername,
        PathValues.ADMIN_USERS_USERNAME_KEYS: AdminUsersUsernameKeys,
        PathValues.ADMIN_USERS_USERNAME_KEYS_ID: AdminUsersUsernameKeysId,
        PathValues.ADMIN_USERS_USERNAME_ORGS: AdminUsersUsernameOrgs,
        PathValues.ADMIN_USERS_USERNAME_REPOS: AdminUsersUsernameRepos,
        PathValues.AMDIN_HOOKS_ID: AmdinHooksId,
        PathValues.MARKDOWN: Markdown,
        PathValues.MARKDOWN_RAW: MarkdownRaw,
        PathValues.NODEINFO: Nodeinfo,
        PathValues.NOTIFICATIONS: Notifications,
        PathValues.NOTIFICATIONS_NEW: NotificationsNew,
        PathValues.NOTIFICATIONS_THREADS_ID: NotificationsThreadsId,
        PathValues.ORG_ORG_REPOS: OrgOrgRepos,
        PathValues.ORGS: Orgs,
        PathValues.ORGS_ORG: OrgsOrg,
        PathValues.ORGS_ORG_HOOKS: OrgsOrgHooks,
        PathValues.ORGS_ORG_HOOKS_ID: OrgsOrgHooksId,
        PathValues.ORGS_ORG_LABELS: OrgsOrgLabels,
        PathValues.ORGS_ORG_LABELS_ID: OrgsOrgLabelsId,
        PathValues.ORGS_ORG_MEMBERS: OrgsOrgMembers,
        PathValues.ORGS_ORG_MEMBERS_USERNAME: OrgsOrgMembersUsername,
        PathValues.ORGS_ORG_PUBLIC_MEMBERS: OrgsOrgPublicMembers,
        PathValues.ORGS_ORG_PUBLIC_MEMBERS_USERNAME: OrgsOrgPublicMembersUsername,
        PathValues.ORGS_ORG_REPOS: OrgsOrgRepos,
        PathValues.ORGS_ORG_TEAMS: OrgsOrgTeams,
        PathValues.ORGS_ORG_TEAMS_SEARCH: OrgsOrgTeamsSearch,
        PathValues.PACKAGES_OWNER: PackagesOwner,
        PathValues.PACKAGES_OWNER_TYPE_NAME_VERSION: PackagesOwnerTypeNameVersion,
        PathValues.PACKAGES_OWNER_TYPE_NAME_VERSION_FILES: PackagesOwnerTypeNameVersionFiles,
        PathValues.REPOS_ISSUES_SEARCH: ReposIssuesSearch,
        PathValues.REPOS_MIGRATE: ReposMigrate,
        PathValues.REPOS_SEARCH: ReposSearch,
        PathValues.REPOS_OWNER_REPO: ReposOwnerRepo,
        PathValues.REPOS_OWNER_REPO_ARCHIVE_ARCHIVE: ReposOwnerRepoArchiveArchive,
        PathValues.REPOS_OWNER_REPO_ASSIGNEES: ReposOwnerRepoAssignees,
        PathValues.REPOS_OWNER_REPO_BRANCH_PROTECTIONS: ReposOwnerRepoBranchProtections,
        PathValues.REPOS_OWNER_REPO_BRANCH_PROTECTIONS_NAME: ReposOwnerRepoBranchProtectionsName,
        PathValues.REPOS_OWNER_REPO_BRANCHES: ReposOwnerRepoBranches,
        PathValues.REPOS_OWNER_REPO_BRANCHES_BRANCH: ReposOwnerRepoBranchesBranch,
        PathValues.REPOS_OWNER_REPO_COLLABORATORS: ReposOwnerRepoCollaborators,
        PathValues.REPOS_OWNER_REPO_COLLABORATORS_COLLABORATOR: ReposOwnerRepoCollaboratorsCollaborator,
        PathValues.REPOS_OWNER_REPO_COLLABORATORS_COLLABORATOR_PERMISSION: ReposOwnerRepoCollaboratorsCollaboratorPermission,
        PathValues.REPOS_OWNER_REPO_COMMITS: ReposOwnerRepoCommits,
        PathValues.REPOS_OWNER_REPO_COMMITS_REF_STATUS: ReposOwnerRepoCommitsRefStatus,
        PathValues.REPOS_OWNER_REPO_COMMITS_REF_STATUSES: ReposOwnerRepoCommitsRefStatuses,
        PathValues.REPOS_OWNER_REPO_CONTENTS: ReposOwnerRepoContents,
        PathValues.REPOS_OWNER_REPO_CONTENTS_FILEPATH: ReposOwnerRepoContentsFilepath,
        PathValues.REPOS_OWNER_REPO_DIFFPATCH: ReposOwnerRepoDiffpatch,
        PathValues.REPOS_OWNER_REPO_EDITORCONFIG_FILEPATH: ReposOwnerRepoEditorconfigFilepath,
        PathValues.REPOS_OWNER_REPO_FORKS: ReposOwnerRepoForks,
        PathValues.REPOS_OWNER_REPO_GIT_BLOBS_SHA: ReposOwnerRepoGitBlobsSha,
        PathValues.REPOS_OWNER_REPO_GIT_COMMITS_SHA: ReposOwnerRepoGitCommitsSha,
        PathValues.REPOS_OWNER_REPO_GIT_COMMITS_SHA_DIFF_TYPE: ReposOwnerRepoGitCommitsShaDiffType,
        PathValues.REPOS_OWNER_REPO_GIT_NOTES_SHA: ReposOwnerRepoGitNotesSha,
        PathValues.REPOS_OWNER_REPO_GIT_REFS: ReposOwnerRepoGitRefs,
        PathValues.REPOS_OWNER_REPO_GIT_REFS_REF: ReposOwnerRepoGitRefsRef,
        PathValues.REPOS_OWNER_REPO_GIT_TAGS_SHA: ReposOwnerRepoGitTagsSha,
        PathValues.REPOS_OWNER_REPO_GIT_TREES_SHA: ReposOwnerRepoGitTreesSha,
        PathValues.REPOS_OWNER_REPO_HOOKS: ReposOwnerRepoHooks,
        PathValues.REPOS_OWNER_REPO_HOOKS_GIT: ReposOwnerRepoHooksGit,
        PathValues.REPOS_OWNER_REPO_HOOKS_GIT_ID: ReposOwnerRepoHooksGitId,
        PathValues.REPOS_OWNER_REPO_HOOKS_ID: ReposOwnerRepoHooksId,
        PathValues.REPOS_OWNER_REPO_HOOKS_ID_TESTS: ReposOwnerRepoHooksIdTests,
        PathValues.REPOS_OWNER_REPO_ISSUE_TEMPLATES: ReposOwnerRepoIssueTemplates,
        PathValues.REPOS_OWNER_REPO_ISSUES: ReposOwnerRepoIssues,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS: ReposOwnerRepoIssuesComments,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS_ID: ReposOwnerRepoIssuesCommentsId,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS_ID_ASSETS: ReposOwnerRepoIssuesCommentsIdAssets,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS_ID_ASSETS_ATTACHMENT_ID: ReposOwnerRepoIssuesCommentsIdAssetsAttachmentId,
        PathValues.REPOS_OWNER_REPO_ISSUES_COMMENTS_ID_REACTIONS: ReposOwnerRepoIssuesCommentsIdReactions,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX: ReposOwnerRepoIssuesIndex,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_ASSETS: ReposOwnerRepoIssuesIndexAssets,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_ASSETS_ATTACHMENT_ID: ReposOwnerRepoIssuesIndexAssetsAttachmentId,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_COMMENTS: ReposOwnerRepoIssuesIndexComments,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_COMMENTS_ID: ReposOwnerRepoIssuesIndexCommentsId,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_DEADLINE: ReposOwnerRepoIssuesIndexDeadline,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_LABELS: ReposOwnerRepoIssuesIndexLabels,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_LABELS_ID: ReposOwnerRepoIssuesIndexLabelsId,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_REACTIONS: ReposOwnerRepoIssuesIndexReactions,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_STOPWATCH_DELETE: ReposOwnerRepoIssuesIndexStopwatchDelete,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_STOPWATCH_START: ReposOwnerRepoIssuesIndexStopwatchStart,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_STOPWATCH_STOP: ReposOwnerRepoIssuesIndexStopwatchStop,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_SUBSCRIPTIONS: ReposOwnerRepoIssuesIndexSubscriptions,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_SUBSCRIPTIONS_CHECK: ReposOwnerRepoIssuesIndexSubscriptionsCheck,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_SUBSCRIPTIONS_USER: ReposOwnerRepoIssuesIndexSubscriptionsUser,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_TIMELINE: ReposOwnerRepoIssuesIndexTimeline,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_TIMES: ReposOwnerRepoIssuesIndexTimes,
        PathValues.REPOS_OWNER_REPO_ISSUES_INDEX_TIMES_ID: ReposOwnerRepoIssuesIndexTimesId,
        PathValues.REPOS_OWNER_REPO_KEYS: ReposOwnerRepoKeys,
        PathValues.REPOS_OWNER_REPO_KEYS_ID: ReposOwnerRepoKeysId,
        PathValues.REPOS_OWNER_REPO_LABELS: ReposOwnerRepoLabels,
        PathValues.REPOS_OWNER_REPO_LABELS_ID: ReposOwnerRepoLabelsId,
        PathValues.REPOS_OWNER_REPO_LANGUAGES: ReposOwnerRepoLanguages,
        PathValues.REPOS_OWNER_REPO_MEDIA_FILEPATH: ReposOwnerRepoMediaFilepath,
        PathValues.REPOS_OWNER_REPO_MILESTONES: ReposOwnerRepoMilestones,
        PathValues.REPOS_OWNER_REPO_MILESTONES_ID: ReposOwnerRepoMilestonesId,
        PathValues.REPOS_OWNER_REPO_MIRRORSYNC: ReposOwnerRepoMirrorSync,
        PathValues.REPOS_OWNER_REPO_NOTIFICATIONS: ReposOwnerRepoNotifications,
        PathValues.REPOS_OWNER_REPO_PULLS: ReposOwnerRepoPulls,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX: ReposOwnerRepoPullsIndex,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_DIFF_TYPE: ReposOwnerRepoPullsIndexDiffType,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_COMMITS: ReposOwnerRepoPullsIndexCommits,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_FILES: ReposOwnerRepoPullsIndexFiles,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_MERGE: ReposOwnerRepoPullsIndexMerge,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REQUESTED_REVIEWERS: ReposOwnerRepoPullsIndexRequestedReviewers,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS: ReposOwnerRepoPullsIndexReviews,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS_ID: ReposOwnerRepoPullsIndexReviewsId,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS_ID_COMMENTS: ReposOwnerRepoPullsIndexReviewsIdComments,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS_ID_DISMISSALS: ReposOwnerRepoPullsIndexReviewsIdDismissals,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_REVIEWS_ID_UNDISMISSALS: ReposOwnerRepoPullsIndexReviewsIdUndismissals,
        PathValues.REPOS_OWNER_REPO_PULLS_INDEX_UPDATE: ReposOwnerRepoPullsIndexUpdate,
        PathValues.REPOS_OWNER_REPO_PUSH_MIRRORS: ReposOwnerRepoPushMirrors,
        PathValues.REPOS_OWNER_REPO_PUSH_MIRRORSSYNC: ReposOwnerRepoPushMirrorsSync,
        PathValues.REPOS_OWNER_REPO_PUSH_MIRRORS_NAME: ReposOwnerRepoPushMirrorsName,
        PathValues.REPOS_OWNER_REPO_RAW_FILEPATH: ReposOwnerRepoRawFilepath,
        PathValues.REPOS_OWNER_REPO_RELEASES: ReposOwnerRepoReleases,
        PathValues.REPOS_OWNER_REPO_RELEASES_LATEST: ReposOwnerRepoReleasesLatest,
        PathValues.REPOS_OWNER_REPO_RELEASES_TAGS_TAG: ReposOwnerRepoReleasesTagsTag,
        PathValues.REPOS_OWNER_REPO_RELEASES_ID: ReposOwnerRepoReleasesId,
        PathValues.REPOS_OWNER_REPO_RELEASES_ID_ASSETS: ReposOwnerRepoReleasesIdAssets,
        PathValues.REPOS_OWNER_REPO_RELEASES_ID_ASSETS_ATTACHMENT_ID: ReposOwnerRepoReleasesIdAssetsAttachmentId,
        PathValues.REPOS_OWNER_REPO_REVIEWERS: ReposOwnerRepoReviewers,
        PathValues.REPOS_OWNER_REPO_SIGNINGKEY_GPG: ReposOwnerRepoSigningKeyGpg,
        PathValues.REPOS_OWNER_REPO_STARGAZERS: ReposOwnerRepoStargazers,
        PathValues.REPOS_OWNER_REPO_STATUSES_SHA: ReposOwnerRepoStatusesSha,
        PathValues.REPOS_OWNER_REPO_SUBSCRIBERS: ReposOwnerRepoSubscribers,
        PathValues.REPOS_OWNER_REPO_SUBSCRIPTION: ReposOwnerRepoSubscription,
        PathValues.REPOS_OWNER_REPO_TAGS: ReposOwnerRepoTags,
        PathValues.REPOS_OWNER_REPO_TAGS_TAG: ReposOwnerRepoTagsTag,
        PathValues.REPOS_OWNER_REPO_TEAMS: ReposOwnerRepoTeams,
        PathValues.REPOS_OWNER_REPO_TEAMS_TEAM: ReposOwnerRepoTeamsTeam,
        PathValues.REPOS_OWNER_REPO_TIMES: ReposOwnerRepoTimes,
        PathValues.REPOS_OWNER_REPO_TIMES_USER: ReposOwnerRepoTimesUser,
        PathValues.REPOS_OWNER_REPO_TOPICS: ReposOwnerRepoTopics,
        PathValues.REPOS_OWNER_REPO_TOPICS_TOPIC: ReposOwnerRepoTopicsTopic,
        PathValues.REPOS_OWNER_REPO_TRANSFER: ReposOwnerRepoTransfer,
        PathValues.REPOS_OWNER_REPO_TRANSFER_ACCEPT: ReposOwnerRepoTransferAccept,
        PathValues.REPOS_OWNER_REPO_TRANSFER_REJECT: ReposOwnerRepoTransferReject,
        PathValues.REPOS_OWNER_REPO_WIKI_NEW: ReposOwnerRepoWikiNew,
        PathValues.REPOS_OWNER_REPO_WIKI_PAGE_PAGE_NAME: ReposOwnerRepoWikiPagePageName,
        PathValues.REPOS_OWNER_REPO_WIKI_PAGES: ReposOwnerRepoWikiPages,
        PathValues.REPOS_OWNER_REPO_WIKI_REVISIONS_PAGE_NAME: ReposOwnerRepoWikiRevisionsPageName,
        PathValues.REPOS_TEMPLATE_OWNER_TEMPLATE_REPO_GENERATE: ReposTemplateOwnerTemplateRepoGenerate,
        PathValues.REPOSITORIES_ID: RepositoriesId,
        PathValues.SETTINGS_API: SettingsApi,
        PathValues.SETTINGS_ATTACHMENT: SettingsAttachment,
        PathValues.SETTINGS_REPOSITORY: SettingsRepository,
        PathValues.SETTINGS_UI: SettingsUi,
        PathValues.SIGNINGKEY_GPG: SigningKeyGpg,
        PathValues.TEAMS_ID: TeamsId,
        PathValues.TEAMS_ID_MEMBERS: TeamsIdMembers,
        PathValues.TEAMS_ID_MEMBERS_USERNAME: TeamsIdMembersUsername,
        PathValues.TEAMS_ID_REPOS: TeamsIdRepos,
        PathValues.TEAMS_ID_REPOS_ORG_REPO: TeamsIdReposOrgRepo,
        PathValues.TOPICS_SEARCH: TopicsSearch,
        PathValues.USER: User,
        PathValues.USER_APPLICATIONS_OAUTH2: UserApplicationsOauth2,
        PathValues.USER_APPLICATIONS_OAUTH2_ID: UserApplicationsOauth2Id,
        PathValues.USER_EMAILS: UserEmails,
        PathValues.USER_FOLLOWERS: UserFollowers,
        PathValues.USER_FOLLOWING: UserFollowing,
        PathValues.USER_FOLLOWING_USERNAME: UserFollowingUsername,
        PathValues.USER_GPG_KEY_TOKEN: UserGpgKeyToken,
        PathValues.USER_GPG_KEY_VERIFY: UserGpgKeyVerify,
        PathValues.USER_GPG_KEYS: UserGpgKeys,
        PathValues.USER_GPG_KEYS_ID: UserGpgKeysId,
        PathValues.USER_KEYS: UserKeys,
        PathValues.USER_KEYS_ID: UserKeysId,
        PathValues.USER_ORGS: UserOrgs,
        PathValues.USER_REPOS: UserRepos,
        PathValues.USER_SETTINGS: UserSettings,
        PathValues.USER_STARRED: UserStarred,
        PathValues.USER_STARRED_OWNER_REPO: UserStarredOwnerRepo,
        PathValues.USER_STOPWATCHES: UserStopwatches,
        PathValues.USER_SUBSCRIPTIONS: UserSubscriptions,
        PathValues.USER_TEAMS: UserTeams,
        PathValues.USER_TIMES: UserTimes,
        PathValues.USERS_SEARCH: UsersSearch,
        PathValues.USERS_USERNAME: UsersUsername,
        PathValues.USERS_USERNAME_FOLLOWERS: UsersUsernameFollowers,
        PathValues.USERS_USERNAME_FOLLOWING: UsersUsernameFollowing,
        PathValues.USERS_USERNAME_FOLLOWING_TARGET: UsersUsernameFollowingTarget,
        PathValues.USERS_USERNAME_GPG_KEYS: UsersUsernameGpgKeys,
        PathValues.USERS_USERNAME_HEATMAP: UsersUsernameHeatmap,
        PathValues.USERS_USERNAME_KEYS: UsersUsernameKeys,
        PathValues.USERS_USERNAME_ORGS: UsersUsernameOrgs,
        PathValues.USERS_USERNAME_ORGS_ORG_PERMISSIONS: UsersUsernameOrgsOrgPermissions,
        PathValues.USERS_USERNAME_REPOS: UsersUsernameRepos,
        PathValues.USERS_USERNAME_STARRED: UsersUsernameStarred,
        PathValues.USERS_USERNAME_SUBSCRIPTIONS: UsersUsernameSubscriptions,
        PathValues.USERS_USERNAME_TOKENS: UsersUsernameTokens,
        PathValues.USERS_USERNAME_TOKENS_TOKEN: UsersUsernameTokensToken,
        PathValues.VERSION: Version,
    }
)

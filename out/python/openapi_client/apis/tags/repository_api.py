# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    The version of the OpenAPI document: 1.19.0
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.repos_owner_repo_transfer_accept.post import AcceptRepoTransfer
from openapi_client.paths.user_repos.post import CreateCurrentUserRepo
from openapi_client.paths.repos_owner_repo_forks.post import CreateFork
from openapi_client.paths.repos_template_owner_template_repo_generate.post import GenerateRepo
from openapi_client.paths.repos_owner_repo_git_tags_sha.get import GetAnnotatedTag
from openapi_client.paths.repos_owner_repo_git_blobs_sha.get import GetBlob
from openapi_client.paths.repos_owner_repo_git_trees_sha.get import GetTree
from openapi_client.paths.repos_owner_repo_forks.get import ListForks
from openapi_client.paths.repos_owner_repo_transfer_reject.post import RejectRepoTransfer
from openapi_client.paths.repos_owner_repo_collaborators_collaborator.put import RepoAddCollaborator
from openapi_client.paths.repos_owner_repo_push_mirrors.post import RepoAddPushMirror
from openapi_client.paths.repos_owner_repo_teams_team.put import RepoAddTeam
from openapi_client.paths.repos_owner_repo_topics_topic.put import RepoAddTopic
from openapi_client.paths.repos_owner_repo_diffpatch.post import RepoApplyDiffPatch
from openapi_client.paths.repos_owner_repo_pulls_index_merge.delete import RepoCancelScheduledAutoMerge
from openapi_client.paths.repos_owner_repo_collaborators_collaborator.get import RepoCheckCollaborator
from openapi_client.paths.repos_owner_repo_teams_team.get import RepoCheckTeam
from openapi_client.paths.repos_owner_repo_branches.post import RepoCreateBranch
from openapi_client.paths.repos_owner_repo_branch_protections.post import RepoCreateBranchProtection
from openapi_client.paths.repos_owner_repo_contents_filepath.post import RepoCreateFile
from openapi_client.paths.repos_owner_repo_hooks.post import RepoCreateHook
from openapi_client.paths.repos_owner_repo_keys.post import RepoCreateKey
from openapi_client.paths.repos_owner_repo_pulls.post import RepoCreatePullRequest
from openapi_client.paths.repos_owner_repo_pulls_index_reviews.post import RepoCreatePullReview
from openapi_client.paths.repos_owner_repo_pulls_index_requested_reviewers.post import RepoCreatePullReviewRequests
from openapi_client.paths.repos_owner_repo_releases.post import RepoCreateRelease
from openapi_client.paths.repos_owner_repo_releases_id_assets.post import RepoCreateReleaseAttachment
from openapi_client.paths.repos_owner_repo_statuses_sha.post import RepoCreateStatus
from openapi_client.paths.repos_owner_repo_tags.post import RepoCreateTag
from openapi_client.paths.repos_owner_repo_wiki_new.post import RepoCreateWikiPage
from openapi_client.paths.repos_owner_repo.delete import RepoDelete
from openapi_client.paths.repos_owner_repo_branches_branch.delete import RepoDeleteBranch
from openapi_client.paths.repos_owner_repo_branch_protections_name.delete import RepoDeleteBranchProtection
from openapi_client.paths.repos_owner_repo_collaborators_collaborator.delete import RepoDeleteCollaborator
from openapi_client.paths.repos_owner_repo_contents_filepath.delete import RepoDeleteFile
from openapi_client.paths.repos_owner_repo_hooks_git_id.delete import RepoDeleteGitHook
from openapi_client.paths.repos_owner_repo_hooks_id.delete import RepoDeleteHook
from openapi_client.paths.repos_owner_repo_keys_id.delete import RepoDeleteKey
from openapi_client.paths.repos_owner_repo_pulls_index_reviews_id.delete import RepoDeletePullReview
from openapi_client.paths.repos_owner_repo_pulls_index_requested_reviewers.delete import RepoDeletePullReviewRequests
from openapi_client.paths.repos_owner_repo_push_mirrors_name.delete import RepoDeletePushMirror
from openapi_client.paths.repos_owner_repo_releases_id.delete import RepoDeleteRelease
from openapi_client.paths.repos_owner_repo_releases_id_assets_attachment_id.delete import RepoDeleteReleaseAttachment
from openapi_client.paths.repos_owner_repo_releases_tags_tag.delete import RepoDeleteReleaseByTag
from openapi_client.paths.repos_owner_repo_tags_tag.delete import RepoDeleteTag
from openapi_client.paths.repos_owner_repo_teams_team.delete import RepoDeleteTeam
from openapi_client.paths.repos_owner_repo_topics_topic.delete import RepoDeleteTopic
from openapi_client.paths.repos_owner_repo_wiki_page_page_name.delete import RepoDeleteWikiPage
from openapi_client.paths.repos_owner_repo_pulls_index_reviews_id_dismissals.post import RepoDismissPullReview
from openapi_client.paths.repos_owner_repo_git_commits_sha_diff_type.get import RepoDownloadCommitDiffOrPatch
from openapi_client.paths.repos_owner_repo_pulls_index_diff_type.get import RepoDownloadPullDiffOrPatch
from openapi_client.paths.repos_owner_repo.patch import RepoEdit
from openapi_client.paths.repos_owner_repo_branch_protections_name.patch import RepoEditBranchProtection
from openapi_client.paths.repos_owner_repo_hooks_git_id.patch import RepoEditGitHook
from openapi_client.paths.repos_owner_repo_hooks_id.patch import RepoEditHook
from openapi_client.paths.repos_owner_repo_pulls_index.patch import RepoEditPullRequest
from openapi_client.paths.repos_owner_repo_releases_id.patch import RepoEditRelease
from openapi_client.paths.repos_owner_repo_releases_id_assets_attachment_id.patch import RepoEditReleaseAttachment
from openapi_client.paths.repos_owner_repo_wiki_page_page_name.patch import RepoEditWikiPage
from openapi_client.paths.repos_owner_repo.get import RepoGet
from openapi_client.paths.repos_owner_repo_commits.get import RepoGetAllCommits
from openapi_client.paths.repos_owner_repo_archive_archive.get import RepoGetArchive
from openapi_client.paths.repos_owner_repo_assignees.get import RepoGetAssignees
from openapi_client.paths.repos_owner_repo_branches_branch.get import RepoGetBranch
from openapi_client.paths.repos_owner_repo_branch_protections_name.get import RepoGetBranchProtection
from openapi_client.paths.repositories_id.get import RepoGetById
from openapi_client.paths.repos_owner_repo_commits_ref_status.get import RepoGetCombinedStatusByRef
from openapi_client.paths.repos_owner_repo_contents_filepath.get import RepoGetContents
from openapi_client.paths.repos_owner_repo_contents.get import RepoGetContentsList
from openapi_client.paths.repos_owner_repo_editorconfig_filepath.get import RepoGetEditorConfig
from openapi_client.paths.repos_owner_repo_hooks_git_id.get import RepoGetGitHook
from openapi_client.paths.repos_owner_repo_hooks_id.get import RepoGetHook
from openapi_client.paths.repos_owner_repo_issue_templates.get import RepoGetIssueTemplates
from openapi_client.paths.repos_owner_repo_keys_id.get import RepoGetKey
from openapi_client.paths.repos_owner_repo_languages.get import RepoGetLanguages
from openapi_client.paths.repos_owner_repo_releases_latest.get import RepoGetLatestRelease
from openapi_client.paths.repos_owner_repo_git_notes_sha.get import RepoGetNote
from openapi_client.paths.repos_owner_repo_pulls_index.get import RepoGetPullRequest
from openapi_client.paths.repos_owner_repo_pulls_index_commits.get import RepoGetPullRequestCommits
from openapi_client.paths.repos_owner_repo_pulls_index_files.get import RepoGetPullRequestFiles
from openapi_client.paths.repos_owner_repo_pulls_index_reviews_id.get import RepoGetPullReview
from openapi_client.paths.repos_owner_repo_pulls_index_reviews_id_comments.get import RepoGetPullReviewComments
from openapi_client.paths.repos_owner_repo_push_mirrors_name.get import RepoGetPushMirrorByRemoteName
from openapi_client.paths.repos_owner_repo_raw_filepath.get import RepoGetRawFile
from openapi_client.paths.repos_owner_repo_media_filepath.get import RepoGetRawFileOrLfs
from openapi_client.paths.repos_owner_repo_releases_id.get import RepoGetRelease
from openapi_client.paths.repos_owner_repo_releases_id_assets_attachment_id.get import RepoGetReleaseAttachment
from openapi_client.paths.repos_owner_repo_releases_tags_tag.get import RepoGetReleaseByTag
from openapi_client.paths.repos_owner_repo_collaborators_collaborator_permission.get import RepoGetRepoPermissions
from openapi_client.paths.repos_owner_repo_reviewers.get import RepoGetReviewers
from openapi_client.paths.repos_owner_repo_git_commits_sha.get import RepoGetSingleCommit
from openapi_client.paths.repos_owner_repo_tags_tag.get import RepoGetTag
from openapi_client.paths.repos_owner_repo_wiki_page_page_name.get import RepoGetWikiPage
from openapi_client.paths.repos_owner_repo_wiki_revisions_page_name.get import RepoGetWikiPageRevisions
from openapi_client.paths.repos_owner_repo_wiki_pages.get import RepoGetWikiPages
from openapi_client.paths.repos_owner_repo_git_refs.get import RepoListAllGitRefs
from openapi_client.paths.repos_owner_repo_branch_protections.get import RepoListBranchProtection
from openapi_client.paths.repos_owner_repo_branches.get import RepoListBranches
from openapi_client.paths.repos_owner_repo_collaborators.get import RepoListCollaborators
from openapi_client.paths.repos_owner_repo_hooks_git.get import RepoListGitHooks
from openapi_client.paths.repos_owner_repo_git_refs_ref.get import RepoListGitRefs
from openapi_client.paths.repos_owner_repo_hooks.get import RepoListHooks
from openapi_client.paths.repos_owner_repo_keys.get import RepoListKeys
from openapi_client.paths.repos_owner_repo_pulls.get import RepoListPullRequests
from openapi_client.paths.repos_owner_repo_pulls_index_reviews.get import RepoListPullReviews
from openapi_client.paths.repos_owner_repo_push_mirrors.get import RepoListPushMirrors
from openapi_client.paths.repos_owner_repo_releases_id_assets.get import RepoListReleaseAttachments
from openapi_client.paths.repos_owner_repo_releases.get import RepoListReleases
from openapi_client.paths.repos_owner_repo_stargazers.get import RepoListStargazers
from openapi_client.paths.repos_owner_repo_statuses_sha.get import RepoListStatuses
from openapi_client.paths.repos_owner_repo_commits_ref_statuses.get import RepoListStatusesByRef
from openapi_client.paths.repos_owner_repo_subscribers.get import RepoListSubscribers
from openapi_client.paths.repos_owner_repo_tags.get import RepoListTags
from openapi_client.paths.repos_owner_repo_teams.get import RepoListTeams
from openapi_client.paths.repos_owner_repo_topics.get import RepoListTopics
from openapi_client.paths.repos_owner_repo_pulls_index_merge.post import RepoMergePullRequest
from openapi_client.paths.repos_migrate.post import RepoMigrate
from openapi_client.paths.repos_owner_repo_mirror_sync.post import RepoMirrorSync
from openapi_client.paths.repos_owner_repo_pulls_index_merge.get import RepoPullRequestIsMerged
from openapi_client.paths.repos_owner_repo_push_mirrors_sync.post import RepoPushMirrorSync
from openapi_client.paths.repos_search.get import RepoSearch
from openapi_client.paths.repos_owner_repo_signing_key_gpg.get import RepoSigningKey
from openapi_client.paths.repos_owner_repo_pulls_index_reviews_id.post import RepoSubmitPullReview
from openapi_client.paths.repos_owner_repo_hooks_id_tests.post import RepoTestHook
from openapi_client.paths.repos_owner_repo_times.get import RepoTrackedTimes
from openapi_client.paths.repos_owner_repo_transfer.post import RepoTransfer
from openapi_client.paths.repos_owner_repo_pulls_index_reviews_id_undismissals.post import RepoUnDismissPullReview
from openapi_client.paths.repos_owner_repo_contents_filepath.put import RepoUpdateFile
from openapi_client.paths.repos_owner_repo_pulls_index_update.post import RepoUpdatePullRequest
from openapi_client.paths.repos_owner_repo_topics.put import RepoUpdateTopics
from openapi_client.paths.topics_search.get import TopicSearch
from openapi_client.paths.repos_owner_repo_subscription.get import UserCurrentCheckSubscription
from openapi_client.paths.repos_owner_repo_subscription.delete import UserCurrentDeleteSubscription
from openapi_client.paths.repos_owner_repo_subscription.put import UserCurrentPutSubscription
from openapi_client.paths.repos_owner_repo_times_user.get import UserTrackedTimes


class RepositoryApi(
    AcceptRepoTransfer,
    CreateCurrentUserRepo,
    CreateFork,
    GenerateRepo,
    GetAnnotatedTag,
    GetBlob,
    GetTree,
    ListForks,
    RejectRepoTransfer,
    RepoAddCollaborator,
    RepoAddPushMirror,
    RepoAddTeam,
    RepoAddTopic,
    RepoApplyDiffPatch,
    RepoCancelScheduledAutoMerge,
    RepoCheckCollaborator,
    RepoCheckTeam,
    RepoCreateBranch,
    RepoCreateBranchProtection,
    RepoCreateFile,
    RepoCreateHook,
    RepoCreateKey,
    RepoCreatePullRequest,
    RepoCreatePullReview,
    RepoCreatePullReviewRequests,
    RepoCreateRelease,
    RepoCreateReleaseAttachment,
    RepoCreateStatus,
    RepoCreateTag,
    RepoCreateWikiPage,
    RepoDelete,
    RepoDeleteBranch,
    RepoDeleteBranchProtection,
    RepoDeleteCollaborator,
    RepoDeleteFile,
    RepoDeleteGitHook,
    RepoDeleteHook,
    RepoDeleteKey,
    RepoDeletePullReview,
    RepoDeletePullReviewRequests,
    RepoDeletePushMirror,
    RepoDeleteRelease,
    RepoDeleteReleaseAttachment,
    RepoDeleteReleaseByTag,
    RepoDeleteTag,
    RepoDeleteTeam,
    RepoDeleteTopic,
    RepoDeleteWikiPage,
    RepoDismissPullReview,
    RepoDownloadCommitDiffOrPatch,
    RepoDownloadPullDiffOrPatch,
    RepoEdit,
    RepoEditBranchProtection,
    RepoEditGitHook,
    RepoEditHook,
    RepoEditPullRequest,
    RepoEditRelease,
    RepoEditReleaseAttachment,
    RepoEditWikiPage,
    RepoGet,
    RepoGetAllCommits,
    RepoGetArchive,
    RepoGetAssignees,
    RepoGetBranch,
    RepoGetBranchProtection,
    RepoGetById,
    RepoGetCombinedStatusByRef,
    RepoGetContents,
    RepoGetContentsList,
    RepoGetEditorConfig,
    RepoGetGitHook,
    RepoGetHook,
    RepoGetIssueTemplates,
    RepoGetKey,
    RepoGetLanguages,
    RepoGetLatestRelease,
    RepoGetNote,
    RepoGetPullRequest,
    RepoGetPullRequestCommits,
    RepoGetPullRequestFiles,
    RepoGetPullReview,
    RepoGetPullReviewComments,
    RepoGetPushMirrorByRemoteName,
    RepoGetRawFile,
    RepoGetRawFileOrLfs,
    RepoGetRelease,
    RepoGetReleaseAttachment,
    RepoGetReleaseByTag,
    RepoGetRepoPermissions,
    RepoGetReviewers,
    RepoGetSingleCommit,
    RepoGetTag,
    RepoGetWikiPage,
    RepoGetWikiPageRevisions,
    RepoGetWikiPages,
    RepoListAllGitRefs,
    RepoListBranchProtection,
    RepoListBranches,
    RepoListCollaborators,
    RepoListGitHooks,
    RepoListGitRefs,
    RepoListHooks,
    RepoListKeys,
    RepoListPullRequests,
    RepoListPullReviews,
    RepoListPushMirrors,
    RepoListReleaseAttachments,
    RepoListReleases,
    RepoListStargazers,
    RepoListStatuses,
    RepoListStatusesByRef,
    RepoListSubscribers,
    RepoListTags,
    RepoListTeams,
    RepoListTopics,
    RepoMergePullRequest,
    RepoMigrate,
    RepoMirrorSync,
    RepoPullRequestIsMerged,
    RepoPushMirrorSync,
    RepoSearch,
    RepoSigningKey,
    RepoSubmitPullReview,
    RepoTestHook,
    RepoTrackedTimes,
    RepoTransfer,
    RepoUnDismissPullReview,
    RepoUpdateFile,
    RepoUpdatePullRequest,
    RepoUpdateTopics,
    TopicSearch,
    UserCurrentCheckSubscription,
    UserCurrentDeleteSubscription,
    UserCurrentPutSubscription,
    UserTrackedTimes,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
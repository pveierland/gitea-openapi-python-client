from openapi_client.paths.repos_owner_repo.get import ApiForget
from openapi_client.paths.repos_owner_repo.delete import ApiFordelete
from openapi_client.paths.repos_owner_repo.patch import ApiForpatch


class ReposOwnerRepo(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass

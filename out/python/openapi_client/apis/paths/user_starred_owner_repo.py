from openapi_client.paths.user_starred_owner_repo.get import ApiForget
from openapi_client.paths.user_starred_owner_repo.put import ApiForput
from openapi_client.paths.user_starred_owner_repo.delete import ApiFordelete


class UserStarredOwnerRepo(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass

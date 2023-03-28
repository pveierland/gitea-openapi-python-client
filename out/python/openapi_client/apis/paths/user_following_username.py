from openapi_client.paths.user_following_username.get import ApiForget
from openapi_client.paths.user_following_username.put import ApiForput
from openapi_client.paths.user_following_username.delete import ApiFordelete


class UserFollowingUsername(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass

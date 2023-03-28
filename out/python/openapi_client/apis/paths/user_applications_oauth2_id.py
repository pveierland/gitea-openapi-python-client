from openapi_client.paths.user_applications_oauth2_id.get import ApiForget
from openapi_client.paths.user_applications_oauth2_id.delete import ApiFordelete
from openapi_client.paths.user_applications_oauth2_id.patch import ApiForpatch


class UserApplicationsOauth2Id(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass

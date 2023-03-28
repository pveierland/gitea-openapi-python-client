from openapi_client.paths.teams_id.get import ApiForget
from openapi_client.paths.teams_id.delete import ApiFordelete
from openapi_client.paths.teams_id.patch import ApiForpatch


class TeamsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass

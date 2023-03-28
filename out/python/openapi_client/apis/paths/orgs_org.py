from openapi_client.paths.orgs_org.get import ApiForget
from openapi_client.paths.orgs_org.delete import ApiFordelete
from openapi_client.paths.orgs_org.patch import ApiForpatch


class OrgsOrg(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass

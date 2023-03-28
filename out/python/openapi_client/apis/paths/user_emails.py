from openapi_client.paths.user_emails.get import ApiForget
from openapi_client.paths.user_emails.post import ApiForpost
from openapi_client.paths.user_emails.delete import ApiFordelete


class UserEmails(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass

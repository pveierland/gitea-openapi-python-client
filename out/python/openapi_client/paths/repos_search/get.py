# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from openapi_client import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401

from openapi_client.model.search_results import SearchResults

from . import path

# Query params
QSchema = schemas.StrSchema
TopicSchema = schemas.BoolSchema
IncludeDescSchema = schemas.BoolSchema
UidSchema = schemas.Int64Schema
PriorityOwnerIdSchema = schemas.Int64Schema
TeamIdSchema = schemas.Int64Schema
StarredBySchema = schemas.Int64Schema
PrivateSchema = schemas.BoolSchema
IsPrivateSchema = schemas.BoolSchema
TemplateSchema = schemas.BoolSchema
ArchivedSchema = schemas.BoolSchema
ModeSchema = schemas.StrSchema
ExclusiveSchema = schemas.BoolSchema
SortSchema = schemas.StrSchema
OrderSchema = schemas.StrSchema
PageSchema = schemas.IntSchema
LimitSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'q': typing.Union[QSchema, str, ],
        'topic': typing.Union[TopicSchema, bool, ],
        'includeDesc': typing.Union[IncludeDescSchema, bool, ],
        'uid': typing.Union[UidSchema, decimal.Decimal, int, ],
        'priority_owner_id': typing.Union[PriorityOwnerIdSchema, decimal.Decimal, int, ],
        'team_id': typing.Union[TeamIdSchema, decimal.Decimal, int, ],
        'starredBy': typing.Union[StarredBySchema, decimal.Decimal, int, ],
        'private': typing.Union[PrivateSchema, bool, ],
        'is_private': typing.Union[IsPrivateSchema, bool, ],
        'template': typing.Union[TemplateSchema, bool, ],
        'archived': typing.Union[ArchivedSchema, bool, ],
        'mode': typing.Union[ModeSchema, str, ],
        'exclusive': typing.Union[ExclusiveSchema, bool, ],
        'sort': typing.Union[SortSchema, str, ],
        'order': typing.Union[OrderSchema, str, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_q = api_client.QueryParameter(
    name="q",
    style=api_client.ParameterStyle.FORM,
    schema=QSchema,
    explode=True,
)
request_query_topic = api_client.QueryParameter(
    name="topic",
    style=api_client.ParameterStyle.FORM,
    schema=TopicSchema,
    explode=True,
)
request_query_include_desc = api_client.QueryParameter(
    name="includeDesc",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeDescSchema,
    explode=True,
)
request_query_uid = api_client.QueryParameter(
    name="uid",
    style=api_client.ParameterStyle.FORM,
    schema=UidSchema,
    explode=True,
)
request_query_priority_owner_id = api_client.QueryParameter(
    name="priority_owner_id",
    style=api_client.ParameterStyle.FORM,
    schema=PriorityOwnerIdSchema,
    explode=True,
)
request_query_team_id = api_client.QueryParameter(
    name="team_id",
    style=api_client.ParameterStyle.FORM,
    schema=TeamIdSchema,
    explode=True,
)
request_query_starred_by = api_client.QueryParameter(
    name="starredBy",
    style=api_client.ParameterStyle.FORM,
    schema=StarredBySchema,
    explode=True,
)
request_query_private = api_client.QueryParameter(
    name="private",
    style=api_client.ParameterStyle.FORM,
    schema=PrivateSchema,
    explode=True,
)
request_query_is_private = api_client.QueryParameter(
    name="is_private",
    style=api_client.ParameterStyle.FORM,
    schema=IsPrivateSchema,
    explode=True,
)
request_query_template = api_client.QueryParameter(
    name="template",
    style=api_client.ParameterStyle.FORM,
    schema=TemplateSchema,
    explode=True,
)
request_query_archived = api_client.QueryParameter(
    name="archived",
    style=api_client.ParameterStyle.FORM,
    schema=ArchivedSchema,
    explode=True,
)
request_query_mode = api_client.QueryParameter(
    name="mode",
    style=api_client.ParameterStyle.FORM,
    schema=ModeSchema,
    explode=True,
)
request_query_exclusive = api_client.QueryParameter(
    name="exclusive",
    style=api_client.ParameterStyle.FORM,
    schema=ExclusiveSchema,
    explode=True,
)
request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
request_query_order = api_client.QueryParameter(
    name="order",
    style=api_client.ParameterStyle.FORM,
    schema=OrderSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
_auth = [
    'TOTPHeader',
    'AuthorizationHeaderToken',
    'SudoHeader',
    'BasicAuth',
    'AccessToken',
    'SudoParam',
    'Token',
]
SchemaFor200ResponseBodyApplicationJson = SearchResults


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
MessageSchema = schemas.StrSchema
message_parameter = api_client.HeaderParameter(
    name="message",
    style=api_client.ParameterStyle.SIMPLE,
    schema=MessageSchema,
)
UrlSchema = schemas.StrSchema
url_parameter = api_client.HeaderParameter(
    name="url",
    style=api_client.ParameterStyle.SIMPLE,
    schema=UrlSchema,
)
ResponseHeadersFor422 = typing_extensions.TypedDict(
    'ResponseHeadersFor422',
    {
        'message': MessageSchema,
        'url': UrlSchema,
    }
)


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Any
    headers: ResponseHeadersFor422


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    headers=[
        message_parameter,
        url_parameter,
    ]
)
_status_code_to_response = {
    '200': _response_for_200,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _repo_search_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _repo_search_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _repo_search_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _repo_search_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Search for repositories
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_q,
            request_query_topic,
            request_query_include_desc,
            request_query_uid,
            request_query_priority_owner_id,
            request_query_team_id,
            request_query_starred_by,
            request_query_private,
            request_query_is_private,
            request_query_template,
            request_query_archived,
            request_query_mode,
            request_query_exclusive,
            request_query_sort,
            request_query_order,
            request_query_page,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class RepoSearch(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def repo_search(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def repo_search(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def repo_search(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def repo_search(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._repo_search_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._repo_search_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


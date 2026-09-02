# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict, Optional
from typing_extensions import Literal

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform, strip_not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.organization_response import OrganizationResponse
from ..types import organization_create_params, organization_list_params
from ..types.organization_list import OrganizationList

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrganizationsResourceWithRawResponse:
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
        return OrganizationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationResponse:
        """
        Creates an organization for your platform and returns it. Organizations group related accounts and users.

        Args:
            name: Organization name.
            metadata: Up to 20 user-defined key-value pairs.
            external_id: Your unique ID for the organization.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationResponse: Created

        Example:
            ```python
            organization = client.organizations.create(
                name="",
            )
            ```
        """
        extra_headers = {
            **strip_not_given(
                {"Request-Id": request_id, "Correlation-Id": correlation_id, "Idempotency-Key": idempotency_key}
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/v1/organizations",
            body=maybe_transform(
                {
                    "name": name,
                    "metadata": metadata,
                    "external_id": external_id,
                },
                organization_create_params.OrganizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationResponse,
        )

    def list(
        self,
        *,
        name: str | Omit = omit,
        external_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationList:
        """
        Returns a paginated list of organizations for your platform. Filter the list by name or external ID.

        Args:
            name: Organization name. Supports partial matches.
            external_id: Your external ID for the organization.
            page_number: Page number. Defaults to `1`.
            page_size: Number of results per page. Defaults to `100`. Maximum `1000`.
            sort_by: Field used to sort results. Defaults to `id`.
            sort_order: Sort direction. Defaults to `asc`.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationList: OK

        Example:
            ```python
            organization = client.organizations.list(
                page_number=1,
                page_size=100,
                sort_by="id",
                sort_order="asc",
            )
            ```
        """
        extra_headers = {
            **strip_not_given({"Request-Id": request_id, "Correlation-Id": correlation_id}),
            **(extra_headers or {}),
        }
        return self._get(
            "/v1/organizations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "external_id": external_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    organization_list_params.OrganizationListParams,
                ),
            ),
            cast_to=OrganizationList,
        )

    def retrieve(
        self,
        organization_id: str,
        *,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationResponse:
        """
        Returns the organization with the specified ID.

        Args:
            organization_id: The ID of the organization.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationResponse: OK

        Example:
            ```python
            organization = client.organizations.retrieve(
                organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {
            **strip_not_given({"Request-Id": request_id, "Correlation-Id": correlation_id}),
            **(extra_headers or {}),
        }
        return self._get(
            path_template("/v1/organizations/{organization_id}", **{"organization_id": organization_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationResponse,
        )


class AsyncOrganizationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsResourceWithRawResponse:
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        return AsyncOrganizationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationResponse:
        """
        Creates an organization for your platform and returns it. Organizations group related accounts and users.

        Args:
            name: Organization name.
            metadata: Up to 20 user-defined key-value pairs.
            external_id: Your unique ID for the organization.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationResponse: Created

        Example:
            ```python
            organization = await client.organizations.create(
                name="",
            )
            ```
        """
        extra_headers = {
            **strip_not_given(
                {"Request-Id": request_id, "Correlation-Id": correlation_id, "Idempotency-Key": idempotency_key}
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/v1/organizations",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "metadata": metadata,
                    "external_id": external_id,
                },
                organization_create_params.OrganizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationResponse,
        )

    async def list(
        self,
        *,
        name: str | Omit = omit,
        external_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationList:
        """
        Returns a paginated list of organizations for your platform. Filter the list by name or external ID.

        Args:
            name: Organization name. Supports partial matches.
            external_id: Your external ID for the organization.
            page_number: Page number. Defaults to `1`.
            page_size: Number of results per page. Defaults to `100`. Maximum `1000`.
            sort_by: Field used to sort results. Defaults to `id`.
            sort_order: Sort direction. Defaults to `asc`.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationList: OK

        Example:
            ```python
            organization = await client.organizations.list(
                page_number=1,
                page_size=100,
                sort_by="id",
                sort_order="asc",
            )
            ```
        """
        extra_headers = {
            **strip_not_given({"Request-Id": request_id, "Correlation-Id": correlation_id}),
            **(extra_headers or {}),
        }
        return await self._get(
            "/v1/organizations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "external_id": external_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    organization_list_params.OrganizationListParams,
                ),
            ),
            cast_to=OrganizationList,
        )

    async def retrieve(
        self,
        organization_id: str,
        *,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationResponse:
        """
        Returns the organization with the specified ID.

        Args:
            organization_id: The ID of the organization.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrganizationResponse: OK

        Example:
            ```python
            organization = await client.organizations.retrieve(
                organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if organization_id is None or (isinstance(organization_id, str) and not organization_id):
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {
            **strip_not_given({"Request-Id": request_id, "Correlation-Id": correlation_id}),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template("/v1/organizations/{organization_id}", **{"organization_id": organization_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationResponse,
        )


class OrganizationsResourceWithRawResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.create = to_raw_response_wrapper(
            organizations.create,
        )
        self.list = to_raw_response_wrapper(
            organizations.list,
        )
        self.retrieve = to_raw_response_wrapper(
            organizations.retrieve,
        )


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.create = async_to_raw_response_wrapper(
            organizations.create,
        )
        self.list = async_to_raw_response_wrapper(
            organizations.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            organizations.retrieve,
        )


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.create = to_streamed_response_wrapper(
            organizations.create,
        )
        self.list = to_streamed_response_wrapper(
            organizations.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            organizations.retrieve,
        )


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.create = async_to_streamed_response_wrapper(
            organizations.create,
        )
        self.list = async_to_streamed_response_wrapper(
            organizations.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            organizations.retrieve,
        )

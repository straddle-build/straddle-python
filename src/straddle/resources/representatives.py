# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict, Optional, Union
from datetime import date
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
from ..types.representative_response import RepresentativeResponse
from ..types.representative_relationship_param import RepresentativeRelationshipParam
from ..types import representative_create_params, representative_list_params, representative_update_params
from ..types.representative_list import RepresentativeList
from ..types.unmasked_representative_response import UnmaskedRepresentativeResponse

__all__ = ["RepresentativesResource", "AsyncRepresentativesResource"]


class RepresentativesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RepresentativesResourceWithRawResponse:
        return RepresentativesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RepresentativesResourceWithStreamingResponse:
        return RepresentativesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        first_name: str,
        last_name: str,
        dob: Union[str, date],
        ssn_last4: str,
        email: str,
        mobile_number: str,
        relationship: RepresentativeRelationshipParam,
        external_id: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepresentativeResponse:
        """
        Creates a representative for an account and returns the representative. Relationship fields identify primary representatives, control persons, and owners.

        Args:
            account_id: ID of the account associated with the representative.
            first_name: Representative's first name.
            last_name: Representative's last name.
            dob: Representative's date of birth in `YYYY-MM-DD` format.
            ssn_last4: Last four digits of the representative's Social Security number.
            email: Representative's company email address.
            mobile_number: Representative's mobile phone number in E.164 format.
            relationship: Body parameter.
            external_id: Your unique ID for the representative.
            metadata: Up to 20 user-defined key-value pairs.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepresentativeResponse: Created

        Example:
            ```python
            representative = client.representatives.create(
                account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                first_name="",
                last_name="",
                dob="1980-01-01",
                ssn_last4="1234",
                email="ron.swanson@pawnee.com",
                mobile_number="+12128675309",
                relationship={"primary": False, "control": False, "owner": False},
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
            "/v1/representatives",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "dob": dob,
                    "ssn_last4": ssn_last4,
                    "email": email,
                    "mobile_number": mobile_number,
                    "relationship": relationship,
                    "external_id": external_id,
                    "metadata": metadata,
                },
                representative_create_params.RepresentativeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepresentativeResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        platform_id: str | Omit = omit,
        organization_id: str | Omit = omit,
        level: Literal["account", "platform"] | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepresentativeList:
        """
        Returns a paginated list of representatives. Filter the list by account, organization, platform, or scope.

        Args:
            account_id: Account ID used to filter the results.
            page_number: Page number. Defaults to `1`.
            page_size: Number of results per page. Defaults to `100`. Maximum `1000`.
            sort_by: Field used to sort results. Defaults to `id`.
            sort_order: Sort direction. Defaults to `asc`.
            platform_id: Platform ID used to filter the results.
            organization_id: Organization ID used to filter the results.
            level: Scope of representatives to return.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepresentativeList: OK

        Example:
            ```python
            representative = client.representatives.list(
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
            "/v1/representatives",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "platform_id": platform_id,
                        "organization_id": organization_id,
                        "level": level,
                    },
                    representative_list_params.RepresentativeListParams,
                ),
            ),
            cast_to=RepresentativeList,
        )

    def update(
        self,
        representative_id: str,
        *,
        first_name: str,
        last_name: str,
        dob: Union[str, date],
        ssn_last4: str,
        email: str,
        mobile_number: str,
        relationship: RepresentativeRelationshipParam,
        external_id: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepresentativeResponse:
        """
        Updates a representative's personal, contact, relationship, external ID, and metadata fields, then returns the representative.

        Args:
            representative_id: The ID of the representative.
            first_name: Representative's first name.
            last_name: Representative's last name.
            dob: Representative's date of birth in `YYYY-MM-DD` format.
            ssn_last4: Last four digits of the representative's Social Security number.
            email: Representative's email address.
            mobile_number: Representative's mobile phone number in E.164 format.
            relationship: Body parameter.
            external_id: Your unique ID for the representative.
            metadata: Up to 20 user-defined key-value pairs.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepresentativeResponse: OK

        Example:
            ```python
            representative = client.representatives.update(
                representative_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                first_name="Ron",
                last_name="Swanson",
                dob="1980-01-01",
                ssn_last4="1234",
                email="ron.swanson@pawnee.com",
                mobile_number="+12128675309",
                relationship={"primary": False, "control": False, "owner": False},
            )
            ```
        """
        if representative_id is None or (isinstance(representative_id, str) and not representative_id):
            raise ValueError(f"Expected a non-empty value for `representative_id` but received {representative_id!r}")
        extra_headers = {
            **strip_not_given(
                {"Request-Id": request_id, "Correlation-Id": correlation_id, "Idempotency-Key": idempotency_key}
            ),
            **(extra_headers or {}),
        }
        return self._put(
            path_template("/v1/representatives/{representative_id}", **{"representative_id": representative_id}),
            body=maybe_transform(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "dob": dob,
                    "ssn_last4": ssn_last4,
                    "email": email,
                    "mobile_number": mobile_number,
                    "relationship": relationship,
                    "external_id": external_id,
                    "metadata": metadata,
                },
                representative_update_params.RepresentativeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepresentativeResponse,
        )

    def retrieve(
        self,
        representative_id: str,
        *,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepresentativeResponse:
        """
        Returns the representative with the specified ID.

        Args:
            representative_id: The ID of the representative.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepresentativeResponse: OK

        Example:
            ```python
            representative = client.representatives.retrieve(
                representative_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if representative_id is None or (isinstance(representative_id, str) and not representative_id):
            raise ValueError(f"Expected a non-empty value for `representative_id` but received {representative_id!r}")
        extra_headers = {
            **strip_not_given({"Request-Id": request_id, "Correlation-Id": correlation_id}),
            **(extra_headers or {}),
        }
        return self._get(
            path_template("/v1/representatives/{representative_id}", **{"representative_id": representative_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepresentativeResponse,
        )

    def list_unmasked(
        self,
        representative_id: str,
        *,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnmaskedRepresentativeResponse:
        """
        Returns the representative with the specified ID without masking sensitive fields. This endpoint requires an administrator role.

        Args:
            representative_id: The ID of the representative.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UnmaskedRepresentativeResponse: OK

        Example:
            ```python
            representative = client.representatives.list_unmasked(
                representative_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if representative_id is None or (isinstance(representative_id, str) and not representative_id):
            raise ValueError(f"Expected a non-empty value for `representative_id` but received {representative_id!r}")
        extra_headers = {
            **strip_not_given({"Request-Id": request_id, "Correlation-Id": correlation_id}),
            **(extra_headers or {}),
        }
        return self._get(
            path_template("/v1/representatives/{representative_id}/unmask", **{"representative_id": representative_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnmaskedRepresentativeResponse,
        )


class AsyncRepresentativesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRepresentativesResourceWithRawResponse:
        return AsyncRepresentativesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRepresentativesResourceWithStreamingResponse:
        return AsyncRepresentativesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        first_name: str,
        last_name: str,
        dob: Union[str, date],
        ssn_last4: str,
        email: str,
        mobile_number: str,
        relationship: RepresentativeRelationshipParam,
        external_id: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepresentativeResponse:
        """
        Creates a representative for an account and returns the representative. Relationship fields identify primary representatives, control persons, and owners.

        Args:
            account_id: ID of the account associated with the representative.
            first_name: Representative's first name.
            last_name: Representative's last name.
            dob: Representative's date of birth in `YYYY-MM-DD` format.
            ssn_last4: Last four digits of the representative's Social Security number.
            email: Representative's company email address.
            mobile_number: Representative's mobile phone number in E.164 format.
            relationship: Body parameter.
            external_id: Your unique ID for the representative.
            metadata: Up to 20 user-defined key-value pairs.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepresentativeResponse: Created

        Example:
            ```python
            representative = await client.representatives.create(
                account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                first_name="",
                last_name="",
                dob="1980-01-01",
                ssn_last4="1234",
                email="ron.swanson@pawnee.com",
                mobile_number="+12128675309",
                relationship={"primary": False, "control": False, "owner": False},
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
            "/v1/representatives",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "dob": dob,
                    "ssn_last4": ssn_last4,
                    "email": email,
                    "mobile_number": mobile_number,
                    "relationship": relationship,
                    "external_id": external_id,
                    "metadata": metadata,
                },
                representative_create_params.RepresentativeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepresentativeResponse,
        )

    async def list(
        self,
        *,
        account_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        platform_id: str | Omit = omit,
        organization_id: str | Omit = omit,
        level: Literal["account", "platform"] | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepresentativeList:
        """
        Returns a paginated list of representatives. Filter the list by account, organization, platform, or scope.

        Args:
            account_id: Account ID used to filter the results.
            page_number: Page number. Defaults to `1`.
            page_size: Number of results per page. Defaults to `100`. Maximum `1000`.
            sort_by: Field used to sort results. Defaults to `id`.
            sort_order: Sort direction. Defaults to `asc`.
            platform_id: Platform ID used to filter the results.
            organization_id: Organization ID used to filter the results.
            level: Scope of representatives to return.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepresentativeList: OK

        Example:
            ```python
            representative = await client.representatives.list(
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
            "/v1/representatives",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "platform_id": platform_id,
                        "organization_id": organization_id,
                        "level": level,
                    },
                    representative_list_params.RepresentativeListParams,
                ),
            ),
            cast_to=RepresentativeList,
        )

    async def update(
        self,
        representative_id: str,
        *,
        first_name: str,
        last_name: str,
        dob: Union[str, date],
        ssn_last4: str,
        email: str,
        mobile_number: str,
        relationship: RepresentativeRelationshipParam,
        external_id: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepresentativeResponse:
        """
        Updates a representative's personal, contact, relationship, external ID, and metadata fields, then returns the representative.

        Args:
            representative_id: The ID of the representative.
            first_name: Representative's first name.
            last_name: Representative's last name.
            dob: Representative's date of birth in `YYYY-MM-DD` format.
            ssn_last4: Last four digits of the representative's Social Security number.
            email: Representative's email address.
            mobile_number: Representative's mobile phone number in E.164 format.
            relationship: Body parameter.
            external_id: Your unique ID for the representative.
            metadata: Up to 20 user-defined key-value pairs.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepresentativeResponse: OK

        Example:
            ```python
            representative = await client.representatives.update(
                representative_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                first_name="Ron",
                last_name="Swanson",
                dob="1980-01-01",
                ssn_last4="1234",
                email="ron.swanson@pawnee.com",
                mobile_number="+12128675309",
                relationship={"primary": False, "control": False, "owner": False},
            )
            ```
        """
        if representative_id is None or (isinstance(representative_id, str) and not representative_id):
            raise ValueError(f"Expected a non-empty value for `representative_id` but received {representative_id!r}")
        extra_headers = {
            **strip_not_given(
                {"Request-Id": request_id, "Correlation-Id": correlation_id, "Idempotency-Key": idempotency_key}
            ),
            **(extra_headers or {}),
        }
        return await self._put(
            path_template("/v1/representatives/{representative_id}", **{"representative_id": representative_id}),
            body=await async_maybe_transform(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "dob": dob,
                    "ssn_last4": ssn_last4,
                    "email": email,
                    "mobile_number": mobile_number,
                    "relationship": relationship,
                    "external_id": external_id,
                    "metadata": metadata,
                },
                representative_update_params.RepresentativeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepresentativeResponse,
        )

    async def retrieve(
        self,
        representative_id: str,
        *,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RepresentativeResponse:
        """
        Returns the representative with the specified ID.

        Args:
            representative_id: The ID of the representative.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RepresentativeResponse: OK

        Example:
            ```python
            representative = await client.representatives.retrieve(
                representative_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if representative_id is None or (isinstance(representative_id, str) and not representative_id):
            raise ValueError(f"Expected a non-empty value for `representative_id` but received {representative_id!r}")
        extra_headers = {
            **strip_not_given({"Request-Id": request_id, "Correlation-Id": correlation_id}),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template("/v1/representatives/{representative_id}", **{"representative_id": representative_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RepresentativeResponse,
        )

    async def list_unmasked(
        self,
        representative_id: str,
        *,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnmaskedRepresentativeResponse:
        """
        Returns the representative with the specified ID without masking sensitive fields. This endpoint requires an administrator role.

        Args:
            representative_id: The ID of the representative.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UnmaskedRepresentativeResponse: OK

        Example:
            ```python
            representative = await client.representatives.list_unmasked(
                representative_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if representative_id is None or (isinstance(representative_id, str) and not representative_id):
            raise ValueError(f"Expected a non-empty value for `representative_id` but received {representative_id!r}")
        extra_headers = {
            **strip_not_given({"Request-Id": request_id, "Correlation-Id": correlation_id}),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template("/v1/representatives/{representative_id}/unmask", **{"representative_id": representative_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnmaskedRepresentativeResponse,
        )


class RepresentativesResourceWithRawResponse:
    def __init__(self, representatives: RepresentativesResource) -> None:
        self._representatives = representatives

        self.create = to_raw_response_wrapper(
            representatives.create,
        )
        self.list = to_raw_response_wrapper(
            representatives.list,
        )
        self.update = to_raw_response_wrapper(
            representatives.update,
        )
        self.retrieve = to_raw_response_wrapper(
            representatives.retrieve,
        )
        self.list_unmasked = to_raw_response_wrapper(
            representatives.list_unmasked,
        )


class AsyncRepresentativesResourceWithRawResponse:
    def __init__(self, representatives: AsyncRepresentativesResource) -> None:
        self._representatives = representatives

        self.create = async_to_raw_response_wrapper(
            representatives.create,
        )
        self.list = async_to_raw_response_wrapper(
            representatives.list,
        )
        self.update = async_to_raw_response_wrapper(
            representatives.update,
        )
        self.retrieve = async_to_raw_response_wrapper(
            representatives.retrieve,
        )
        self.list_unmasked = async_to_raw_response_wrapper(
            representatives.list_unmasked,
        )


class RepresentativesResourceWithStreamingResponse:
    def __init__(self, representatives: RepresentativesResource) -> None:
        self._representatives = representatives

        self.create = to_streamed_response_wrapper(
            representatives.create,
        )
        self.list = to_streamed_response_wrapper(
            representatives.list,
        )
        self.update = to_streamed_response_wrapper(
            representatives.update,
        )
        self.retrieve = to_streamed_response_wrapper(
            representatives.retrieve,
        )
        self.list_unmasked = to_streamed_response_wrapper(
            representatives.list_unmasked,
        )


class AsyncRepresentativesResourceWithStreamingResponse:
    def __init__(self, representatives: AsyncRepresentativesResource) -> None:
        self._representatives = representatives

        self.create = async_to_streamed_response_wrapper(
            representatives.create,
        )
        self.list = async_to_streamed_response_wrapper(
            representatives.list,
        )
        self.update = async_to_streamed_response_wrapper(
            representatives.update,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            representatives.retrieve,
        )
        self.list_unmasked = async_to_streamed_response_wrapper(
            representatives.list_unmasked,
        )

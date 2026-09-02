# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

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
from ..types.capability_request_list import CapabilityRequestList
from ..types import capability_request_create_params, capability_request_list_params

__all__ = ["CapabilityRequestsResource", "AsyncCapabilityRequestsResource"]


class CapabilityRequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CapabilityRequestsResourceWithRawResponse:
        return CapabilityRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CapabilityRequestsResourceWithStreamingResponse:
        return CapabilityRequestsResourceWithStreamingResponse(self)

    def create(
        self,
        account_id: str,
        *,
        charges: capability_request_create_params.Charges | Omit = omit,
        payouts: capability_request_create_params.Payouts | Omit = omit,
        internet: capability_request_create_params.Internet | Omit = omit,
        individuals: capability_request_create_params.Individuals | Omit = omit,
        businesses: capability_request_create_params.Businesses | Omit = omit,
        signed_agreement: capability_request_create_params.SignedAgreement | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CapabilityRequestList:
        """
        Creates one or more capability requests for an account and returns the resulting requests.

        Args:
            account_id: The ID of the account.
            charges: Requested charge capability and limits.
            payouts: Requested payout capability and limits.
            internet: Request to enable or disable internet and mobile payment authorization.
            individuals: Request to enable or disable payments from individuals.
            businesses: Request to enable or disable payments from businesses.
            signed_agreement: Request to enable or disable signed-agreement payment authorization.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CapabilityRequestList: Created

        Example:
            ```python
            capability_request = client.capability_requests.create(
                account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if account_id is None or (isinstance(account_id, str) and not account_id):
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {
            **strip_not_given(
                {"Request-Id": request_id, "Correlation-Id": correlation_id, "Idempotency-Key": idempotency_key}
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/v1/accounts/{account_id}/capability_requests", **{"account_id": account_id}),
            body=maybe_transform(
                {
                    "charges": charges,
                    "payouts": payouts,
                    "internet": internet,
                    "individuals": individuals,
                    "businesses": businesses,
                    "signed_agreement": signed_agreement,
                },
                capability_request_create_params.CapabilityRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CapabilityRequestList,
        )

    def list(
        self,
        account_id: str,
        *,
        type: Literal["charges", "payouts", "individuals", "businesses", "signed_agreement", "internet"] | Omit = omit,
        category: Literal["payment_type", "customer_type", "consent_type"] | Omit = omit,
        status: Literal["active", "inactive", "in_review", "rejected"] | Omit = omit,
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
    ) -> CapabilityRequestList:
        """
        Returns a paginated list of capability requests for an account. Filter the list by capability type, category, or status.

        Args:
            account_id: The ID of the account.
            type: Capability type to return.
            category: Capability category to return.
            status: Capability request status to return.
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
            CapabilityRequestList: OK

        Example:
            ```python
            capability_request = client.capability_requests.list(
                account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                page_number=1,
                page_size=100,
                sort_by="id",
                sort_order="asc",
            )
            ```
        """
        if account_id is None or (isinstance(account_id, str) and not account_id):
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {
            **strip_not_given({"Request-Id": request_id, "Correlation-Id": correlation_id}),
            **(extra_headers or {}),
        }
        return self._get(
            path_template("/v1/accounts/{account_id}/capability_requests", **{"account_id": account_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "type": type,
                        "category": category,
                        "status": status,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    capability_request_list_params.CapabilityRequestListParams,
                ),
            ),
            cast_to=CapabilityRequestList,
        )


class AsyncCapabilityRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCapabilityRequestsResourceWithRawResponse:
        return AsyncCapabilityRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCapabilityRequestsResourceWithStreamingResponse:
        return AsyncCapabilityRequestsResourceWithStreamingResponse(self)

    async def create(
        self,
        account_id: str,
        *,
        charges: capability_request_create_params.Charges | Omit = omit,
        payouts: capability_request_create_params.Payouts | Omit = omit,
        internet: capability_request_create_params.Internet | Omit = omit,
        individuals: capability_request_create_params.Individuals | Omit = omit,
        businesses: capability_request_create_params.Businesses | Omit = omit,
        signed_agreement: capability_request_create_params.SignedAgreement | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CapabilityRequestList:
        """
        Creates one or more capability requests for an account and returns the resulting requests.

        Args:
            account_id: The ID of the account.
            charges: Requested charge capability and limits.
            payouts: Requested payout capability and limits.
            internet: Request to enable or disable internet and mobile payment authorization.
            individuals: Request to enable or disable payments from individuals.
            businesses: Request to enable or disable payments from businesses.
            signed_agreement: Request to enable or disable signed-agreement payment authorization.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CapabilityRequestList: Created

        Example:
            ```python
            capability_request = await client.capability_requests.create(
                account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if account_id is None or (isinstance(account_id, str) and not account_id):
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {
            **strip_not_given(
                {"Request-Id": request_id, "Correlation-Id": correlation_id, "Idempotency-Key": idempotency_key}
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/v1/accounts/{account_id}/capability_requests", **{"account_id": account_id}),
            body=await async_maybe_transform(
                {
                    "charges": charges,
                    "payouts": payouts,
                    "internet": internet,
                    "individuals": individuals,
                    "businesses": businesses,
                    "signed_agreement": signed_agreement,
                },
                capability_request_create_params.CapabilityRequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CapabilityRequestList,
        )

    async def list(
        self,
        account_id: str,
        *,
        type: Literal["charges", "payouts", "individuals", "businesses", "signed_agreement", "internet"] | Omit = omit,
        category: Literal["payment_type", "customer_type", "consent_type"] | Omit = omit,
        status: Literal["active", "inactive", "in_review", "rejected"] | Omit = omit,
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
    ) -> CapabilityRequestList:
        """
        Returns a paginated list of capability requests for an account. Filter the list by capability type, category, or status.

        Args:
            account_id: The ID of the account.
            type: Capability type to return.
            category: Capability category to return.
            status: Capability request status to return.
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
            CapabilityRequestList: OK

        Example:
            ```python
            capability_request = await client.capability_requests.list(
                account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                page_number=1,
                page_size=100,
                sort_by="id",
                sort_order="asc",
            )
            ```
        """
        if account_id is None or (isinstance(account_id, str) and not account_id):
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {
            **strip_not_given({"Request-Id": request_id, "Correlation-Id": correlation_id}),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template("/v1/accounts/{account_id}/capability_requests", **{"account_id": account_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "type": type,
                        "category": category,
                        "status": status,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    capability_request_list_params.CapabilityRequestListParams,
                ),
            ),
            cast_to=CapabilityRequestList,
        )


class CapabilityRequestsResourceWithRawResponse:
    def __init__(self, capability_requests: CapabilityRequestsResource) -> None:
        self._capability_requests = capability_requests

        self.create = to_raw_response_wrapper(
            capability_requests.create,
        )
        self.list = to_raw_response_wrapper(
            capability_requests.list,
        )


class AsyncCapabilityRequestsResourceWithRawResponse:
    def __init__(self, capability_requests: AsyncCapabilityRequestsResource) -> None:
        self._capability_requests = capability_requests

        self.create = async_to_raw_response_wrapper(
            capability_requests.create,
        )
        self.list = async_to_raw_response_wrapper(
            capability_requests.list,
        )


class CapabilityRequestsResourceWithStreamingResponse:
    def __init__(self, capability_requests: CapabilityRequestsResource) -> None:
        self._capability_requests = capability_requests

        self.create = to_streamed_response_wrapper(
            capability_requests.create,
        )
        self.list = to_streamed_response_wrapper(
            capability_requests.list,
        )


class AsyncCapabilityRequestsResourceWithStreamingResponse:
    def __init__(self, capability_requests: AsyncCapabilityRequestsResource) -> None:
        self._capability_requests = capability_requests

        self.create = async_to_streamed_response_wrapper(
            capability_requests.create,
        )
        self.list = async_to_streamed_response_wrapper(
            capability_requests.list,
        )

# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List, Optional, Union
from datetime import datetime
from typing_extensions import Literal

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform, strip_not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .review import (
    ReviewResource,
    AsyncReviewResource,
    ReviewResourceWithRawResponse,
    AsyncReviewResourceWithRawResponse,
    ReviewResourceWithStreamingResponse,
    AsyncReviewResourceWithStreamingResponse,
)
from ...types.paykey_response import PaykeyResponse
from ...types.unmasked_paykey_response import UnmaskedPaykeyResponse
from ...types.paykey_summary_list import PaykeySummaryList
from ...types.paykey_status import PaykeyStatus
from ...types.sort_order import SortOrder
from ...types.paykey_source import PaykeySource
from ...types import paykey_list_params, paykey_cancel_params, paykey_unblock_params
from ...types.revealed_paykey_response import RevealedPaykeyResponse

__all__ = ["PaykeysResource", "AsyncPaykeysResource"]


class PaykeysResource(SyncAPIResource):
    @cached_property
    def review(self) -> ReviewResource:
        return ReviewResource(self._client)

    @cached_property
    def with_raw_response(self) -> PaykeysResourceWithRawResponse:
        return PaykeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaykeysResourceWithStreamingResponse:
        return PaykeysResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaykeyResponse:
        """
        Returns a paykey by `id`, including the masked paykey value and bank account details.

        Args:
            id: Unique identifier for the paykey.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaykeyResponse: OK

        Example:
            ```python
            paykey = client.paykeys.retrieve(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {"Straddle-Account-Id": straddle_account_id, "Request-Id": request_id, "Correlation-Id": correlation_id}
            ),
            **(extra_headers or {}),
        }
        return self._get(
            path_template("/v1/paykeys/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaykeyResponse,
        )

    def list_unmasked(
        self,
        id: str,
        *,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnmaskedPaykeyResponse:
        """
        Returns a paykey by `id`, including the full paykey value and unmasked bank account details. Straddle must enable this endpoint for your account. Use this endpoint only when unmasked data is necessary.

        Args:
            id: Unique identifier for the paykey.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UnmaskedPaykeyResponse: OK

        Example:
            ```python
            paykey = client.paykeys.list_unmasked(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {"Straddle-Account-Id": straddle_account_id, "Request-Id": request_id, "Correlation-Id": correlation_id}
            ),
            **(extra_headers or {}),
        }
        return self._get(
            path_template("/v1/paykeys/{id}/unmasked", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnmaskedPaykeyResponse,
        )

    def list(
        self,
        *,
        customer_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        status: List[PaykeyStatus] | Omit = omit,
        sort_by: Literal["institution_name", "expires_at", "created_at"] | Omit = omit,
        sort_order: SortOrder | Omit = omit,
        source: List[PaykeySource] | Omit = omit,
        unblock_eligible: bool | Omit = omit,
        search_text: str | Omit = omit,
        created_from: Union[str, datetime] | Omit = omit,
        created_to: Union[str, datetime] | Omit = omit,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaykeySummaryList:
        """
        Returns a paginated list of paykeys for the account. Optional query parameters filter, search, and sort the results.

        Args:
            customer_id: Filter paykeys by related customer ID.
            page_number: Page number for paginated results. Starts at 1.
            page_size: Number of results per page. Maximum: 1000.
            status: Filter paykeys by their current status.
            sort_by: Field used to sort the results.
            sort_order: Order in which to sort the results.
            source: Filter paykeys by their source.
            unblock_eligible: Filters paykeys by unblock eligibility. `true` returns blocked paykeys that are eligible because of an `R29` return and have not been unblocked before. `false` returns blocked paykeys that are not eligible.
            search_text: General search term to filter paykeys.
            created_from: Start date for filtering by creation date.
            created_to: End date for filtering by creation date.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaykeySummaryList: OK

        Example:
            ```python
            paykey = client.paykeys.list(
                page_number=1,
                page_size=100,
                sort_order="asc",
            )
            ```
        """
        extra_headers = {
            **strip_not_given(
                {"Straddle-Account-Id": straddle_account_id, "Request-Id": request_id, "Correlation-Id": correlation_id}
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/v1/paykeys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "customer_id": customer_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "status": status,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "source": source,
                        "unblock_eligible": unblock_eligible,
                        "search_text": search_text,
                        "created_from": created_from,
                        "created_to": created_to,
                    },
                    paykey_list_params.PaykeyListParams,
                ),
            ),
            cast_to=PaykeySummaryList,
        )

    def reveal(
        self,
        id: str,
        *,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RevealedPaykeyResponse:
        """
        Returns a paykey by `id`, including the full paykey value and masked bank account details.

        Args:
            id: Unique identifier for the paykey.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RevealedPaykeyResponse: OK

        Example:
            ```python
            paykey = client.paykeys.reveal(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {"Straddle-Account-Id": straddle_account_id, "Request-Id": request_id, "Correlation-Id": correlation_id}
            ),
            **(extra_headers or {}),
        }
        return self._get(
            path_template("/v1/paykeys/{id}/reveal", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RevealedPaykeyResponse,
        )

    def cancel(
        self,
        id: str,
        *,
        reason: Optional[str] | Omit = omit,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaykeyResponse:
        """
        Cancels a paykey so it cannot be used for new payments.

        Args:
            id: Unique identifier for the paykey.
            reason: Reason for canceling the paykey.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaykeyResponse: OK

        Example:
            ```python
            paykey = client.paykeys.cancel(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Straddle-Account-Id": straddle_account_id,
                    "Request-Id": request_id,
                    "Correlation-Id": correlation_id,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._put(
            path_template("/v1/paykeys/{id}/cancel", **{"id": id}),
            body=maybe_transform(
                {"reason": reason},
                paykey_cancel_params.PaykeyCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaykeyResponse,
        )

    def refresh_review(
        self,
        id: str,
        *,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaykeyResponse:
        """
        Starts a new verification review for a paykey. The review runs asynchronously. Webhooks and the paykey review endpoint return updated results.

        Args:
            id: Unique identifier for the paykey.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaykeyResponse: Accepted

        Example:
            ```python
            paykey = client.paykeys.refresh_review(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Straddle-Account-Id": straddle_account_id,
                    "Request-Id": request_id,
                    "Correlation-Id": correlation_id,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._put(
            path_template("/v1/paykeys/{id}/refresh_review", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaykeyResponse,
        )

    def refresh_balance(
        self,
        id: str,
        *,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaykeyResponse:
        """
        Starts an asynchronous balance refresh for a paykey. The response returns the paykey before the refresh finishes.

        Args:
            id: Unique identifier for the paykey.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaykeyResponse: Accepted

        Example:
            ```python
            paykey = client.paykeys.refresh_balance(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Straddle-Account-Id": straddle_account_id,
                    "Request-Id": request_id,
                    "Correlation-Id": correlation_id,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._put(
            path_template("/v1/paykeys/{id}/refresh_balance", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaykeyResponse,
        )

    def unblock(
        self,
        id: str,
        *,
        message: Optional[str] | Omit = omit,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaykeyResponse:
        """
        Unblocks a paykey that was blocked by an `R29` return. The paykey must not have been unblocked before.

        Args:
            id: Unique identifier for the paykey.
            message: Optional message describing the reason for unblocking.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaykeyResponse: OK

        Example:
            ```python
            paykey = client.paykeys.unblock(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Straddle-Account-Id": straddle_account_id,
                    "Request-Id": request_id,
                    "Correlation-Id": correlation_id,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._patch(
            path_template("/v1/paykeys/{id}/unblock", **{"id": id}),
            body=maybe_transform(
                {"message": message},
                paykey_unblock_params.PaykeyUnblockParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaykeyResponse,
        )


class AsyncPaykeysResource(AsyncAPIResource):
    @cached_property
    def review(self) -> AsyncReviewResource:
        return AsyncReviewResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPaykeysResourceWithRawResponse:
        return AsyncPaykeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaykeysResourceWithStreamingResponse:
        return AsyncPaykeysResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaykeyResponse:
        """
        Returns a paykey by `id`, including the masked paykey value and bank account details.

        Args:
            id: Unique identifier for the paykey.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaykeyResponse: OK

        Example:
            ```python
            paykey = await client.paykeys.retrieve(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {"Straddle-Account-Id": straddle_account_id, "Request-Id": request_id, "Correlation-Id": correlation_id}
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template("/v1/paykeys/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaykeyResponse,
        )

    async def list_unmasked(
        self,
        id: str,
        *,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnmaskedPaykeyResponse:
        """
        Returns a paykey by `id`, including the full paykey value and unmasked bank account details. Straddle must enable this endpoint for your account. Use this endpoint only when unmasked data is necessary.

        Args:
            id: Unique identifier for the paykey.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UnmaskedPaykeyResponse: OK

        Example:
            ```python
            paykey = await client.paykeys.list_unmasked(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {"Straddle-Account-Id": straddle_account_id, "Request-Id": request_id, "Correlation-Id": correlation_id}
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template("/v1/paykeys/{id}/unmasked", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnmaskedPaykeyResponse,
        )

    async def list(
        self,
        *,
        customer_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        status: List[PaykeyStatus] | Omit = omit,
        sort_by: Literal["institution_name", "expires_at", "created_at"] | Omit = omit,
        sort_order: SortOrder | Omit = omit,
        source: List[PaykeySource] | Omit = omit,
        unblock_eligible: bool | Omit = omit,
        search_text: str | Omit = omit,
        created_from: Union[str, datetime] | Omit = omit,
        created_to: Union[str, datetime] | Omit = omit,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaykeySummaryList:
        """
        Returns a paginated list of paykeys for the account. Optional query parameters filter, search, and sort the results.

        Args:
            customer_id: Filter paykeys by related customer ID.
            page_number: Page number for paginated results. Starts at 1.
            page_size: Number of results per page. Maximum: 1000.
            status: Filter paykeys by their current status.
            sort_by: Field used to sort the results.
            sort_order: Order in which to sort the results.
            source: Filter paykeys by their source.
            unblock_eligible: Filters paykeys by unblock eligibility. `true` returns blocked paykeys that are eligible because of an `R29` return and have not been unblocked before. `false` returns blocked paykeys that are not eligible.
            search_text: General search term to filter paykeys.
            created_from: Start date for filtering by creation date.
            created_to: End date for filtering by creation date.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaykeySummaryList: OK

        Example:
            ```python
            paykey = await client.paykeys.list(
                page_number=1,
                page_size=100,
                sort_order="asc",
            )
            ```
        """
        extra_headers = {
            **strip_not_given(
                {"Straddle-Account-Id": straddle_account_id, "Request-Id": request_id, "Correlation-Id": correlation_id}
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/v1/paykeys",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "customer_id": customer_id,
                        "page_number": page_number,
                        "page_size": page_size,
                        "status": status,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "source": source,
                        "unblock_eligible": unblock_eligible,
                        "search_text": search_text,
                        "created_from": created_from,
                        "created_to": created_to,
                    },
                    paykey_list_params.PaykeyListParams,
                ),
            ),
            cast_to=PaykeySummaryList,
        )

    async def reveal(
        self,
        id: str,
        *,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RevealedPaykeyResponse:
        """
        Returns a paykey by `id`, including the full paykey value and masked bank account details.

        Args:
            id: Unique identifier for the paykey.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RevealedPaykeyResponse: OK

        Example:
            ```python
            paykey = await client.paykeys.reveal(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {"Straddle-Account-Id": straddle_account_id, "Request-Id": request_id, "Correlation-Id": correlation_id}
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template("/v1/paykeys/{id}/reveal", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RevealedPaykeyResponse,
        )

    async def cancel(
        self,
        id: str,
        *,
        reason: Optional[str] | Omit = omit,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaykeyResponse:
        """
        Cancels a paykey so it cannot be used for new payments.

        Args:
            id: Unique identifier for the paykey.
            reason: Reason for canceling the paykey.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaykeyResponse: OK

        Example:
            ```python
            paykey = await client.paykeys.cancel(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Straddle-Account-Id": straddle_account_id,
                    "Request-Id": request_id,
                    "Correlation-Id": correlation_id,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._put(
            path_template("/v1/paykeys/{id}/cancel", **{"id": id}),
            body=await async_maybe_transform(
                {"reason": reason},
                paykey_cancel_params.PaykeyCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaykeyResponse,
        )

    async def refresh_review(
        self,
        id: str,
        *,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaykeyResponse:
        """
        Starts a new verification review for a paykey. The review runs asynchronously. Webhooks and the paykey review endpoint return updated results.

        Args:
            id: Unique identifier for the paykey.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaykeyResponse: Accepted

        Example:
            ```python
            paykey = await client.paykeys.refresh_review(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Straddle-Account-Id": straddle_account_id,
                    "Request-Id": request_id,
                    "Correlation-Id": correlation_id,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._put(
            path_template("/v1/paykeys/{id}/refresh_review", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaykeyResponse,
        )

    async def refresh_balance(
        self,
        id: str,
        *,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaykeyResponse:
        """
        Starts an asynchronous balance refresh for a paykey. The response returns the paykey before the refresh finishes.

        Args:
            id: Unique identifier for the paykey.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaykeyResponse: Accepted

        Example:
            ```python
            paykey = await client.paykeys.refresh_balance(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Straddle-Account-Id": straddle_account_id,
                    "Request-Id": request_id,
                    "Correlation-Id": correlation_id,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._put(
            path_template("/v1/paykeys/{id}/refresh_balance", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaykeyResponse,
        )

    async def unblock(
        self,
        id: str,
        *,
        message: Optional[str] | Omit = omit,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaykeyResponse:
        """
        Unblocks a paykey that was blocked by an `R29` return. The paykey must not have been unblocked before.

        Args:
            id: Unique identifier for the paykey.
            message: Optional message describing the reason for unblocking.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaykeyResponse: OK

        Example:
            ```python
            paykey = await client.paykeys.unblock(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if id is None or (isinstance(id, str) and not id):
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Straddle-Account-Id": straddle_account_id,
                    "Request-Id": request_id,
                    "Correlation-Id": correlation_id,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._patch(
            path_template("/v1/paykeys/{id}/unblock", **{"id": id}),
            body=await async_maybe_transform(
                {"message": message},
                paykey_unblock_params.PaykeyUnblockParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaykeyResponse,
        )


class PaykeysResourceWithRawResponse:
    def __init__(self, paykeys: PaykeysResource) -> None:
        self._paykeys = paykeys

        self.retrieve = to_raw_response_wrapper(
            paykeys.retrieve,
        )
        self.list_unmasked = to_raw_response_wrapper(
            paykeys.list_unmasked,
        )
        self.list = to_raw_response_wrapper(
            paykeys.list,
        )
        self.reveal = to_raw_response_wrapper(
            paykeys.reveal,
        )
        self.cancel = to_raw_response_wrapper(
            paykeys.cancel,
        )
        self.refresh_review = to_raw_response_wrapper(
            paykeys.refresh_review,
        )
        self.refresh_balance = to_raw_response_wrapper(
            paykeys.refresh_balance,
        )
        self.unblock = to_raw_response_wrapper(
            paykeys.unblock,
        )

    @cached_property
    def review(self) -> ReviewResourceWithRawResponse:
        return ReviewResourceWithRawResponse(self._paykeys.review)


class AsyncPaykeysResourceWithRawResponse:
    def __init__(self, paykeys: AsyncPaykeysResource) -> None:
        self._paykeys = paykeys

        self.retrieve = async_to_raw_response_wrapper(
            paykeys.retrieve,
        )
        self.list_unmasked = async_to_raw_response_wrapper(
            paykeys.list_unmasked,
        )
        self.list = async_to_raw_response_wrapper(
            paykeys.list,
        )
        self.reveal = async_to_raw_response_wrapper(
            paykeys.reveal,
        )
        self.cancel = async_to_raw_response_wrapper(
            paykeys.cancel,
        )
        self.refresh_review = async_to_raw_response_wrapper(
            paykeys.refresh_review,
        )
        self.refresh_balance = async_to_raw_response_wrapper(
            paykeys.refresh_balance,
        )
        self.unblock = async_to_raw_response_wrapper(
            paykeys.unblock,
        )

    @cached_property
    def review(self) -> AsyncReviewResourceWithRawResponse:
        return AsyncReviewResourceWithRawResponse(self._paykeys.review)


class PaykeysResourceWithStreamingResponse:
    def __init__(self, paykeys: PaykeysResource) -> None:
        self._paykeys = paykeys

        self.retrieve = to_streamed_response_wrapper(
            paykeys.retrieve,
        )
        self.list_unmasked = to_streamed_response_wrapper(
            paykeys.list_unmasked,
        )
        self.list = to_streamed_response_wrapper(
            paykeys.list,
        )
        self.reveal = to_streamed_response_wrapper(
            paykeys.reveal,
        )
        self.cancel = to_streamed_response_wrapper(
            paykeys.cancel,
        )
        self.refresh_review = to_streamed_response_wrapper(
            paykeys.refresh_review,
        )
        self.refresh_balance = to_streamed_response_wrapper(
            paykeys.refresh_balance,
        )
        self.unblock = to_streamed_response_wrapper(
            paykeys.unblock,
        )

    @cached_property
    def review(self) -> ReviewResourceWithStreamingResponse:
        return ReviewResourceWithStreamingResponse(self._paykeys.review)


class AsyncPaykeysResourceWithStreamingResponse:
    def __init__(self, paykeys: AsyncPaykeysResource) -> None:
        self._paykeys = paykeys

        self.retrieve = async_to_streamed_response_wrapper(
            paykeys.retrieve,
        )
        self.list_unmasked = async_to_streamed_response_wrapper(
            paykeys.list_unmasked,
        )
        self.list = async_to_streamed_response_wrapper(
            paykeys.list,
        )
        self.reveal = async_to_streamed_response_wrapper(
            paykeys.reveal,
        )
        self.cancel = async_to_streamed_response_wrapper(
            paykeys.cancel,
        )
        self.refresh_review = async_to_streamed_response_wrapper(
            paykeys.refresh_review,
        )
        self.refresh_balance = async_to_streamed_response_wrapper(
            paykeys.refresh_balance,
        )
        self.unblock = async_to_streamed_response_wrapper(
            paykeys.unblock,
        )

    @cached_property
    def review(self) -> AsyncReviewResourceWithStreamingResponse:
        return AsyncReviewResourceWithStreamingResponse(self._paykeys.review)

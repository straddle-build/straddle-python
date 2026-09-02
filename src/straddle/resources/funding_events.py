# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List, Optional, Union
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
from ..types.funding_event_summary_list import FundingEventSummaryList
from ..types.sort_order import SortOrder
from ..types.transfer_direction import TransferDirection
from ..types.funding_event_type import FundingEventType
from ..types.payment_status import PaymentStatus
from ..types.payment_status_reason import PaymentStatusReason
from ..types.payment_status_source import PaymentStatusSource
from ..types import funding_event_list_params, funding_event_simulate_params, funding_event_list_payments_params
from ..types.funding_event_response import FundingEventResponse
from ..types.funding_event_simulation import FundingEventSimulation
from ..types.simulated_payment_outcome import SimulatedPaymentOutcome
from ..types.funding_event_payment_list import FundingEventPaymentList

__all__ = ["FundingEventsResource", "AsyncFundingEventsResource"]


class FundingEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FundingEventsResourceWithRawResponse:
        return FundingEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FundingEventsResourceWithStreamingResponse:
        return FundingEventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: Literal["transfer_date", "id", "amount"] | Omit = omit,
        sort_order: SortOrder | Omit = omit,
        created_from: Optional[Union[str, date]] | Omit = omit,
        created_to: Optional[Union[str, date]] | Omit = omit,
        direction: TransferDirection | Omit = omit,
        event_type: FundingEventType | Omit = omit,
        trace_number: Optional[str] | Omit = omit,
        search_text: Optional[str] | Omit = omit,
        status: Optional[List[PaymentStatus]] | Omit = omit,
        trace_id: Optional[str] | Omit = omit,
        status_reason: Optional[List[PaymentStatusReason]] | Omit = omit,
        status_source: Optional[List[PaymentStatusSource]] | Omit = omit,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundingEventSummaryList:
        """
        Returns a paginated list of funding events that match the specified filters.

        Args:
            page_number: Results page number. Starts at page 1.
            page_size: Results page size. Max value: 1000.
            sort_by: Field used to sort the results.
            sort_order: Order in which to sort the results.
            created_from: Filter to funding events created on or after this date.
            created_to: Filter to funding events created on or before this date.
            direction: Filter by transfer direction relative to the linked bank account.
            event_type: Filter by funding event type.
            trace_number: Filter by a network trace number assigned during processing.
            search_text: Free-text search across funding event fields.
            status: Filter by funding event status.
            trace_id: Filter by a network-level trace identifier assigned during processing.
            status_reason: Filter by the reason for the most recent status change.
            status_source: Filter by the source of the most recent status change.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FundingEventSummaryList: OK

        Example:
            ```python
            funding_event = client.funding_events.list(
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
            "/v1/funding_events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "created_from": created_from,
                        "created_to": created_to,
                        "direction": direction,
                        "event_type": event_type,
                        "trace_number": trace_number,
                        "search_text": search_text,
                        "status": status,
                        "trace_id": trace_id,
                        "status_reason": status_reason,
                        "status_source": status_source,
                    },
                    funding_event_list_params.FundingEventListParams,
                ),
            ),
            cast_to=FundingEventSummaryList,
        )

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
    ) -> FundingEventResponse:
        """
        Returns a funding event by its unique identifier, including its current status, status history, and linked bank account details when available.

        Args:
            id: Unique identifier for the funding event.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FundingEventResponse: OK

        Example:
            ```python
            funding_event = client.funding_events.retrieve(
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
            path_template("/v1/funding_events/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FundingEventResponse,
        )

    def simulate(
        self,
        *,
        funding_event_job_type: Literal["charges", "payouts"],
        sandbox_outcome: SimulatedPaymentOutcome | Omit = omit,
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
    ) -> FundingEventSimulation:
        """
        Creates a funding event for unfunded charge or payout activity in the sandbox and returns its ID. This endpoint is unavailable in production.

        Args:
            funding_event_job_type: Required. Selects charge or payout activity for the simulated funding event.
            sandbox_outcome: Optional. Sets the processing outcome for the simulated funding event. Defaults to `standard`.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FundingEventSimulation: Created

        Example:
            ```python
            funding_event = client.funding_events.simulate(
                funding_event_job_type="charges",
            )
            ```
        """
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
        return self._post(
            "/v1/funding_events/simulate",
            body=maybe_transform(
                {
                    "funding_event_job_type": funding_event_job_type,
                    "sandbox_outcome": sandbox_outcome,
                },
                funding_event_simulate_params.FundingEventSimulateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FundingEventSimulation,
        )

    def list_payments(
        self,
        id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        include_metadata: bool | Omit = omit,
        default_page_size: int | Omit = omit,
        default_sort: Literal["created_at", "payment_date", "effective_at", "id"] | Omit = omit,
        default_sort_order: SortOrder | Omit = omit,
        sort_by: Literal["created_at", "payment_date", "effective_at", "id"] | Omit = omit,
        sort_order: SortOrder | Omit = omit,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundingEventPaymentList:
        """
        Returns a paginated list of payments included in the funding event.

        Args:
            id: Unique identifier for the funding event.
            page_number: Results page number. Starts at 1. Defaults to 1.
            page_size: Number of results per page. Maximum 1,000. Defaults to 100.
            include_metadata: When `true`, includes each payment's metadata. Defaults to `false`.
            default_page_size: Default number of results returned per page.
            default_sort: Default field used to sort the results.
            default_sort_order: Default order in which to sort the results.
            sort_by: Field used to sort the results.
            sort_order: Order in which to sort the results.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FundingEventPaymentList: OK

        Example:
            ```python
            funding_event = client.funding_events.list_payments(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                default_sort_order="asc",
                sort_order="asc",
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
            path_template("/v1/funding_event_payments/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "include_metadata": include_metadata,
                        "default_page_size": default_page_size,
                        "default_sort": default_sort,
                        "default_sort_order": default_sort_order,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    funding_event_list_payments_params.FundingEventListPaymentsParams,
                ),
            ),
            cast_to=FundingEventPaymentList,
        )


class AsyncFundingEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFundingEventsResourceWithRawResponse:
        return AsyncFundingEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFundingEventsResourceWithStreamingResponse:
        return AsyncFundingEventsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: Literal["transfer_date", "id", "amount"] | Omit = omit,
        sort_order: SortOrder | Omit = omit,
        created_from: Optional[Union[str, date]] | Omit = omit,
        created_to: Optional[Union[str, date]] | Omit = omit,
        direction: TransferDirection | Omit = omit,
        event_type: FundingEventType | Omit = omit,
        trace_number: Optional[str] | Omit = omit,
        search_text: Optional[str] | Omit = omit,
        status: Optional[List[PaymentStatus]] | Omit = omit,
        trace_id: Optional[str] | Omit = omit,
        status_reason: Optional[List[PaymentStatusReason]] | Omit = omit,
        status_source: Optional[List[PaymentStatusSource]] | Omit = omit,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundingEventSummaryList:
        """
        Returns a paginated list of funding events that match the specified filters.

        Args:
            page_number: Results page number. Starts at page 1.
            page_size: Results page size. Max value: 1000.
            sort_by: Field used to sort the results.
            sort_order: Order in which to sort the results.
            created_from: Filter to funding events created on or after this date.
            created_to: Filter to funding events created on or before this date.
            direction: Filter by transfer direction relative to the linked bank account.
            event_type: Filter by funding event type.
            trace_number: Filter by a network trace number assigned during processing.
            search_text: Free-text search across funding event fields.
            status: Filter by funding event status.
            trace_id: Filter by a network-level trace identifier assigned during processing.
            status_reason: Filter by the reason for the most recent status change.
            status_source: Filter by the source of the most recent status change.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FundingEventSummaryList: OK

        Example:
            ```python
            funding_event = await client.funding_events.list(
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
            "/v1/funding_events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "created_from": created_from,
                        "created_to": created_to,
                        "direction": direction,
                        "event_type": event_type,
                        "trace_number": trace_number,
                        "search_text": search_text,
                        "status": status,
                        "trace_id": trace_id,
                        "status_reason": status_reason,
                        "status_source": status_source,
                    },
                    funding_event_list_params.FundingEventListParams,
                ),
            ),
            cast_to=FundingEventSummaryList,
        )

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
    ) -> FundingEventResponse:
        """
        Returns a funding event by its unique identifier, including its current status, status history, and linked bank account details when available.

        Args:
            id: Unique identifier for the funding event.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FundingEventResponse: OK

        Example:
            ```python
            funding_event = await client.funding_events.retrieve(
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
            path_template("/v1/funding_events/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FundingEventResponse,
        )

    async def simulate(
        self,
        *,
        funding_event_job_type: Literal["charges", "payouts"],
        sandbox_outcome: SimulatedPaymentOutcome | Omit = omit,
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
    ) -> FundingEventSimulation:
        """
        Creates a funding event for unfunded charge or payout activity in the sandbox and returns its ID. This endpoint is unavailable in production.

        Args:
            funding_event_job_type: Required. Selects charge or payout activity for the simulated funding event.
            sandbox_outcome: Optional. Sets the processing outcome for the simulated funding event. Defaults to `standard`.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FundingEventSimulation: Created

        Example:
            ```python
            funding_event = await client.funding_events.simulate(
                funding_event_job_type="charges",
            )
            ```
        """
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
        return await self._post(
            "/v1/funding_events/simulate",
            body=await async_maybe_transform(
                {
                    "funding_event_job_type": funding_event_job_type,
                    "sandbox_outcome": sandbox_outcome,
                },
                funding_event_simulate_params.FundingEventSimulateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FundingEventSimulation,
        )

    async def list_payments(
        self,
        id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        include_metadata: bool | Omit = omit,
        default_page_size: int | Omit = omit,
        default_sort: Literal["created_at", "payment_date", "effective_at", "id"] | Omit = omit,
        default_sort_order: SortOrder | Omit = omit,
        sort_by: Literal["created_at", "payment_date", "effective_at", "id"] | Omit = omit,
        sort_order: SortOrder | Omit = omit,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundingEventPaymentList:
        """
        Returns a paginated list of payments included in the funding event.

        Args:
            id: Unique identifier for the funding event.
            page_number: Results page number. Starts at 1. Defaults to 1.
            page_size: Number of results per page. Maximum 1,000. Defaults to 100.
            include_metadata: When `true`, includes each payment's metadata. Defaults to `false`.
            default_page_size: Default number of results returned per page.
            default_sort: Default field used to sort the results.
            default_sort_order: Default order in which to sort the results.
            sort_by: Field used to sort the results.
            sort_order: Order in which to sort the results.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            FundingEventPaymentList: OK

        Example:
            ```python
            funding_event = await client.funding_events.list_payments(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                default_sort_order="asc",
                sort_order="asc",
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
            path_template("/v1/funding_event_payments/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "include_metadata": include_metadata,
                        "default_page_size": default_page_size,
                        "default_sort": default_sort,
                        "default_sort_order": default_sort_order,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    funding_event_list_payments_params.FundingEventListPaymentsParams,
                ),
            ),
            cast_to=FundingEventPaymentList,
        )


class FundingEventsResourceWithRawResponse:
    def __init__(self, funding_events: FundingEventsResource) -> None:
        self._funding_events = funding_events

        self.list = to_raw_response_wrapper(
            funding_events.list,
        )
        self.retrieve = to_raw_response_wrapper(
            funding_events.retrieve,
        )
        self.simulate = to_raw_response_wrapper(
            funding_events.simulate,
        )
        self.list_payments = to_raw_response_wrapper(
            funding_events.list_payments,
        )


class AsyncFundingEventsResourceWithRawResponse:
    def __init__(self, funding_events: AsyncFundingEventsResource) -> None:
        self._funding_events = funding_events

        self.list = async_to_raw_response_wrapper(
            funding_events.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            funding_events.retrieve,
        )
        self.simulate = async_to_raw_response_wrapper(
            funding_events.simulate,
        )
        self.list_payments = async_to_raw_response_wrapper(
            funding_events.list_payments,
        )


class FundingEventsResourceWithStreamingResponse:
    def __init__(self, funding_events: FundingEventsResource) -> None:
        self._funding_events = funding_events

        self.list = to_streamed_response_wrapper(
            funding_events.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            funding_events.retrieve,
        )
        self.simulate = to_streamed_response_wrapper(
            funding_events.simulate,
        )
        self.list_payments = to_streamed_response_wrapper(
            funding_events.list_payments,
        )


class AsyncFundingEventsResourceWithStreamingResponse:
    def __init__(self, funding_events: AsyncFundingEventsResource) -> None:
        self._funding_events = funding_events

        self.list = async_to_streamed_response_wrapper(
            funding_events.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            funding_events.retrieve,
        )
        self.simulate = async_to_streamed_response_wrapper(
            funding_events.simulate,
        )
        self.list_payments = async_to_streamed_response_wrapper(
            funding_events.list_payments,
        )

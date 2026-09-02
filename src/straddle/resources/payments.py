# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import List, Union
from datetime import date, datetime
from typing_extensions import Literal

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform, strip_not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.payment_summary_list import PaymentSummaryList
from ..types.sort_order import SortOrder
from ..types.payment_type import PaymentType
from ..types.payment_status import PaymentStatus
from ..types.payment_status_reason import PaymentStatusReason
from ..types.payment_status_source import PaymentStatusSource
from ..types import payment_list_params

__all__ = ["PaymentsResource", "AsyncPaymentsResource"]


class PaymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentsResourceWithRawResponse:
        return PaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentsResourceWithStreamingResponse:
        return PaymentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: Literal["created_at", "payment_date", "effective_at", "id", "amount", "updated_at"] | Omit = omit,
        sort_order: SortOrder | Omit = omit,
        payment_type: List[PaymentType] | Omit = omit,
        payment_status: List[PaymentStatus] | Omit = omit,
        payment_id: str | Omit = omit,
        external_id: str | Omit = omit,
        customer_id: str | Omit = omit,
        paykey_id: str | Omit = omit,
        paykey: str | Omit = omit,
        min_amount: int | Omit = omit,
        max_amount: int | Omit = omit,
        min_payment_date: Union[str, date] | Omit = omit,
        max_payment_date: Union[str, date] | Omit = omit,
        min_created_at: Union[str, datetime] | Omit = omit,
        max_created_at: Union[str, datetime] | Omit = omit,
        min_effective_at: Union[str, datetime] | Omit = omit,
        max_effective_at: Union[str, datetime] | Omit = omit,
        funding_id: str | Omit = omit,
        search_text: str | Omit = omit,
        default_page_size: int | Omit = omit,
        default_sort: Literal["created_at", "payment_date", "effective_at", "id", "amount", "updated_at"] | Omit = omit,
        default_sort_order: SortOrder | Omit = omit,
        status_reason: List[PaymentStatusReason] | Omit = omit,
        status_source: List[PaymentStatusSource] | Omit = omit,
        include_metadata: bool | Omit = omit,
        is_refund: bool | Omit = omit,
        has_refund: bool | Omit = omit,
        is_resubmit: bool | Omit = omit,
        has_resubmit: bool | Omit = omit,
        min_updated_at: Union[str, datetime] | Omit = omit,
        max_updated_at: Union[str, datetime] | Omit = omit,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentSummaryList:
        """
        Returns a paged list of charges and payouts that match the filters.

        Args:
            page_number: Page number to return.
            page_size: Number of results to return per page.
            sort_by: Field used to sort the results.
            sort_order: Order in which to sort the results.
            payment_type: Filter by payment type.
            payment_status: Filter by payment status.
            payment_id: Filter by the payment's unique identifier.
            external_id: Filter by your external identifier for the payment.
            customer_id: Filter by the unique identifier of the customer.
            paykey_id: Filter by the unique identifier of the paykey.
            paykey: Filter by the paykey token.
            min_amount: Filter to payments with an amount in cents greater than or equal to this value.
            max_amount: Filter to payments with an amount in cents less than or equal to this value.
            min_payment_date: Filter to payments with a payment date on or after this date.
            max_payment_date: Filter to payments with a payment date on or before this date.
            min_created_at: Filter to payments created at or after this timestamp.
            max_created_at: Filter to payments created at or before this timestamp.
            min_effective_at: Filter to payments effective at or after this timestamp.
            max_effective_at: Filter to payments effective at or before this timestamp.
            funding_id: Filter by the unique identifier of a funding event.
            search_text: Free-text search across payment fields.
            default_page_size: Default number of results returned per page.
            default_sort: Default field used to sort the results.
            default_sort_order: Default order in which to sort the results.
            status_reason: Filter by the reason for the most recent payment status change.
            status_source: Filter by the source of the most recent payment status change.
            include_metadata: Whether to include metadata in each returned payment. Defaults to false.
            is_refund: Filter payouts by whether they refund an original charge.
            has_refund: Filter charges by whether an associated payout has refunded them.
            is_resubmit: Filter payments by whether they resubmit an original payment.
            has_resubmit: Filter payments by whether they have been resubmitted.
            min_updated_at: Filter to payments last updated on or after this timestamp.
            max_updated_at: Filter to payments last updated on or before this timestamp.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaymentSummaryList: OK

        Example:
            ```python
            payment = client.payments.list(
                page_number=1,
                page_size=100,
                sort_by="id",
                sort_order="asc",
                default_sort="id",
                default_sort_order="asc",
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
            "/v1/payments",
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
                        "payment_type": payment_type,
                        "payment_status": payment_status,
                        "payment_id": payment_id,
                        "external_id": external_id,
                        "customer_id": customer_id,
                        "paykey_id": paykey_id,
                        "paykey": paykey,
                        "min_amount": min_amount,
                        "max_amount": max_amount,
                        "min_payment_date": min_payment_date,
                        "max_payment_date": max_payment_date,
                        "min_created_at": min_created_at,
                        "max_created_at": max_created_at,
                        "min_effective_at": min_effective_at,
                        "max_effective_at": max_effective_at,
                        "funding_id": funding_id,
                        "search_text": search_text,
                        "default_page_size": default_page_size,
                        "default_sort": default_sort,
                        "default_sort_order": default_sort_order,
                        "status_reason": status_reason,
                        "status_source": status_source,
                        "include_metadata": include_metadata,
                        "is_refund": is_refund,
                        "has_refund": has_refund,
                        "is_resubmit": is_resubmit,
                        "has_resubmit": has_resubmit,
                        "min_updated_at": min_updated_at,
                        "max_updated_at": max_updated_at,
                    },
                    payment_list_params.PaymentListParams,
                ),
            ),
            cast_to=PaymentSummaryList,
        )


class AsyncPaymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentsResourceWithRawResponse:
        return AsyncPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentsResourceWithStreamingResponse:
        return AsyncPaymentsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: Literal["created_at", "payment_date", "effective_at", "id", "amount", "updated_at"] | Omit = omit,
        sort_order: SortOrder | Omit = omit,
        payment_type: List[PaymentType] | Omit = omit,
        payment_status: List[PaymentStatus] | Omit = omit,
        payment_id: str | Omit = omit,
        external_id: str | Omit = omit,
        customer_id: str | Omit = omit,
        paykey_id: str | Omit = omit,
        paykey: str | Omit = omit,
        min_amount: int | Omit = omit,
        max_amount: int | Omit = omit,
        min_payment_date: Union[str, date] | Omit = omit,
        max_payment_date: Union[str, date] | Omit = omit,
        min_created_at: Union[str, datetime] | Omit = omit,
        max_created_at: Union[str, datetime] | Omit = omit,
        min_effective_at: Union[str, datetime] | Omit = omit,
        max_effective_at: Union[str, datetime] | Omit = omit,
        funding_id: str | Omit = omit,
        search_text: str | Omit = omit,
        default_page_size: int | Omit = omit,
        default_sort: Literal["created_at", "payment_date", "effective_at", "id", "amount", "updated_at"] | Omit = omit,
        default_sort_order: SortOrder | Omit = omit,
        status_reason: List[PaymentStatusReason] | Omit = omit,
        status_source: List[PaymentStatusSource] | Omit = omit,
        include_metadata: bool | Omit = omit,
        is_refund: bool | Omit = omit,
        has_refund: bool | Omit = omit,
        is_resubmit: bool | Omit = omit,
        has_resubmit: bool | Omit = omit,
        min_updated_at: Union[str, datetime] | Omit = omit,
        max_updated_at: Union[str, datetime] | Omit = omit,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentSummaryList:
        """
        Returns a paged list of charges and payouts that match the filters.

        Args:
            page_number: Page number to return.
            page_size: Number of results to return per page.
            sort_by: Field used to sort the results.
            sort_order: Order in which to sort the results.
            payment_type: Filter by payment type.
            payment_status: Filter by payment status.
            payment_id: Filter by the payment's unique identifier.
            external_id: Filter by your external identifier for the payment.
            customer_id: Filter by the unique identifier of the customer.
            paykey_id: Filter by the unique identifier of the paykey.
            paykey: Filter by the paykey token.
            min_amount: Filter to payments with an amount in cents greater than or equal to this value.
            max_amount: Filter to payments with an amount in cents less than or equal to this value.
            min_payment_date: Filter to payments with a payment date on or after this date.
            max_payment_date: Filter to payments with a payment date on or before this date.
            min_created_at: Filter to payments created at or after this timestamp.
            max_created_at: Filter to payments created at or before this timestamp.
            min_effective_at: Filter to payments effective at or after this timestamp.
            max_effective_at: Filter to payments effective at or before this timestamp.
            funding_id: Filter by the unique identifier of a funding event.
            search_text: Free-text search across payment fields.
            default_page_size: Default number of results returned per page.
            default_sort: Default field used to sort the results.
            default_sort_order: Default order in which to sort the results.
            status_reason: Filter by the reason for the most recent payment status change.
            status_source: Filter by the source of the most recent payment status change.
            include_metadata: Whether to include metadata in each returned payment. Defaults to false.
            is_refund: Filter payouts by whether they refund an original charge.
            has_refund: Filter charges by whether an associated payout has refunded them.
            is_resubmit: Filter payments by whether they resubmit an original payment.
            has_resubmit: Filter payments by whether they have been resubmitted.
            min_updated_at: Filter to payments last updated on or after this timestamp.
            max_updated_at: Filter to payments last updated on or before this timestamp.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaymentSummaryList: OK

        Example:
            ```python
            payment = await client.payments.list(
                page_number=1,
                page_size=100,
                sort_by="id",
                sort_order="asc",
                default_sort="id",
                default_sort_order="asc",
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
            "/v1/payments",
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
                        "payment_type": payment_type,
                        "payment_status": payment_status,
                        "payment_id": payment_id,
                        "external_id": external_id,
                        "customer_id": customer_id,
                        "paykey_id": paykey_id,
                        "paykey": paykey,
                        "min_amount": min_amount,
                        "max_amount": max_amount,
                        "min_payment_date": min_payment_date,
                        "max_payment_date": max_payment_date,
                        "min_created_at": min_created_at,
                        "max_created_at": max_created_at,
                        "min_effective_at": min_effective_at,
                        "max_effective_at": max_effective_at,
                        "funding_id": funding_id,
                        "search_text": search_text,
                        "default_page_size": default_page_size,
                        "default_sort": default_sort,
                        "default_sort_order": default_sort_order,
                        "status_reason": status_reason,
                        "status_source": status_source,
                        "include_metadata": include_metadata,
                        "is_refund": is_refund,
                        "has_refund": has_refund,
                        "is_resubmit": is_resubmit,
                        "has_resubmit": has_resubmit,
                        "min_updated_at": min_updated_at,
                        "max_updated_at": max_updated_at,
                    },
                    payment_list_params.PaymentListParams,
                ),
            ),
            cast_to=PaymentSummaryList,
        )


class PaymentsResourceWithRawResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.list = to_raw_response_wrapper(
            payments.list,
        )


class AsyncPaymentsResourceWithRawResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.list = async_to_raw_response_wrapper(
            payments.list,
        )


class PaymentsResourceWithStreamingResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.list = to_streamed_response_wrapper(
            payments.list,
        )


class AsyncPaymentsResourceWithStreamingResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.list = async_to_streamed_response_wrapper(
            payments.list,
        )

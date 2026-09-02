# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

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
from ...types.customers.customer_review_response import CustomerReviewResponse
from ...types.customer_response import CustomerResponse
from ...types.customers import review_set_verification_decision_params

__all__ = ["ReviewResource", "AsyncReviewResource"]


class ReviewResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReviewResourceWithRawResponse:
        return ReviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReviewResourceWithStreamingResponse:
        return ReviewResourceWithStreamingResponse(self)

    def list(
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
    ) -> CustomerReviewResponse:
        """
        Returns the results of a customer's identity and fraud review. The response includes decisions, risk and correlation scores, reason codes, watchlist matches, and network alerts.

        Args:
            id: Unique identifier for the customer.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomerReviewResponse: OK

        Example:
            ```python
            review = client.customers.review.list(
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
            path_template("/v1/customers/{id}/review", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerReviewResponse,
        )

    def set_verification_decision(
        self,
        id: str,
        *,
        status: Literal["verified", "rejected"],
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
    ) -> CustomerResponse:
        """
        Updates the verification decision for a customer. The customer's current `status` must be `review`.

        Args:
            id: Unique identifier for the customer.
            status: The final status of the customer review.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomerResponse: OK

        Example:
            ```python
            review = client.customers.review.set_verification_decision(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                status="verified",
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
            path_template("/v1/customers/{id}/review", **{"id": id}),
            body=maybe_transform(
                {"status": status},
                review_set_verification_decision_params.ReviewSetVerificationDecisionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )


class AsyncReviewResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReviewResourceWithRawResponse:
        return AsyncReviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReviewResourceWithStreamingResponse:
        return AsyncReviewResourceWithStreamingResponse(self)

    async def list(
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
    ) -> CustomerReviewResponse:
        """
        Returns the results of a customer's identity and fraud review. The response includes decisions, risk and correlation scores, reason codes, watchlist matches, and network alerts.

        Args:
            id: Unique identifier for the customer.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomerReviewResponse: OK

        Example:
            ```python
            review = await client.customers.review.list(
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
            path_template("/v1/customers/{id}/review", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerReviewResponse,
        )

    async def set_verification_decision(
        self,
        id: str,
        *,
        status: Literal["verified", "rejected"],
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
    ) -> CustomerResponse:
        """
        Updates the verification decision for a customer. The customer's current `status` must be `review`.

        Args:
            id: Unique identifier for the customer.
            status: The final status of the customer review.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomerResponse: OK

        Example:
            ```python
            review = await client.customers.review.set_verification_decision(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                status="verified",
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
            path_template("/v1/customers/{id}/review", **{"id": id}),
            body=await async_maybe_transform(
                {"status": status},
                review_set_verification_decision_params.ReviewSetVerificationDecisionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )


class ReviewResourceWithRawResponse:
    def __init__(self, review: ReviewResource) -> None:
        self._review = review

        self.list = to_raw_response_wrapper(
            review.list,
        )
        self.set_verification_decision = to_raw_response_wrapper(
            review.set_verification_decision,
        )


class AsyncReviewResourceWithRawResponse:
    def __init__(self, review: AsyncReviewResource) -> None:
        self._review = review

        self.list = async_to_raw_response_wrapper(
            review.list,
        )
        self.set_verification_decision = async_to_raw_response_wrapper(
            review.set_verification_decision,
        )


class ReviewResourceWithStreamingResponse:
    def __init__(self, review: ReviewResource) -> None:
        self._review = review

        self.list = to_streamed_response_wrapper(
            review.list,
        )
        self.set_verification_decision = to_streamed_response_wrapper(
            review.set_verification_decision,
        )


class AsyncReviewResourceWithStreamingResponse:
    def __init__(self, review: AsyncReviewResource) -> None:
        self._review = review

        self.list = async_to_streamed_response_wrapper(
            review.list,
        )
        self.set_verification_decision = async_to_streamed_response_wrapper(
            review.set_verification_decision,
        )

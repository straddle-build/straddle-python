# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, strip_not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.account_settings_response import AccountSettingsResponse

__all__ = ["AccountSettingsResource", "AsyncAccountSettingsResource"]


class AccountSettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountSettingsResourceWithRawResponse:
        return AccountSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountSettingsResourceWithStreamingResponse:
        return AccountSettingsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        account_id: str,
        *,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountSettingsResponse:
        """
        Returns all effective settings for the account, including values inherited from its organization, platform, and system defaults.

        Args:
            account_id: The ID of the account.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccountSettingsResponse: OK

        Example:
            ```python
            account_setting = client.account_settings.retrieve(
                account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
            path_template("/v1/account_settings/{account_id}", **{"account_id": account_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountSettingsResponse,
        )


class AsyncAccountSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountSettingsResourceWithRawResponse:
        return AsyncAccountSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountSettingsResourceWithStreamingResponse:
        return AsyncAccountSettingsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        account_id: str,
        *,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountSettingsResponse:
        """
        Returns all effective settings for the account, including values inherited from its organization, platform, and system defaults.

        Args:
            account_id: The ID of the account.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccountSettingsResponse: OK

        Example:
            ```python
            account_setting = await client.account_settings.retrieve(
                account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
            path_template("/v1/account_settings/{account_id}", **{"account_id": account_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountSettingsResponse,
        )


class AccountSettingsResourceWithRawResponse:
    def __init__(self, account_settings: AccountSettingsResource) -> None:
        self._account_settings = account_settings

        self.retrieve = to_raw_response_wrapper(
            account_settings.retrieve,
        )


class AsyncAccountSettingsResourceWithRawResponse:
    def __init__(self, account_settings: AsyncAccountSettingsResource) -> None:
        self._account_settings = account_settings

        self.retrieve = async_to_raw_response_wrapper(
            account_settings.retrieve,
        )


class AccountSettingsResourceWithStreamingResponse:
    def __init__(self, account_settings: AccountSettingsResource) -> None:
        self._account_settings = account_settings

        self.retrieve = to_streamed_response_wrapper(
            account_settings.retrieve,
        )


class AsyncAccountSettingsResourceWithStreamingResponse:
    def __init__(self, account_settings: AsyncAccountSettingsResource) -> None:
        self._account_settings = account_settings

        self.retrieve = async_to_streamed_response_wrapper(
            account_settings.retrieve,
        )

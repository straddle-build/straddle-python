# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict, Optional

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
from ..types.paykey_response import PaykeyResponse
from ..types.account_type import AccountType
from ..types.paykey_configuration_param import PaykeyConfigurationParam
from ..types import (
    bridge_create_bank_account_paykey_params,
    bridge_create_plaid_paykey_params,
    bridge_create_token_params,
    bridge_create_quiltt_paykey_params,
)
from ..types.bridge_token_response import BridgeTokenResponse
from ..types.revealed_paykey_response import RevealedPaykeyResponse

__all__ = ["BridgeResource", "AsyncBridgeResource"]


class BridgeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BridgeResourceWithRawResponse:
        return BridgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BridgeResourceWithStreamingResponse:
        return BridgeResourceWithStreamingResponse(self)

    def create_bank_account_paykey(
        self,
        *,
        customer_id: str,
        routing_number: str,
        account_number: str,
        account_type: AccountType,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        config: PaykeyConfigurationParam | Omit = omit,
        external_id: Optional[str] | Omit = omit,
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
        Creates a paykey from a routing number, account number, and account type.

        Args:
            customer_id: Unique identifier for the customer associated with the paykey.
            routing_number: Bank routing number.
            account_number: Bank account number.
            account_type: Body parameter.
            metadata: Up to 20 user-defined key-value pairs associated with the paykey.
            config: Body parameter.
            external_id: Unique identifier for the paykey in your system.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaykeyResponse: Created

        Example:
            ```python
            bridge = client.bridge.create_bank_account_paykey(
                customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                routing_number="xxxxxxxxx",
                account_number="",
                account_type="checking",
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
            "/v1/bridge/bank_account",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "routing_number": routing_number,
                    "account_number": account_number,
                    "account_type": account_type,
                    "metadata": metadata,
                    "config": config,
                    "external_id": external_id,
                },
                bridge_create_bank_account_paykey_params.BridgeCreateBankAccountPaykeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaykeyResponse,
        )

    def create_plaid_paykey(
        self,
        *,
        customer_id: str,
        plaid_token: str,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        config: PaykeyConfigurationParam | Omit = omit,
        external_id: Optional[str] | Omit = omit,
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
        Creates a paykey from a Plaid processor token.

        Args:
            customer_id: Unique identifier for the customer associated with the paykey.
            plaid_token: Plaid processor token generated by your application for use with the Straddle API.
            metadata: Up to 20 user-defined key-value pairs associated with the paykey.
            config: Body parameter.
            external_id: Unique identifier for the paykey in your system.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaykeyResponse: Created

        Example:
            ```python
            bridge = client.bridge.create_plaid_paykey(
                customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                plaid_token="",
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
            "/v1/bridge/plaid",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "plaid_token": plaid_token,
                    "metadata": metadata,
                    "config": config,
                    "external_id": external_id,
                },
                bridge_create_plaid_paykey_params.BridgeCreatePlaidPaykeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaykeyResponse,
        )

    def create_token(
        self,
        *,
        customer_id: str,
        config: PaykeyConfigurationParam | Omit = omit,
        external_id: Optional[str] | Omit = omit,
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
    ) -> BridgeTokenResponse:
        """
        Creates a session token for the Bridge widget.

        Args:
            customer_id: Unique identifier for the customer associated with the Bridge session.
            config: Body parameter.
            external_id: Unique identifier for the paykey in your system.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BridgeTokenResponse: Created

        Example:
            ```python
            bridge = client.bridge.create_token(
                customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
            "/v1/bridge/initialize",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "config": config,
                    "external_id": external_id,
                },
                bridge_create_token_params.BridgeCreateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BridgeTokenResponse,
        )

    def create_quiltt_paykey(
        self,
        *,
        customer_id: str,
        quiltt_token: str,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        config: PaykeyConfigurationParam | Omit = omit,
        external_id: Optional[str] | Omit = omit,
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
    ) -> RevealedPaykeyResponse:
        """
        Creates a paykey from a Quiltt processor token.

        Args:
            customer_id: Unique identifier for the customer associated with the paykey.
            quiltt_token: Quiltt processor token generated by your application for use with the Straddle API.
            metadata: Up to 20 user-defined key-value pairs associated with the paykey.
            config: Body parameter.
            external_id: Unique identifier for the paykey in your system.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RevealedPaykeyResponse: Created

        Example:
            ```python
            bridge = client.bridge.create_quiltt_paykey(
                customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                quiltt_token="",
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
            "/v1/bridge/quiltt",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "quiltt_token": quiltt_token,
                    "metadata": metadata,
                    "config": config,
                    "external_id": external_id,
                },
                bridge_create_quiltt_paykey_params.BridgeCreateQuilttPaykeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RevealedPaykeyResponse,
        )


class AsyncBridgeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBridgeResourceWithRawResponse:
        return AsyncBridgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBridgeResourceWithStreamingResponse:
        return AsyncBridgeResourceWithStreamingResponse(self)

    async def create_bank_account_paykey(
        self,
        *,
        customer_id: str,
        routing_number: str,
        account_number: str,
        account_type: AccountType,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        config: PaykeyConfigurationParam | Omit = omit,
        external_id: Optional[str] | Omit = omit,
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
        Creates a paykey from a routing number, account number, and account type.

        Args:
            customer_id: Unique identifier for the customer associated with the paykey.
            routing_number: Bank routing number.
            account_number: Bank account number.
            account_type: Body parameter.
            metadata: Up to 20 user-defined key-value pairs associated with the paykey.
            config: Body parameter.
            external_id: Unique identifier for the paykey in your system.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaykeyResponse: Created

        Example:
            ```python
            bridge = await client.bridge.create_bank_account_paykey(
                customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                routing_number="xxxxxxxxx",
                account_number="",
                account_type="checking",
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
            "/v1/bridge/bank_account",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "routing_number": routing_number,
                    "account_number": account_number,
                    "account_type": account_type,
                    "metadata": metadata,
                    "config": config,
                    "external_id": external_id,
                },
                bridge_create_bank_account_paykey_params.BridgeCreateBankAccountPaykeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaykeyResponse,
        )

    async def create_plaid_paykey(
        self,
        *,
        customer_id: str,
        plaid_token: str,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        config: PaykeyConfigurationParam | Omit = omit,
        external_id: Optional[str] | Omit = omit,
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
        Creates a paykey from a Plaid processor token.

        Args:
            customer_id: Unique identifier for the customer associated with the paykey.
            plaid_token: Plaid processor token generated by your application for use with the Straddle API.
            metadata: Up to 20 user-defined key-value pairs associated with the paykey.
            config: Body parameter.
            external_id: Unique identifier for the paykey in your system.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PaykeyResponse: Created

        Example:
            ```python
            bridge = await client.bridge.create_plaid_paykey(
                customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                plaid_token="",
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
            "/v1/bridge/plaid",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "plaid_token": plaid_token,
                    "metadata": metadata,
                    "config": config,
                    "external_id": external_id,
                },
                bridge_create_plaid_paykey_params.BridgeCreatePlaidPaykeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaykeyResponse,
        )

    async def create_token(
        self,
        *,
        customer_id: str,
        config: PaykeyConfigurationParam | Omit = omit,
        external_id: Optional[str] | Omit = omit,
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
    ) -> BridgeTokenResponse:
        """
        Creates a session token for the Bridge widget.

        Args:
            customer_id: Unique identifier for the customer associated with the Bridge session.
            config: Body parameter.
            external_id: Unique identifier for the paykey in your system.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            BridgeTokenResponse: Created

        Example:
            ```python
            bridge = await client.bridge.create_token(
                customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
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
            "/v1/bridge/initialize",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "config": config,
                    "external_id": external_id,
                },
                bridge_create_token_params.BridgeCreateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BridgeTokenResponse,
        )

    async def create_quiltt_paykey(
        self,
        *,
        customer_id: str,
        quiltt_token: str,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        config: PaykeyConfigurationParam | Omit = omit,
        external_id: Optional[str] | Omit = omit,
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
    ) -> RevealedPaykeyResponse:
        """
        Creates a paykey from a Quiltt processor token.

        Args:
            customer_id: Unique identifier for the customer associated with the paykey.
            quiltt_token: Quiltt processor token generated by your application for use with the Straddle API.
            metadata: Up to 20 user-defined key-value pairs associated with the paykey.
            config: Body parameter.
            external_id: Unique identifier for the paykey in your system.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            RevealedPaykeyResponse: Created

        Example:
            ```python
            bridge = await client.bridge.create_quiltt_paykey(
                customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                quiltt_token="",
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
            "/v1/bridge/quiltt",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "quiltt_token": quiltt_token,
                    "metadata": metadata,
                    "config": config,
                    "external_id": external_id,
                },
                bridge_create_quiltt_paykey_params.BridgeCreateQuilttPaykeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RevealedPaykeyResponse,
        )


class BridgeResourceWithRawResponse:
    def __init__(self, bridge: BridgeResource) -> None:
        self._bridge = bridge

        self.create_bank_account_paykey = to_raw_response_wrapper(
            bridge.create_bank_account_paykey,
        )
        self.create_plaid_paykey = to_raw_response_wrapper(
            bridge.create_plaid_paykey,
        )
        self.create_token = to_raw_response_wrapper(
            bridge.create_token,
        )
        self.create_quiltt_paykey = to_raw_response_wrapper(
            bridge.create_quiltt_paykey,
        )


class AsyncBridgeResourceWithRawResponse:
    def __init__(self, bridge: AsyncBridgeResource) -> None:
        self._bridge = bridge

        self.create_bank_account_paykey = async_to_raw_response_wrapper(
            bridge.create_bank_account_paykey,
        )
        self.create_plaid_paykey = async_to_raw_response_wrapper(
            bridge.create_plaid_paykey,
        )
        self.create_token = async_to_raw_response_wrapper(
            bridge.create_token,
        )
        self.create_quiltt_paykey = async_to_raw_response_wrapper(
            bridge.create_quiltt_paykey,
        )


class BridgeResourceWithStreamingResponse:
    def __init__(self, bridge: BridgeResource) -> None:
        self._bridge = bridge

        self.create_bank_account_paykey = to_streamed_response_wrapper(
            bridge.create_bank_account_paykey,
        )
        self.create_plaid_paykey = to_streamed_response_wrapper(
            bridge.create_plaid_paykey,
        )
        self.create_token = to_streamed_response_wrapper(
            bridge.create_token,
        )
        self.create_quiltt_paykey = to_streamed_response_wrapper(
            bridge.create_quiltt_paykey,
        )


class AsyncBridgeResourceWithStreamingResponse:
    def __init__(self, bridge: AsyncBridgeResource) -> None:
        self._bridge = bridge

        self.create_bank_account_paykey = async_to_streamed_response_wrapper(
            bridge.create_bank_account_paykey,
        )
        self.create_plaid_paykey = async_to_streamed_response_wrapper(
            bridge.create_plaid_paykey,
        )
        self.create_token = async_to_streamed_response_wrapper(
            bridge.create_token,
        )
        self.create_quiltt_paykey = async_to_streamed_response_wrapper(
            bridge.create_quiltt_paykey,
        )

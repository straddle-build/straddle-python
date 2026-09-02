# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict, List, Optional
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
from ..types.linked_bank_account_response import LinkedBankAccountResponse
from ..types import (
    linked_bank_account_create_params,
    linked_bank_account_list_params,
    linked_bank_account_update_params,
)
from ..types.linked_bank_account_list import LinkedBankAccountList
from ..types.unmasked_linked_bank_account_response import UnmaskedLinkedBankAccountResponse

__all__ = ["LinkedBankAccountsResource", "AsyncLinkedBankAccountsResource"]


class LinkedBankAccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LinkedBankAccountsResourceWithRawResponse:
        return LinkedBankAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LinkedBankAccountsResourceWithStreamingResponse:
        return LinkedBankAccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: Optional[str] | Omit = omit,
        bank_account: linked_bank_account_create_params.BankAccount,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        platform_id: Optional[str] | Omit = omit,
        purposes: Optional[List[Literal["charges", "payouts", "billing"]]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkedBankAccountResponse:
        """
        Creates a linked bank account for an account or platform, assigns its payment purposes, and returns the linked bank account.

        Args:
            account_id: ID of the account that will own the linked bank account. Omit this field to assign ownership to the platform in the authenticated request context.
            bank_account: Body parameter.
            metadata: Up to 20 user-defined key-value pairs.
            platform_id: ID of the platform to associate with the linked bank account.
            purposes: Payment purposes for the linked bank account. Defaults to `charges`, `payouts`, and `billing`.
            description: Your description for the linked bank account.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LinkedBankAccountResponse: Created

        Example:
            ```python
            linked_bank_account = client.linked_bank_accounts.create(
                bank_account={"account_holder": "", "routing_number": "xxxxxxxxx", "account_number": ""},
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
            "/v1/linked_bank_accounts",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "bank_account": bank_account,
                    "metadata": metadata,
                    "platform_id": platform_id,
                    "purposes": purposes,
                    "description": description,
                },
                linked_bank_account_create_params.LinkedBankAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkedBankAccountResponse,
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        level: Literal["account", "platform"] | Omit = omit,
        purpose: Literal["charges", "payouts", "billing"] | Omit = omit,
        status: Literal["created", "onboarding", "active", "rejected", "inactive", "canceled"] | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkedBankAccountList:
        """
        Returns a paginated list of linked bank accounts. Filter the list by account, scope, purpose, or status.

        Args:
            account_id: Account ID used to filter the results.
            page_number: Page number. Defaults to `1`.
            page_size: Number of results per page. Defaults to `100`. Maximum `1000`.
            sort_by: Field used to sort results. Defaults to `id`.
            sort_order: Sort direction. Defaults to `asc`.
            level: Scope of linked bank accounts to return.
            purpose: Linked bank account purpose. Accepted values are `charges`, `payouts`, and `billing`.
            status: Linked bank account status. Accepted values are `created`, `onboarding`, `active`, `rejected`, `inactive`, and `canceled`.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LinkedBankAccountList: OK

        Example:
            ```python
            linked_bank_account = client.linked_bank_accounts.list(
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
            "/v1/linked_bank_accounts",
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
                        "level": level,
                        "purpose": purpose,
                        "status": status,
                    },
                    linked_bank_account_list_params.LinkedBankAccountListParams,
                ),
            ),
            cast_to=LinkedBankAccountList,
        )

    def update(
        self,
        linked_bank_account_id: str,
        *,
        bank_account: linked_bank_account_update_params.BankAccount,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkedBankAccountResponse:
        """
        Updates bank account details and metadata, then returns the linked bank account. The linked bank account must have status `created`, or status `onboarding` with `status_detail.reason` set to `stuck`.

        Args:
            linked_bank_account_id: The ID of the linked bank account.
            bank_account: Body parameter.
            metadata: Up to 20 user-defined key-value pairs.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LinkedBankAccountResponse: OK

        Example:
            ```python
            linked_bank_account = client.linked_bank_accounts.update(
                linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                bank_account={"account_holder": "", "routing_number": "xxxxxxxxx", "account_number": ""},
            )
            ```
        """
        if linked_bank_account_id is None or (isinstance(linked_bank_account_id, str) and not linked_bank_account_id):
            raise ValueError(
                f"Expected a non-empty value for `linked_bank_account_id` but received {linked_bank_account_id!r}"
            )
        extra_headers = {
            **strip_not_given(
                {"Request-Id": request_id, "Correlation-Id": correlation_id, "Idempotency-Key": idempotency_key}
            ),
            **(extra_headers or {}),
        }
        return self._put(
            path_template(
                "/v1/linked_bank_accounts/{linked_bank_account_id}",
                **{"linked_bank_account_id": linked_bank_account_id},
            ),
            body=maybe_transform(
                {
                    "bank_account": bank_account,
                    "metadata": metadata,
                },
                linked_bank_account_update_params.LinkedBankAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkedBankAccountResponse,
        )

    def retrieve(
        self,
        linked_bank_account_id: str,
        *,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkedBankAccountResponse:
        """
        Returns the linked bank account with the specified ID. The response masks the account number.

        Args:
            linked_bank_account_id: The ID of the linked bank account.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LinkedBankAccountResponse: OK

        Example:
            ```python
            linked_bank_account = client.linked_bank_accounts.retrieve(
                linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if linked_bank_account_id is None or (isinstance(linked_bank_account_id, str) and not linked_bank_account_id):
            raise ValueError(
                f"Expected a non-empty value for `linked_bank_account_id` but received {linked_bank_account_id!r}"
            )
        extra_headers = {
            **strip_not_given({"Request-Id": request_id, "Correlation-Id": correlation_id}),
            **(extra_headers or {}),
        }
        return self._get(
            path_template(
                "/v1/linked_bank_accounts/{linked_bank_account_id}",
                **{"linked_bank_account_id": linked_bank_account_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkedBankAccountResponse,
        )

    def list_unmasked(
        self,
        linked_bank_account_id: str,
        *,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnmaskedLinkedBankAccountResponse:
        """
        Returns the linked bank account with the specified ID without masking its account number. This endpoint is available only when Straddle enables data unmasking for the account.

        Args:
            linked_bank_account_id: The ID of the linked bank account.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UnmaskedLinkedBankAccountResponse: OK

        Example:
            ```python
            linked_bank_account = client.linked_bank_accounts.list_unmasked(
                linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if linked_bank_account_id is None or (isinstance(linked_bank_account_id, str) and not linked_bank_account_id):
            raise ValueError(
                f"Expected a non-empty value for `linked_bank_account_id` but received {linked_bank_account_id!r}"
            )
        extra_headers = {
            **strip_not_given({"Request-Id": request_id, "Correlation-Id": correlation_id}),
            **(extra_headers or {}),
        }
        return self._get(
            path_template(
                "/v1/linked_bank_accounts/{linked_bank_account_id}/unmask",
                **{"linked_bank_account_id": linked_bank_account_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnmaskedLinkedBankAccountResponse,
        )

    def cancel(
        self,
        linked_bank_account_id: str,
        *,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkedBankAccountResponse:
        """
        Cancels a linked bank account and returns it with status `canceled`. The linked bank account must have status `created`.

        Args:
            linked_bank_account_id: The ID of the linked bank account.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LinkedBankAccountResponse: OK

        Example:
            ```python
            linked_bank_account = client.linked_bank_accounts.cancel(
                linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if linked_bank_account_id is None or (isinstance(linked_bank_account_id, str) and not linked_bank_account_id):
            raise ValueError(
                f"Expected a non-empty value for `linked_bank_account_id` but received {linked_bank_account_id!r}"
            )
        extra_headers = {
            **strip_not_given(
                {"Request-Id": request_id, "Correlation-Id": correlation_id, "Idempotency-Key": idempotency_key}
            ),
            **(extra_headers or {}),
        }
        return self._patch(
            path_template(
                "/v1/linked_bank_accounts/{linked_bank_account_id}/cancel",
                **{"linked_bank_account_id": linked_bank_account_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkedBankAccountResponse,
        )


class AsyncLinkedBankAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLinkedBankAccountsResourceWithRawResponse:
        return AsyncLinkedBankAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLinkedBankAccountsResourceWithStreamingResponse:
        return AsyncLinkedBankAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: Optional[str] | Omit = omit,
        bank_account: linked_bank_account_create_params.BankAccount,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        platform_id: Optional[str] | Omit = omit,
        purposes: Optional[List[Literal["charges", "payouts", "billing"]]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkedBankAccountResponse:
        """
        Creates a linked bank account for an account or platform, assigns its payment purposes, and returns the linked bank account.

        Args:
            account_id: ID of the account that will own the linked bank account. Omit this field to assign ownership to the platform in the authenticated request context.
            bank_account: Body parameter.
            metadata: Up to 20 user-defined key-value pairs.
            platform_id: ID of the platform to associate with the linked bank account.
            purposes: Payment purposes for the linked bank account. Defaults to `charges`, `payouts`, and `billing`.
            description: Your description for the linked bank account.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LinkedBankAccountResponse: Created

        Example:
            ```python
            linked_bank_account = await client.linked_bank_accounts.create(
                bank_account={"account_holder": "", "routing_number": "xxxxxxxxx", "account_number": ""},
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
            "/v1/linked_bank_accounts",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "bank_account": bank_account,
                    "metadata": metadata,
                    "platform_id": platform_id,
                    "purposes": purposes,
                    "description": description,
                },
                linked_bank_account_create_params.LinkedBankAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkedBankAccountResponse,
        )

    async def list(
        self,
        *,
        account_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        level: Literal["account", "platform"] | Omit = omit,
        purpose: Literal["charges", "payouts", "billing"] | Omit = omit,
        status: Literal["created", "onboarding", "active", "rejected", "inactive", "canceled"] | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkedBankAccountList:
        """
        Returns a paginated list of linked bank accounts. Filter the list by account, scope, purpose, or status.

        Args:
            account_id: Account ID used to filter the results.
            page_number: Page number. Defaults to `1`.
            page_size: Number of results per page. Defaults to `100`. Maximum `1000`.
            sort_by: Field used to sort results. Defaults to `id`.
            sort_order: Sort direction. Defaults to `asc`.
            level: Scope of linked bank accounts to return.
            purpose: Linked bank account purpose. Accepted values are `charges`, `payouts`, and `billing`.
            status: Linked bank account status. Accepted values are `created`, `onboarding`, `active`, `rejected`, `inactive`, and `canceled`.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LinkedBankAccountList: OK

        Example:
            ```python
            linked_bank_account = await client.linked_bank_accounts.list(
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
            "/v1/linked_bank_accounts",
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
                        "level": level,
                        "purpose": purpose,
                        "status": status,
                    },
                    linked_bank_account_list_params.LinkedBankAccountListParams,
                ),
            ),
            cast_to=LinkedBankAccountList,
        )

    async def update(
        self,
        linked_bank_account_id: str,
        *,
        bank_account: linked_bank_account_update_params.BankAccount,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkedBankAccountResponse:
        """
        Updates bank account details and metadata, then returns the linked bank account. The linked bank account must have status `created`, or status `onboarding` with `status_detail.reason` set to `stuck`.

        Args:
            linked_bank_account_id: The ID of the linked bank account.
            bank_account: Body parameter.
            metadata: Up to 20 user-defined key-value pairs.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LinkedBankAccountResponse: OK

        Example:
            ```python
            linked_bank_account = await client.linked_bank_accounts.update(
                linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                bank_account={"account_holder": "", "routing_number": "xxxxxxxxx", "account_number": ""},
            )
            ```
        """
        if linked_bank_account_id is None or (isinstance(linked_bank_account_id, str) and not linked_bank_account_id):
            raise ValueError(
                f"Expected a non-empty value for `linked_bank_account_id` but received {linked_bank_account_id!r}"
            )
        extra_headers = {
            **strip_not_given(
                {"Request-Id": request_id, "Correlation-Id": correlation_id, "Idempotency-Key": idempotency_key}
            ),
            **(extra_headers or {}),
        }
        return await self._put(
            path_template(
                "/v1/linked_bank_accounts/{linked_bank_account_id}",
                **{"linked_bank_account_id": linked_bank_account_id},
            ),
            body=await async_maybe_transform(
                {
                    "bank_account": bank_account,
                    "metadata": metadata,
                },
                linked_bank_account_update_params.LinkedBankAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkedBankAccountResponse,
        )

    async def retrieve(
        self,
        linked_bank_account_id: str,
        *,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkedBankAccountResponse:
        """
        Returns the linked bank account with the specified ID. The response masks the account number.

        Args:
            linked_bank_account_id: The ID of the linked bank account.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LinkedBankAccountResponse: OK

        Example:
            ```python
            linked_bank_account = await client.linked_bank_accounts.retrieve(
                linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if linked_bank_account_id is None or (isinstance(linked_bank_account_id, str) and not linked_bank_account_id):
            raise ValueError(
                f"Expected a non-empty value for `linked_bank_account_id` but received {linked_bank_account_id!r}"
            )
        extra_headers = {
            **strip_not_given({"Request-Id": request_id, "Correlation-Id": correlation_id}),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template(
                "/v1/linked_bank_accounts/{linked_bank_account_id}",
                **{"linked_bank_account_id": linked_bank_account_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkedBankAccountResponse,
        )

    async def list_unmasked(
        self,
        linked_bank_account_id: str,
        *,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnmaskedLinkedBankAccountResponse:
        """
        Returns the linked bank account with the specified ID without masking its account number. This endpoint is available only when Straddle enables data unmasking for the account.

        Args:
            linked_bank_account_id: The ID of the linked bank account.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UnmaskedLinkedBankAccountResponse: OK

        Example:
            ```python
            linked_bank_account = await client.linked_bank_accounts.list_unmasked(
                linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if linked_bank_account_id is None or (isinstance(linked_bank_account_id, str) and not linked_bank_account_id):
            raise ValueError(
                f"Expected a non-empty value for `linked_bank_account_id` but received {linked_bank_account_id!r}"
            )
        extra_headers = {
            **strip_not_given({"Request-Id": request_id, "Correlation-Id": correlation_id}),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template(
                "/v1/linked_bank_accounts/{linked_bank_account_id}/unmask",
                **{"linked_bank_account_id": linked_bank_account_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnmaskedLinkedBankAccountResponse,
        )

    async def cancel(
        self,
        linked_bank_account_id: str,
        *,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkedBankAccountResponse:
        """
        Cancels a linked bank account and returns it with status `canceled`. The linked bank account must have status `created`.

        Args:
            linked_bank_account_id: The ID of the linked bank account.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            LinkedBankAccountResponse: OK

        Example:
            ```python
            linked_bank_account = await client.linked_bank_accounts.cancel(
                linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
            )
            ```
        """
        if linked_bank_account_id is None or (isinstance(linked_bank_account_id, str) and not linked_bank_account_id):
            raise ValueError(
                f"Expected a non-empty value for `linked_bank_account_id` but received {linked_bank_account_id!r}"
            )
        extra_headers = {
            **strip_not_given(
                {"Request-Id": request_id, "Correlation-Id": correlation_id, "Idempotency-Key": idempotency_key}
            ),
            **(extra_headers or {}),
        }
        return await self._patch(
            path_template(
                "/v1/linked_bank_accounts/{linked_bank_account_id}/cancel",
                **{"linked_bank_account_id": linked_bank_account_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkedBankAccountResponse,
        )


class LinkedBankAccountsResourceWithRawResponse:
    def __init__(self, linked_bank_accounts: LinkedBankAccountsResource) -> None:
        self._linked_bank_accounts = linked_bank_accounts

        self.create = to_raw_response_wrapper(
            linked_bank_accounts.create,
        )
        self.list = to_raw_response_wrapper(
            linked_bank_accounts.list,
        )
        self.update = to_raw_response_wrapper(
            linked_bank_accounts.update,
        )
        self.retrieve = to_raw_response_wrapper(
            linked_bank_accounts.retrieve,
        )
        self.list_unmasked = to_raw_response_wrapper(
            linked_bank_accounts.list_unmasked,
        )
        self.cancel = to_raw_response_wrapper(
            linked_bank_accounts.cancel,
        )


class AsyncLinkedBankAccountsResourceWithRawResponse:
    def __init__(self, linked_bank_accounts: AsyncLinkedBankAccountsResource) -> None:
        self._linked_bank_accounts = linked_bank_accounts

        self.create = async_to_raw_response_wrapper(
            linked_bank_accounts.create,
        )
        self.list = async_to_raw_response_wrapper(
            linked_bank_accounts.list,
        )
        self.update = async_to_raw_response_wrapper(
            linked_bank_accounts.update,
        )
        self.retrieve = async_to_raw_response_wrapper(
            linked_bank_accounts.retrieve,
        )
        self.list_unmasked = async_to_raw_response_wrapper(
            linked_bank_accounts.list_unmasked,
        )
        self.cancel = async_to_raw_response_wrapper(
            linked_bank_accounts.cancel,
        )


class LinkedBankAccountsResourceWithStreamingResponse:
    def __init__(self, linked_bank_accounts: LinkedBankAccountsResource) -> None:
        self._linked_bank_accounts = linked_bank_accounts

        self.create = to_streamed_response_wrapper(
            linked_bank_accounts.create,
        )
        self.list = to_streamed_response_wrapper(
            linked_bank_accounts.list,
        )
        self.update = to_streamed_response_wrapper(
            linked_bank_accounts.update,
        )
        self.retrieve = to_streamed_response_wrapper(
            linked_bank_accounts.retrieve,
        )
        self.list_unmasked = to_streamed_response_wrapper(
            linked_bank_accounts.list_unmasked,
        )
        self.cancel = to_streamed_response_wrapper(
            linked_bank_accounts.cancel,
        )


class AsyncLinkedBankAccountsResourceWithStreamingResponse:
    def __init__(self, linked_bank_accounts: AsyncLinkedBankAccountsResource) -> None:
        self._linked_bank_accounts = linked_bank_accounts

        self.create = async_to_streamed_response_wrapper(
            linked_bank_accounts.create,
        )
        self.list = async_to_streamed_response_wrapper(
            linked_bank_accounts.list,
        )
        self.update = async_to_streamed_response_wrapper(
            linked_bank_accounts.update,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            linked_bank_accounts.retrieve,
        )
        self.list_unmasked = async_to_streamed_response_wrapper(
            linked_bank_accounts.list_unmasked,
        )
        self.cancel = async_to_streamed_response_wrapper(
            linked_bank_accounts.cancel,
        )

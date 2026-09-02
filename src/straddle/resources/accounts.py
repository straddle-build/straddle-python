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
from ..types.account_response import AccountResponse
from ..types.account_business_profile_param import AccountBusinessProfileParam
from ..types import (
    account_update_params,
    account_create_params,
    account_list_params,
    account_onboard_params,
    account_simulate_onboarding_params,
)
from ..types.account_list import AccountList
from ..types.terms_of_service_param import TermsOfServiceParam

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self)

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
    ) -> AccountResponse:
        """
        Returns the account with the specified ID.

        Args:
            account_id: The ID of the account.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccountResponse: OK

        Example:
            ```python
            account = client.accounts.retrieve(
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
            path_template("/v1/accounts/{account_id}", **{"account_id": account_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountResponse,
        )

    def update(
        self,
        account_id: str,
        *,
        business_profile: AccountBusinessProfileParam,
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
    ) -> AccountResponse:
        """
        Updates an account's business profile, metadata, and external ID, then returns the account.

        Args:
            account_id: The ID of the account.
            business_profile: Body parameter.
            metadata: Up to 20 user-defined key-value pairs.
            external_id: Your unique ID for the account.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccountResponse: OK

        Example:
            ```python
            account = client.accounts.update(
                account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                business_profile={"name": "", "website": "https://example.com"},
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
        return self._put(
            path_template("/v1/accounts/{account_id}", **{"account_id": account_id}),
            body=maybe_transform(
                {
                    "business_profile": business_profile,
                    "metadata": metadata,
                    "external_id": external_id,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountResponse,
        )

    def create(
        self,
        *,
        organization_id: str,
        account_type: Literal["business"],
        business_profile: AccountBusinessProfileParam,
        access_level: Literal["standard", "managed"],
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
    ) -> AccountResponse:
        """
        Creates a business account in the specified organization and returns the account.

        Args:
            organization_id: ID of the organization that will own the account.
            account_type: Account type. The only accepted value is `business`.
            business_profile: Body parameter.
            access_level: The account access level. `standard` provides normal account access, including access to the Straddle dashboard. `managed` means the platform manages the account and account users cannot access the Straddle dashboard.
            metadata: Up to 20 user-defined key-value pairs.
            external_id: Your unique ID for the account.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccountResponse: Created

        Example:
            ```python
            account = client.accounts.create(
                organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                account_type="business",
                business_profile={"name": "", "website": "https://example.com"},
                access_level="standard",
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
            "/v1/accounts",
            body=maybe_transform(
                {
                    "organization_id": organization_id,
                    "account_type": account_type,
                    "business_profile": business_profile,
                    "access_level": access_level,
                    "metadata": metadata,
                    "external_id": external_id,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        search_text: str | Omit = omit,
        status: Literal["created", "onboarding", "active", "rejected", "inactive"] | Omit = omit,
        type: Literal["business"] | Omit = omit,
        external_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountList:
        """
        Returns a paginated list of accounts for your platform. Filter the list by status, type, external ID, or text search.

        Args:
            page_number: Page number. Defaults to `1`.
            page_size: Number of results per page. Defaults to `100`. Maximum `1000`.
            sort_by: Field used to sort results. Defaults to `id`.
            sort_order: Sort direction. Defaults to `asc`.
            search_text: Text to search for across account fields.
            status: Account status to return.
            type: Account type to return.
            external_id: Your external ID for the account.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccountList: OK

        Example:
            ```python
            account = client.accounts.list(
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
            "/v1/accounts",
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
                        "search_text": search_text,
                        "status": status,
                        "type": type,
                        "external_id": external_id,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            cast_to=AccountList,
        )

    def onboard(
        self,
        account_id: str,
        *,
        terms_of_service: TermsOfServiceParam,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountResponse:
        """
        Starts onboarding and records the account's acceptance of Straddle's Terms of Service. The account must have at least one representative and one linked bank account. This operation also moves all associated representatives and linked bank accounts to `onboarding`.

        Args:
            account_id: The ID of the account.
            terms_of_service: Body parameter.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccountResponse: Created

        Example:
            ```python
            account = client.accounts.onboard(
                account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                terms_of_service={"accepted_date": "2024-01-01T00:00:00.000Z", "agreement_url": "", "agreement_type": "embedded"},
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
            path_template("/v1/accounts/{account_id}/onboard", **{"account_id": account_id}),
            body=maybe_transform(
                {"terms_of_service": terms_of_service},
                account_onboard_params.AccountOnboardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountResponse,
        )

    def simulate_onboarding(
        self,
        account_id: str,
        *,
        final_status: Literal["onboarding", "active"] | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountResponse:
        """
        Simulates an account status transition to `onboarding` or `active` in the sandbox and returns the account.

        Args:
            account_id: The ID of the account.
            final_status: Final account status to produce in the sandbox simulation.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccountResponse: Created

        Example:
            ```python
            account = client.accounts.simulate_onboarding(
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
            path_template("/v1/accounts/{account_id}/simulate", **{"account_id": account_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"final_status": final_status}, account_simulate_onboarding_params.AccountSimulateOnboardingParams
                ),
            ),
            cast_to=AccountResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self)

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
    ) -> AccountResponse:
        """
        Returns the account with the specified ID.

        Args:
            account_id: The ID of the account.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccountResponse: OK

        Example:
            ```python
            account = await client.accounts.retrieve(
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
            path_template("/v1/accounts/{account_id}", **{"account_id": account_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountResponse,
        )

    async def update(
        self,
        account_id: str,
        *,
        business_profile: AccountBusinessProfileParam,
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
    ) -> AccountResponse:
        """
        Updates an account's business profile, metadata, and external ID, then returns the account.

        Args:
            account_id: The ID of the account.
            business_profile: Body parameter.
            metadata: Up to 20 user-defined key-value pairs.
            external_id: Your unique ID for the account.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccountResponse: OK

        Example:
            ```python
            account = await client.accounts.update(
                account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                business_profile={"name": "", "website": "https://example.com"},
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
        return await self._put(
            path_template("/v1/accounts/{account_id}", **{"account_id": account_id}),
            body=await async_maybe_transform(
                {
                    "business_profile": business_profile,
                    "metadata": metadata,
                    "external_id": external_id,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountResponse,
        )

    async def create(
        self,
        *,
        organization_id: str,
        account_type: Literal["business"],
        business_profile: AccountBusinessProfileParam,
        access_level: Literal["standard", "managed"],
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
    ) -> AccountResponse:
        """
        Creates a business account in the specified organization and returns the account.

        Args:
            organization_id: ID of the organization that will own the account.
            account_type: Account type. The only accepted value is `business`.
            business_profile: Body parameter.
            access_level: The account access level. `standard` provides normal account access, including access to the Straddle dashboard. `managed` means the platform manages the account and account users cannot access the Straddle dashboard.
            metadata: Up to 20 user-defined key-value pairs.
            external_id: Your unique ID for the account.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccountResponse: Created

        Example:
            ```python
            account = await client.accounts.create(
                organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                account_type="business",
                business_profile={"name": "", "website": "https://example.com"},
                access_level="standard",
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
            "/v1/accounts",
            body=await async_maybe_transform(
                {
                    "organization_id": organization_id,
                    "account_type": account_type,
                    "business_profile": business_profile,
                    "access_level": access_level,
                    "metadata": metadata,
                    "external_id": external_id,
                },
                account_create_params.AccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountResponse,
        )

    async def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        search_text: str | Omit = omit,
        status: Literal["created", "onboarding", "active", "rejected", "inactive"] | Omit = omit,
        type: Literal["business"] | Omit = omit,
        external_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountList:
        """
        Returns a paginated list of accounts for your platform. Filter the list by status, type, external ID, or text search.

        Args:
            page_number: Page number. Defaults to `1`.
            page_size: Number of results per page. Defaults to `100`. Maximum `1000`.
            sort_by: Field used to sort results. Defaults to `id`.
            sort_order: Sort direction. Defaults to `asc`.
            search_text: Text to search for across account fields.
            status: Account status to return.
            type: Account type to return.
            external_id: Your external ID for the account.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccountList: OK

        Example:
            ```python
            account = await client.accounts.list(
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
            "/v1/accounts",
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
                        "search_text": search_text,
                        "status": status,
                        "type": type,
                        "external_id": external_id,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            cast_to=AccountList,
        )

    async def onboard(
        self,
        account_id: str,
        *,
        terms_of_service: TermsOfServiceParam,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountResponse:
        """
        Starts onboarding and records the account's acceptance of Straddle's Terms of Service. The account must have at least one representative and one linked bank account. This operation also moves all associated representatives and linked bank accounts to `onboarding`.

        Args:
            account_id: The ID of the account.
            terms_of_service: Body parameter.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccountResponse: Created

        Example:
            ```python
            account = await client.accounts.onboard(
                account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                terms_of_service={"accepted_date": "2024-01-01T00:00:00.000Z", "agreement_url": "", "agreement_type": "embedded"},
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
            path_template("/v1/accounts/{account_id}/onboard", **{"account_id": account_id}),
            body=await async_maybe_transform(
                {"terms_of_service": terms_of_service},
                account_onboard_params.AccountOnboardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountResponse,
        )

    async def simulate_onboarding(
        self,
        account_id: str,
        *,
        final_status: Literal["onboarding", "active"] | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountResponse:
        """
        Simulates an account status transition to `onboarding` or `active` in the sandbox and returns the account.

        Args:
            account_id: The ID of the account.
            final_status: Final account status to produce in the sandbox simulation.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AccountResponse: Created

        Example:
            ```python
            account = await client.accounts.simulate_onboarding(
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
            path_template("/v1/accounts/{account_id}/simulate", **{"account_id": account_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"final_status": final_status}, account_simulate_onboarding_params.AccountSimulateOnboardingParams
                ),
            ),
            cast_to=AccountResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            accounts.update,
        )
        self.create = to_raw_response_wrapper(
            accounts.create,
        )
        self.list = to_raw_response_wrapper(
            accounts.list,
        )
        self.onboard = to_raw_response_wrapper(
            accounts.onboard,
        )
        self.simulate_onboarding = to_raw_response_wrapper(
            accounts.simulate_onboarding,
        )


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = async_to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            accounts.update,
        )
        self.create = async_to_raw_response_wrapper(
            accounts.create,
        )
        self.list = async_to_raw_response_wrapper(
            accounts.list,
        )
        self.onboard = async_to_raw_response_wrapper(
            accounts.onboard,
        )
        self.simulate_onboarding = async_to_raw_response_wrapper(
            accounts.simulate_onboarding,
        )


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            accounts.update,
        )
        self.create = to_streamed_response_wrapper(
            accounts.create,
        )
        self.list = to_streamed_response_wrapper(
            accounts.list,
        )
        self.onboard = to_streamed_response_wrapper(
            accounts.onboard,
        )
        self.simulate_onboarding = to_streamed_response_wrapper(
            accounts.simulate_onboarding,
        )


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = async_to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            accounts.update,
        )
        self.create = async_to_streamed_response_wrapper(
            accounts.create,
        )
        self.list = async_to_streamed_response_wrapper(
            accounts.list,
        )
        self.onboard = async_to_streamed_response_wrapper(
            accounts.onboard,
        )
        self.simulate_onboarding = async_to_streamed_response_wrapper(
            accounts.simulate_onboarding,
        )

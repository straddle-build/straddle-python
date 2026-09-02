# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict, List, Optional, Union
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
from ...types.customer_response import CustomerResponse
from ...types.customer_address_param import CustomerAddressParam
from ...types.unmasked_compliance_profile_param import UnmaskedComplianceProfileParam
from ...types.customer_device_param import CustomerDeviceParam
from ...types.customer_status import CustomerStatus
from ...types import customer_update_params, customer_list_params, customer_create_params
from ...types.customer_summary_list import CustomerSummaryList
from ...types.sort_order import SortOrder
from ...types.customer_type import CustomerType
from ...types.customer_configuration_param import CustomerConfigurationParam
from ...types.unmasked_customer_response import UnmaskedCustomerResponse

__all__ = ["CustomersResource", "AsyncCustomersResource"]


class CustomersResource(SyncAPIResource):
    @cached_property
    def review(self) -> ReviewResource:
        return ReviewResource(self._client)

    @cached_property
    def with_raw_response(self) -> CustomersResourceWithRawResponse:
        return CustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomersResourceWithStreamingResponse:
        return CustomersResourceWithStreamingResponse(self)

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
    ) -> CustomerResponse:
        """
        Returns a customer by `id`.

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
            CustomerResponse: OK

        Example:
            ```python
            customer = client.customers.retrieve(
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
            path_template("/v1/customers/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )

    def update(
        self,
        id: str,
        *,
        name: str,
        email: str,
        address: Optional[CustomerAddressParam] | Omit = omit,
        phone: str,
        compliance_profile: Optional[UnmaskedComplianceProfileParam] | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        device: CustomerDeviceParam,
        status: CustomerStatus,
        metadata: Optional[Dict[str, str]] | Omit = omit,
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
        Updates an existing customer's profile, status, and metadata.

        Args:
            id: Unique identifier for the customer.
            name: Full name for an individual customer or business name for a business customer.
            email: Customer email address.
            address: Customer postal address. When provided, the object must include all required fields.
            phone: Customer phone number in E.164 format.
            compliance_profile: Body parameter.
            external_id: Unique identifier for the customer in your system.
            device: Body parameter.
            status: Body parameter.
            metadata: Up to 20 user-defined key-value pairs associated with the customer.
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
            customer = client.customers.update(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                name="",
                email="user@example.com",
                phone="",
                device={"ip_address": "192.168.1.1"},
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
        return self._put(
            path_template("/v1/customers/{id}", **{"id": id}),
            body=maybe_transform(
                {
                    "name": name,
                    "email": email,
                    "address": address,
                    "phone": phone,
                    "compliance_profile": compliance_profile,
                    "external_id": external_id,
                    "device": device,
                    "status": status,
                    "metadata": metadata,
                },
                customer_update_params.CustomerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )

    def delete(
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
    ) -> CustomerResponse:
        """
        Permanently deletes a customer record. The deletion cannot be undone. Use this endpoint only to meet regulatory or privacy requirements.

        Args:
            id: Unique identifier for the customer.
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
            customer = client.customers.delete(
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
        return self._delete(
            path_template("/v1/customers/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: Literal["name", "created_at"] | Omit = omit,
        sort_order: SortOrder | Omit = omit,
        created_from: Union[str, datetime] | Omit = omit,
        created_to: Union[str, datetime] | Omit = omit,
        name: str | Omit = omit,
        external_id: str | Omit = omit,
        email: str | Omit = omit,
        status: List[CustomerStatus] | Omit = omit,
        search_text: str | Omit = omit,
        types: List[CustomerType] | Omit = omit,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerSummaryList:
        """
        Returns a paginated list of customers for the account. Optional query parameters filter, search, and sort the results.

        Args:
            page_number: Page number for paginated results. Starts at 1.
            page_size: Number of results per page. Maximum: 1000.
            sort_by: Field used to sort the results.
            sort_order: Order in which to sort the results.
            created_from: Start date for filtering by `created_at` date.
            created_to: End date for filtering by `created_at` date.
            name: Filter customers by `name` (partial match).
            external_id: Filter by your system's `external_id`.
            email: Filter customers by `email` address.
            status: Filter customers by their current `status`.
            search_text: General search term to filter customers.
            types: Filter by customer type `individual` or `business`.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomerSummaryList: OK

        Example:
            ```python
            customer = client.customers.list(
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
            "/v1/customers",
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
                        "name": name,
                        "external_id": external_id,
                        "email": email,
                        "status": status,
                        "search_text": search_text,
                        "types": types,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            cast_to=CustomerSummaryList,
        )

    def create(
        self,
        *,
        name: str,
        type: CustomerType,
        email: str,
        address: Optional[CustomerAddressParam] | Omit = omit,
        phone: str,
        compliance_profile: Optional[UnmaskedComplianceProfileParam] | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        device: CustomerDeviceParam,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        config: CustomerConfigurationParam | Omit = omit,
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
        Creates a customer and starts identity, fraud, and risk assessments.

        Args:
            name: Full name for an individual customer or business name for a business customer.
            type: Body parameter.
            email: Customer email address.
            address: Customer postal address. When provided, the object must include all required fields.
            phone: Customer phone number in E.164 format. A mobile number is preferred.
            compliance_profile: Customer compliance profile. When provided, the object must include all fields required for the customer type.
            external_id: Unique identifier for the customer in your system.
            device: Body parameter.
            metadata: Up to 20 user-defined key-value pairs associated with the customer.
            config: Body parameter.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomerResponse: Created

        Example:
            ```python
            customer = client.customers.create(
                name="Ron Swanson",
                type="individual",
                email="ron.swanson@pawnee.com",
                address={"address1": "123 Main St", "city": "Anytown", "state": "CA", "zip": "94105"},
                phone="+12128675309",
                external_id="customer_123",
                device={"ip_address": "192.168.1.1"},
                metadata={},
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
            "/v1/customers",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "email": email,
                    "address": address,
                    "phone": phone,
                    "compliance_profile": compliance_profile,
                    "external_id": external_id,
                    "device": device,
                    "metadata": metadata,
                    "config": config,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
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
    ) -> UnmaskedCustomerResponse:
        """
        Returns unmasked details for a customer, including personally identifiable information. Straddle must enable this endpoint for your account. Use this endpoint only when unmasked data is necessary.

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
            UnmaskedCustomerResponse: OK

        Example:
            ```python
            customer = client.customers.list_unmasked(
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
            path_template("/v1/customers/{id}/unmasked", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnmaskedCustomerResponse,
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
    ) -> CustomerResponse:
        """
        Starts a new identity review for a customer. The review runs asynchronously. Webhooks and the customer review endpoint return updated results.

        Args:
            id: Unique identifier for the customer.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomerResponse: Accepted

        Example:
            ```python
            customer = client.customers.refresh_review(
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
            path_template("/v1/customers/{id}/refresh_review", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )


class AsyncCustomersResource(AsyncAPIResource):
    @cached_property
    def review(self) -> AsyncReviewResource:
        return AsyncReviewResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomersResourceWithRawResponse:
        return AsyncCustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomersResourceWithStreamingResponse:
        return AsyncCustomersResourceWithStreamingResponse(self)

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
    ) -> CustomerResponse:
        """
        Returns a customer by `id`.

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
            CustomerResponse: OK

        Example:
            ```python
            customer = await client.customers.retrieve(
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
            path_template("/v1/customers/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )

    async def update(
        self,
        id: str,
        *,
        name: str,
        email: str,
        address: Optional[CustomerAddressParam] | Omit = omit,
        phone: str,
        compliance_profile: Optional[UnmaskedComplianceProfileParam] | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        device: CustomerDeviceParam,
        status: CustomerStatus,
        metadata: Optional[Dict[str, str]] | Omit = omit,
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
        Updates an existing customer's profile, status, and metadata.

        Args:
            id: Unique identifier for the customer.
            name: Full name for an individual customer or business name for a business customer.
            email: Customer email address.
            address: Customer postal address. When provided, the object must include all required fields.
            phone: Customer phone number in E.164 format.
            compliance_profile: Body parameter.
            external_id: Unique identifier for the customer in your system.
            device: Body parameter.
            status: Body parameter.
            metadata: Up to 20 user-defined key-value pairs associated with the customer.
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
            customer = await client.customers.update(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                name="",
                email="user@example.com",
                phone="",
                device={"ip_address": "192.168.1.1"},
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
        return await self._put(
            path_template("/v1/customers/{id}", **{"id": id}),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "email": email,
                    "address": address,
                    "phone": phone,
                    "compliance_profile": compliance_profile,
                    "external_id": external_id,
                    "device": device,
                    "status": status,
                    "metadata": metadata,
                },
                customer_update_params.CustomerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )

    async def delete(
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
    ) -> CustomerResponse:
        """
        Permanently deletes a customer record. The deletion cannot be undone. Use this endpoint only to meet regulatory or privacy requirements.

        Args:
            id: Unique identifier for the customer.
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
            customer = await client.customers.delete(
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
        return await self._delete(
            path_template("/v1/customers/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )

    async def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort_by: Literal["name", "created_at"] | Omit = omit,
        sort_order: SortOrder | Omit = omit,
        created_from: Union[str, datetime] | Omit = omit,
        created_to: Union[str, datetime] | Omit = omit,
        name: str | Omit = omit,
        external_id: str | Omit = omit,
        email: str | Omit = omit,
        status: List[CustomerStatus] | Omit = omit,
        search_text: str | Omit = omit,
        types: List[CustomerType] | Omit = omit,
        straddle_account_id: str | Omit = omit,
        request_id: str | Omit = omit,
        correlation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerSummaryList:
        """
        Returns a paginated list of customers for the account. Optional query parameters filter, search, and sort the results.

        Args:
            page_number: Page number for paginated results. Starts at 1.
            page_size: Number of results per page. Maximum: 1000.
            sort_by: Field used to sort the results.
            sort_order: Order in which to sort the results.
            created_from: Start date for filtering by `created_at` date.
            created_to: End date for filtering by `created_at` date.
            name: Filter customers by `name` (partial match).
            external_id: Filter by your system's `external_id`.
            email: Filter customers by `email` address.
            status: Filter customers by their current `status`.
            search_text: General search term to filter customers.
            types: Filter by customer type `individual` or `business`.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomerSummaryList: OK

        Example:
            ```python
            customer = await client.customers.list(
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
            "/v1/customers",
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
                        "name": name,
                        "external_id": external_id,
                        "email": email,
                        "status": status,
                        "search_text": search_text,
                        "types": types,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            cast_to=CustomerSummaryList,
        )

    async def create(
        self,
        *,
        name: str,
        type: CustomerType,
        email: str,
        address: Optional[CustomerAddressParam] | Omit = omit,
        phone: str,
        compliance_profile: Optional[UnmaskedComplianceProfileParam] | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        device: CustomerDeviceParam,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        config: CustomerConfigurationParam | Omit = omit,
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
        Creates a customer and starts identity, fraud, and risk assessments.

        Args:
            name: Full name for an individual customer or business name for a business customer.
            type: Body parameter.
            email: Customer email address.
            address: Customer postal address. When provided, the object must include all required fields.
            phone: Customer phone number in E.164 format. A mobile number is preferred.
            compliance_profile: Customer compliance profile. When provided, the object must include all fields required for the customer type.
            external_id: Unique identifier for the customer in your system.
            device: Body parameter.
            metadata: Up to 20 user-defined key-value pairs associated with the customer.
            config: Body parameter.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomerResponse: Created

        Example:
            ```python
            customer = await client.customers.create(
                name="Ron Swanson",
                type="individual",
                email="ron.swanson@pawnee.com",
                address={"address1": "123 Main St", "city": "Anytown", "state": "CA", "zip": "94105"},
                phone="+12128675309",
                external_id="customer_123",
                device={"ip_address": "192.168.1.1"},
                metadata={},
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
            "/v1/customers",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "email": email,
                    "address": address,
                    "phone": phone,
                    "compliance_profile": compliance_profile,
                    "external_id": external_id,
                    "device": device,
                    "metadata": metadata,
                    "config": config,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
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
    ) -> UnmaskedCustomerResponse:
        """
        Returns unmasked details for a customer, including personally identifiable information. Straddle must enable this endpoint for your account. Use this endpoint only when unmasked data is necessary.

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
            UnmaskedCustomerResponse: OK

        Example:
            ```python
            customer = await client.customers.list_unmasked(
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
            path_template("/v1/customers/{id}/unmasked", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnmaskedCustomerResponse,
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
    ) -> CustomerResponse:
        """
        Starts a new identity review for a customer. The review runs asynchronously. Webhooks and the customer review endpoint return updated results.

        Args:
            id: Unique identifier for the customer.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            CustomerResponse: Accepted

        Example:
            ```python
            customer = await client.customers.refresh_review(
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
            path_template("/v1/customers/{id}/refresh_review", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )


class CustomersResourceWithRawResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.retrieve = to_raw_response_wrapper(
            customers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            customers.update,
        )
        self.delete = to_raw_response_wrapper(
            customers.delete,
        )
        self.list = to_raw_response_wrapper(
            customers.list,
        )
        self.create = to_raw_response_wrapper(
            customers.create,
        )
        self.list_unmasked = to_raw_response_wrapper(
            customers.list_unmasked,
        )
        self.refresh_review = to_raw_response_wrapper(
            customers.refresh_review,
        )

    @cached_property
    def review(self) -> ReviewResourceWithRawResponse:
        return ReviewResourceWithRawResponse(self._customers.review)


class AsyncCustomersResourceWithRawResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.retrieve = async_to_raw_response_wrapper(
            customers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            customers.update,
        )
        self.delete = async_to_raw_response_wrapper(
            customers.delete,
        )
        self.list = async_to_raw_response_wrapper(
            customers.list,
        )
        self.create = async_to_raw_response_wrapper(
            customers.create,
        )
        self.list_unmasked = async_to_raw_response_wrapper(
            customers.list_unmasked,
        )
        self.refresh_review = async_to_raw_response_wrapper(
            customers.refresh_review,
        )

    @cached_property
    def review(self) -> AsyncReviewResourceWithRawResponse:
        return AsyncReviewResourceWithRawResponse(self._customers.review)


class CustomersResourceWithStreamingResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.retrieve = to_streamed_response_wrapper(
            customers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            customers.update,
        )
        self.delete = to_streamed_response_wrapper(
            customers.delete,
        )
        self.list = to_streamed_response_wrapper(
            customers.list,
        )
        self.create = to_streamed_response_wrapper(
            customers.create,
        )
        self.list_unmasked = to_streamed_response_wrapper(
            customers.list_unmasked,
        )
        self.refresh_review = to_streamed_response_wrapper(
            customers.refresh_review,
        )

    @cached_property
    def review(self) -> ReviewResourceWithStreamingResponse:
        return ReviewResourceWithStreamingResponse(self._customers.review)


class AsyncCustomersResourceWithStreamingResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.retrieve = async_to_streamed_response_wrapper(
            customers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            customers.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            customers.delete,
        )
        self.list = async_to_streamed_response_wrapper(
            customers.list,
        )
        self.create = async_to_streamed_response_wrapper(
            customers.create,
        )
        self.list_unmasked = async_to_streamed_response_wrapper(
            customers.list_unmasked,
        )
        self.refresh_review = async_to_streamed_response_wrapper(
            customers.refresh_review,
        )

    @cached_property
    def review(self) -> AsyncReviewResourceWithStreamingResponse:
        return AsyncReviewResourceWithStreamingResponse(self._customers.review)

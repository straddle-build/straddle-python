# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict, Mapping, Optional, Union, cast
from datetime import date
from .._types import FileTypes

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._files import deepcopy_with_paths
from .._utils import extract_files, path_template, maybe_transform, async_maybe_transform, strip_not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.charge_response import ChargeResponse
from ..types import (
    charge_update_params,
    charge_create_params,
    charge_hold_params,
    charge_release_params,
    charge_cancel_params,
    charge_resubmit_params,
    charge_refund_params,
    charge_upload_authorization_proof_params,
)
from ..types.consent_type import ConsentType
from ..types.payment_device_param import PaymentDeviceParam
from ..types.charge_configuration_param import ChargeConfigurationParam
from ..types.unmasked_charge_response import UnmaskedChargeResponse
from ..types.payout_response import PayoutResponse

__all__ = ["ChargesResource", "AsyncChargesResource"]


class ChargesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChargesResourceWithRawResponse:
        return ChargesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChargesResourceWithStreamingResponse:
        return ChargesResourceWithStreamingResponse(self)

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
    ) -> ChargeResponse:
        """
        Returns a charge by its unique identifier.

        Args:
            id: Unique identifier for the charge.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChargeResponse: OK

        Example:
            ```python
            charge = client.charges.retrieve(
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
            path_template("/v1/charges/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChargeResponse,
        )

    def update(
        self,
        id: str,
        *,
        description: Optional[str],
        amount: int,
        payment_date: Union[str, date],
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
    ) -> ChargeResponse:
        """
        Updates the description, amount, `payment_date`, or metadata. The charge must have a status of `created` or `on_hold`.

        Args:
            id: Unique identifier for the charge.
            description: Updated description for the charge.
            amount: Amount in cents.
            payment_date: New date for Straddle to submit the charge for processing.
            metadata: Replacement metadata for the charge. Up to 20 user-defined string key-value pairs.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChargeResponse: OK

        Example:
            ```python
            charge = client.charges.update(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                description="Monthly subscription fee",
                amount=10000,
                payment_date="2024-01-01",
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
            path_template("/v1/charges/{id}", **{"id": id}),
            body=maybe_transform(
                {
                    "description": description,
                    "amount": amount,
                    "payment_date": payment_date,
                    "metadata": metadata,
                },
                charge_update_params.ChargeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChargeResponse,
        )

    def create(
        self,
        *,
        paykey: str,
        description: Optional[str],
        amount: int,
        currency: str,
        payment_date: Union[str, date],
        consent_type: ConsentType,
        device: PaymentDeviceParam,
        external_id: str,
        config: ChargeConfigurationParam,
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
    ) -> ChargeResponse:
        """
        Creates a charge against a customer's paykey. Straddle submits the charge for processing on `payment_date` unless the charge is on hold.

        Args:
            paykey: The paykey token that identifies the customer's bank account.
            description: Description shown on the customer's bank statement where supported.
            amount: Amount in cents.
            currency: Currency code. Only `USD` is supported.
            payment_date: Date when Straddle submits the charge for processing.
            consent_type: How the customer authorized the charge. `internet` covers online and mobile authorization. `signed` covers written or PDF-signed agreements.
            device: Body parameter.
            external_id: Your unique identifier for the charge. Must be unique across charges.
            config: Body parameter.
            metadata: Up to 20 user-defined string key-value pairs.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChargeResponse: Created

        Example:
            ```python
            charge = client.charges.create(
                paykey="",
                description="Monthly subscription fee",
                amount=10000,
                currency="USD",
                payment_date="2024-01-01",
                consent_type="internet",
                device={"ip_address": "192.168.1.1"},
                external_id="",
                config={"balance_check": "enabled"},
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
            "/v1/charges",
            body=maybe_transform(
                {
                    "paykey": paykey,
                    "description": description,
                    "amount": amount,
                    "currency": currency,
                    "payment_date": payment_date,
                    "consent_type": consent_type,
                    "device": device,
                    "external_id": external_id,
                    "config": config,
                    "metadata": metadata,
                },
                charge_create_params.ChargeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChargeResponse,
        )

    def hold(
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
    ) -> ChargeResponse:
        """
        Places a charge on hold to prevent submission for processing. The charge must have a status of `created` or `scheduled`.

        Args:
            id: Unique identifier for the charge.
            reason: Message explaining the charge status change.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChargeResponse: OK

        Example:
            ```python
            charge = client.charges.hold(
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
            path_template("/v1/charges/{id}/hold", **{"id": id}),
            body=maybe_transform(
                {"reason": reason},
                charge_hold_params.ChargeHoldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChargeResponse,
        )

    def release(
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
    ) -> ChargeResponse:
        """
        Releases a charge from `on_hold` and returns it to `created` for submission on `payment_date`.

        Args:
            id: Unique identifier for the charge.
            reason: Message explaining the charge status change.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChargeResponse: OK

        Example:
            ```python
            charge = client.charges.release(
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
            path_template("/v1/charges/{id}/release", **{"id": id}),
            body=maybe_transform(
                {"reason": reason},
                charge_release_params.ChargeReleaseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChargeResponse,
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
    ) -> ChargeResponse:
        """
        Cancels a charge. The charge must have a status of `created`, `scheduled`, or `on_hold`.

        Args:
            id: Unique identifier for the charge.
            reason: Message explaining the charge status change.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChargeResponse: OK

        Example:
            ```python
            charge = client.charges.cancel(
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
            path_template("/v1/charges/{id}/cancel", **{"id": id}),
            body=maybe_transform(
                {"reason": reason},
                charge_cancel_params.ChargeCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChargeResponse,
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
    ) -> UnmaskedChargeResponse:
        """
        Return a charge with its sensitive fields unmasked.

        Args:
            id: Unique identifier for the charge.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UnmaskedChargeResponse: OK

        Example:
            ```python
            charge = client.charges.list_unmasked(
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
            path_template("/v1/charges/{id}/unmask", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnmaskedChargeResponse,
        )

    def resubmit(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        payment_date: Optional[Union[str, date]] | Omit = omit,
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
    ) -> ChargeResponse:
        """
        Creates a new charge from a failed, reversed, or cancelled charge. The request can override `description`, `external_id`, and `payment_date`. Other payment details come from the original charge.

        Args:
            id: Unique identifier for the charge.
            description: Description for the resubmitted charge. Defaults to the original description if omitted.
            payment_date: Date when Straddle submits the resubmitted charge for processing. Defaults to today if omitted.
            external_id: Your unique identifier for the resubmitted charge. Defaults to a new value if omitted.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChargeResponse: Created

        Example:
            ```python
            charge = client.charges.resubmit(
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
        return self._post(
            path_template("/v1/charges/{id}/resubmit", **{"id": id}),
            body=maybe_transform(
                {
                    "description": description,
                    "payment_date": payment_date,
                    "external_id": external_id,
                },
                charge_resubmit_params.ChargeResubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChargeResponse,
        )

    def refund(
        self,
        id: str,
        *,
        amount: Optional[int] | Omit = omit,
        description: Optional[str] | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        payment_date: Optional[Union[str, date]] | Omit = omit,
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
    ) -> PayoutResponse:
        """
        Creates a payout to return funds from a paid charge to the customer's bank account. The payout is linked to the charge through `related_payments`. A charge can be refunded once, either fully or partially.

        Args:
            id: Unique identifier for the charge.
            amount: Refund amount in cents. `null` refunds the full original amount. A value must be greater than zero and no more than the original charge amount.
            description: Description for the refund payout. Defaults to a description that identifies the original charge.
            external_id: Your unique identifier for the refund. Defaults to a new value if omitted.
            payment_date: Date when Straddle submits the refund payout for processing. Defaults to today if omitted.
            metadata: User-defined string key-value pairs for the refund payout.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PayoutResponse: Created

        Example:
            ```python
            charge = client.charges.refund(
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
        return self._post(
            path_template("/v1/charges/{id}/refund", **{"id": id}),
            body=maybe_transform(
                {
                    "amount": amount,
                    "description": description,
                    "external_id": external_id,
                    "payment_date": payment_date,
                    "metadata": metadata,
                },
                charge_refund_params.ChargeRefundParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayoutResponse,
        )

    def upload_authorization_proof(
        self,
        id: str,
        *,
        file: FileTypes,
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
    ) -> ChargeResponse:
        """
        Uploads a proof-of-authorization document for a charge. A later upload adds another document and does not replace an existing one.

        Args:
            id: Unique identifier for the charge.
            file: The document file to upload as proof of authorization for this charge. Supported file types are PDF (.pdf), PNG (.png), JPEG (.jpg, .jpeg), Word (.doc), and Word (.docx), with a maximum file size of 10 MiB (10,485,760 bytes). Empty (0-byte) files are rejected. Uploaded files are validated for matching file signatures (magic bytes) and file extension agreement.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChargeResponse: Created

        Example:
            ```python
            charge = client.charges.upload_authorization_proof(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                file=b"",
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
        body = deepcopy_with_paths(
            {
                "File": file,
            },
            [["File"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["File"]])
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template("/v1/charges/{id}/authorization", **{"id": id}),
            body=maybe_transform(body, charge_upload_authorization_proof_params.ChargeUploadAuthorizationProofParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChargeResponse,
        )


class AsyncChargesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChargesResourceWithRawResponse:
        return AsyncChargesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChargesResourceWithStreamingResponse:
        return AsyncChargesResourceWithStreamingResponse(self)

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
    ) -> ChargeResponse:
        """
        Returns a charge by its unique identifier.

        Args:
            id: Unique identifier for the charge.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChargeResponse: OK

        Example:
            ```python
            charge = await client.charges.retrieve(
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
            path_template("/v1/charges/{id}", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChargeResponse,
        )

    async def update(
        self,
        id: str,
        *,
        description: Optional[str],
        amount: int,
        payment_date: Union[str, date],
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
    ) -> ChargeResponse:
        """
        Updates the description, amount, `payment_date`, or metadata. The charge must have a status of `created` or `on_hold`.

        Args:
            id: Unique identifier for the charge.
            description: Updated description for the charge.
            amount: Amount in cents.
            payment_date: New date for Straddle to submit the charge for processing.
            metadata: Replacement metadata for the charge. Up to 20 user-defined string key-value pairs.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChargeResponse: OK

        Example:
            ```python
            charge = await client.charges.update(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                description="Monthly subscription fee",
                amount=10000,
                payment_date="2024-01-01",
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
            path_template("/v1/charges/{id}", **{"id": id}),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "amount": amount,
                    "payment_date": payment_date,
                    "metadata": metadata,
                },
                charge_update_params.ChargeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChargeResponse,
        )

    async def create(
        self,
        *,
        paykey: str,
        description: Optional[str],
        amount: int,
        currency: str,
        payment_date: Union[str, date],
        consent_type: ConsentType,
        device: PaymentDeviceParam,
        external_id: str,
        config: ChargeConfigurationParam,
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
    ) -> ChargeResponse:
        """
        Creates a charge against a customer's paykey. Straddle submits the charge for processing on `payment_date` unless the charge is on hold.

        Args:
            paykey: The paykey token that identifies the customer's bank account.
            description: Description shown on the customer's bank statement where supported.
            amount: Amount in cents.
            currency: Currency code. Only `USD` is supported.
            payment_date: Date when Straddle submits the charge for processing.
            consent_type: How the customer authorized the charge. `internet` covers online and mobile authorization. `signed` covers written or PDF-signed agreements.
            device: Body parameter.
            external_id: Your unique identifier for the charge. Must be unique across charges.
            config: Body parameter.
            metadata: Up to 20 user-defined string key-value pairs.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChargeResponse: Created

        Example:
            ```python
            charge = await client.charges.create(
                paykey="",
                description="Monthly subscription fee",
                amount=10000,
                currency="USD",
                payment_date="2024-01-01",
                consent_type="internet",
                device={"ip_address": "192.168.1.1"},
                external_id="",
                config={"balance_check": "enabled"},
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
            "/v1/charges",
            body=await async_maybe_transform(
                {
                    "paykey": paykey,
                    "description": description,
                    "amount": amount,
                    "currency": currency,
                    "payment_date": payment_date,
                    "consent_type": consent_type,
                    "device": device,
                    "external_id": external_id,
                    "config": config,
                    "metadata": metadata,
                },
                charge_create_params.ChargeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChargeResponse,
        )

    async def hold(
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
    ) -> ChargeResponse:
        """
        Places a charge on hold to prevent submission for processing. The charge must have a status of `created` or `scheduled`.

        Args:
            id: Unique identifier for the charge.
            reason: Message explaining the charge status change.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChargeResponse: OK

        Example:
            ```python
            charge = await client.charges.hold(
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
            path_template("/v1/charges/{id}/hold", **{"id": id}),
            body=await async_maybe_transform(
                {"reason": reason},
                charge_hold_params.ChargeHoldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChargeResponse,
        )

    async def release(
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
    ) -> ChargeResponse:
        """
        Releases a charge from `on_hold` and returns it to `created` for submission on `payment_date`.

        Args:
            id: Unique identifier for the charge.
            reason: Message explaining the charge status change.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChargeResponse: OK

        Example:
            ```python
            charge = await client.charges.release(
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
            path_template("/v1/charges/{id}/release", **{"id": id}),
            body=await async_maybe_transform(
                {"reason": reason},
                charge_release_params.ChargeReleaseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChargeResponse,
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
    ) -> ChargeResponse:
        """
        Cancels a charge. The charge must have a status of `created`, `scheduled`, or `on_hold`.

        Args:
            id: Unique identifier for the charge.
            reason: Message explaining the charge status change.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChargeResponse: OK

        Example:
            ```python
            charge = await client.charges.cancel(
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
            path_template("/v1/charges/{id}/cancel", **{"id": id}),
            body=await async_maybe_transform(
                {"reason": reason},
                charge_cancel_params.ChargeCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChargeResponse,
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
    ) -> UnmaskedChargeResponse:
        """
        Return a charge with its sensitive fields unmasked.

        Args:
            id: Unique identifier for the charge.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            UnmaskedChargeResponse: OK

        Example:
            ```python
            charge = await client.charges.list_unmasked(
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
            path_template("/v1/charges/{id}/unmask", **{"id": id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnmaskedChargeResponse,
        )

    async def resubmit(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        payment_date: Optional[Union[str, date]] | Omit = omit,
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
    ) -> ChargeResponse:
        """
        Creates a new charge from a failed, reversed, or cancelled charge. The request can override `description`, `external_id`, and `payment_date`. Other payment details come from the original charge.

        Args:
            id: Unique identifier for the charge.
            description: Description for the resubmitted charge. Defaults to the original description if omitted.
            payment_date: Date when Straddle submits the resubmitted charge for processing. Defaults to today if omitted.
            external_id: Your unique identifier for the resubmitted charge. Defaults to a new value if omitted.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChargeResponse: Created

        Example:
            ```python
            charge = await client.charges.resubmit(
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
        return await self._post(
            path_template("/v1/charges/{id}/resubmit", **{"id": id}),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "payment_date": payment_date,
                    "external_id": external_id,
                },
                charge_resubmit_params.ChargeResubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChargeResponse,
        )

    async def refund(
        self,
        id: str,
        *,
        amount: Optional[int] | Omit = omit,
        description: Optional[str] | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        payment_date: Optional[Union[str, date]] | Omit = omit,
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
    ) -> PayoutResponse:
        """
        Creates a payout to return funds from a paid charge to the customer's bank account. The payout is linked to the charge through `related_payments`. A charge can be refunded once, either fully or partially.

        Args:
            id: Unique identifier for the charge.
            amount: Refund amount in cents. `null` refunds the full original amount. A value must be greater than zero and no more than the original charge amount.
            description: Description for the refund payout. Defaults to a description that identifies the original charge.
            external_id: Your unique identifier for the refund. Defaults to a new value if omitted.
            payment_date: Date when Straddle submits the refund payout for processing. Defaults to today if omitted.
            metadata: User-defined string key-value pairs for the refund payout.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            PayoutResponse: Created

        Example:
            ```python
            charge = await client.charges.refund(
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
        return await self._post(
            path_template("/v1/charges/{id}/refund", **{"id": id}),
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "description": description,
                    "external_id": external_id,
                    "payment_date": payment_date,
                    "metadata": metadata,
                },
                charge_refund_params.ChargeRefundParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayoutResponse,
        )

    async def upload_authorization_proof(
        self,
        id: str,
        *,
        file: FileTypes,
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
    ) -> ChargeResponse:
        """
        Uploads a proof-of-authorization document for a charge. A later upload adds another document and does not replace an existing one.

        Args:
            id: Unique identifier for the charge.
            file: The document file to upload as proof of authorization for this charge. Supported file types are PDF (.pdf), PNG (.png), JPEG (.jpg, .jpeg), Word (.doc), and Word (.docx), with a maximum file size of 10 MiB (10,485,760 bytes). Empty (0-byte) files are rejected. Uploaded files are validated for matching file signatures (magic bytes) and file extension agreement.
            straddle_account_id: For platform requests, the embedded account UUID that sets the request scope.
            request_id: Optional client-generated identifier for tracing one request.
            correlation_id: Optional client-generated identifier for tracing a series of related requests.
            idempotency_key: Optional client-generated key for an idempotent request.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ChargeResponse: Created

        Example:
            ```python
            charge = await client.charges.upload_authorization_proof(
                id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
                file=b"",
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
        body = deepcopy_with_paths(
            {
                "File": file,
            },
            [["File"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["File"]])
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template("/v1/charges/{id}/authorization", **{"id": id}),
            body=await async_maybe_transform(
                body, charge_upload_authorization_proof_params.ChargeUploadAuthorizationProofParams
            ),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChargeResponse,
        )


class ChargesResourceWithRawResponse:
    def __init__(self, charges: ChargesResource) -> None:
        self._charges = charges

        self.retrieve = to_raw_response_wrapper(
            charges.retrieve,
        )
        self.update = to_raw_response_wrapper(
            charges.update,
        )
        self.create = to_raw_response_wrapper(
            charges.create,
        )
        self.hold = to_raw_response_wrapper(
            charges.hold,
        )
        self.release = to_raw_response_wrapper(
            charges.release,
        )
        self.cancel = to_raw_response_wrapper(
            charges.cancel,
        )
        self.list_unmasked = to_raw_response_wrapper(
            charges.list_unmasked,
        )
        self.resubmit = to_raw_response_wrapper(
            charges.resubmit,
        )
        self.refund = to_raw_response_wrapper(
            charges.refund,
        )
        self.upload_authorization_proof = to_raw_response_wrapper(
            charges.upload_authorization_proof,
        )


class AsyncChargesResourceWithRawResponse:
    def __init__(self, charges: AsyncChargesResource) -> None:
        self._charges = charges

        self.retrieve = async_to_raw_response_wrapper(
            charges.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            charges.update,
        )
        self.create = async_to_raw_response_wrapper(
            charges.create,
        )
        self.hold = async_to_raw_response_wrapper(
            charges.hold,
        )
        self.release = async_to_raw_response_wrapper(
            charges.release,
        )
        self.cancel = async_to_raw_response_wrapper(
            charges.cancel,
        )
        self.list_unmasked = async_to_raw_response_wrapper(
            charges.list_unmasked,
        )
        self.resubmit = async_to_raw_response_wrapper(
            charges.resubmit,
        )
        self.refund = async_to_raw_response_wrapper(
            charges.refund,
        )
        self.upload_authorization_proof = async_to_raw_response_wrapper(
            charges.upload_authorization_proof,
        )


class ChargesResourceWithStreamingResponse:
    def __init__(self, charges: ChargesResource) -> None:
        self._charges = charges

        self.retrieve = to_streamed_response_wrapper(
            charges.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            charges.update,
        )
        self.create = to_streamed_response_wrapper(
            charges.create,
        )
        self.hold = to_streamed_response_wrapper(
            charges.hold,
        )
        self.release = to_streamed_response_wrapper(
            charges.release,
        )
        self.cancel = to_streamed_response_wrapper(
            charges.cancel,
        )
        self.list_unmasked = to_streamed_response_wrapper(
            charges.list_unmasked,
        )
        self.resubmit = to_streamed_response_wrapper(
            charges.resubmit,
        )
        self.refund = to_streamed_response_wrapper(
            charges.refund,
        )
        self.upload_authorization_proof = to_streamed_response_wrapper(
            charges.upload_authorization_proof,
        )


class AsyncChargesResourceWithStreamingResponse:
    def __init__(self, charges: AsyncChargesResource) -> None:
        self._charges = charges

        self.retrieve = async_to_streamed_response_wrapper(
            charges.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            charges.update,
        )
        self.create = async_to_streamed_response_wrapper(
            charges.create,
        )
        self.hold = async_to_streamed_response_wrapper(
            charges.hold,
        )
        self.release = async_to_streamed_response_wrapper(
            charges.release,
        )
        self.cancel = async_to_streamed_response_wrapper(
            charges.cancel,
        )
        self.list_unmasked = async_to_streamed_response_wrapper(
            charges.list_unmasked,
        )
        self.resubmit = async_to_streamed_response_wrapper(
            charges.resubmit,
        )
        self.refund = async_to_streamed_response_wrapper(
            charges.refund,
        )
        self.upload_authorization_proof = async_to_streamed_response_wrapper(
            charges.upload_authorization_proof,
        )

# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import os
import threading
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, is_mapping_t, get_async_library
from ._compat import cached_property
from ._exceptions import APIStatusError, StraddleAPIError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._version import __version__

if TYPE_CHECKING:
    from .resources import (
        accounts,
        capability_requests,
        linked_bank_accounts,
        organizations,
        representatives,
        bridge,
        customers,
        paykeys,
        charges,
        funding_events,
        payments,
        payouts,
        account_settings,
        webhooks,
    )
    from .resources.accounts import AccountsResource, AsyncAccountsResource
    from .resources.capability_requests import CapabilityRequestsResource, AsyncCapabilityRequestsResource
    from .resources.linked_bank_accounts import LinkedBankAccountsResource, AsyncLinkedBankAccountsResource
    from .resources.organizations import OrganizationsResource, AsyncOrganizationsResource
    from .resources.representatives import RepresentativesResource, AsyncRepresentativesResource
    from .resources.bridge import BridgeResource, AsyncBridgeResource
    from .resources.customers import CustomersResource, AsyncCustomersResource
    from .resources.paykeys import PaykeysResource, AsyncPaykeysResource
    from .resources.charges import ChargesResource, AsyncChargesResource
    from .resources.funding_events import FundingEventsResource, AsyncFundingEventsResource
    from .resources.payments import PaymentsResource, AsyncPaymentsResource
    from .resources.payouts import PayoutsResource, AsyncPayoutsResource
    from .resources.account_settings import AccountSettingsResource, AsyncAccountSettingsResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource

# Serializes lazy resource imports so concurrent cold access from multiple
# threads cannot deadlock on CPython import locks (see CPython 3.14).
_RESOURCE_IMPORT_LOCK = threading.RLock()

__all__ = [
    "StraddleAPI",
    "AsyncStraddleAPI",
    "Client",
    "AsyncClient",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
]


class StraddleAPI(SyncAPIClient):
    # client options
    bearer: str
    webhook_secret: str | None

    def __init__(
        self,
        *,
        bearer: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous StraddleAPI client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer` from `BEARER`
        - `webhook_secret` from `STRADDLE_WEBHOOK_SECRET`
        """
        if bearer is None:
            bearer = os.environ.get("BEARER")
        if bearer is None:
            raise StraddleAPIError(
                "The bearer client option must be set either by passing bearer to the client or by setting the BEARER environment variable"
            )
        self.bearer = bearer
        if webhook_secret is None:
            webhook_secret = os.environ.get("STRADDLE_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret
        if base_url is None:
            base_url = os.environ.get("STRADDLE_BASE_URL")
        if base_url is None:
            base_url = "https://sandbox.straddle.com"
        custom_headers_env = os.environ.get("STRADDLE_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self._idempotency_header = None
        self._default_stream_cls = Stream

    @cached_property
    def accounts(self) -> "AccountsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.accounts import AccountsResource
        return AccountsResource(self)

    @cached_property
    def capability_requests(self) -> "CapabilityRequestsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.capability_requests import CapabilityRequestsResource
        return CapabilityRequestsResource(self)

    @cached_property
    def linked_bank_accounts(self) -> "LinkedBankAccountsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.linked_bank_accounts import LinkedBankAccountsResource
        return LinkedBankAccountsResource(self)

    @cached_property
    def organizations(self) -> "OrganizationsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organizations import OrganizationsResource
        return OrganizationsResource(self)

    @cached_property
    def representatives(self) -> "RepresentativesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.representatives import RepresentativesResource
        return RepresentativesResource(self)

    @cached_property
    def bridge(self) -> "BridgeResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.bridge import BridgeResource
        return BridgeResource(self)

    @cached_property
    def customers(self) -> "CustomersResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.customers import CustomersResource
        return CustomersResource(self)

    @cached_property
    def paykeys(self) -> "PaykeysResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.paykeys import PaykeysResource
        return PaykeysResource(self)

    @cached_property
    def charges(self) -> "ChargesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.charges import ChargesResource
        return ChargesResource(self)

    @cached_property
    def funding_events(self) -> "FundingEventsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.funding_events import FundingEventsResource
        return FundingEventsResource(self)

    @cached_property
    def payments(self) -> "PaymentsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.payments import PaymentsResource
        return PaymentsResource(self)

    @cached_property
    def payouts(self) -> "PayoutsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.payouts import PayoutsResource
        return PayoutsResource(self)

    @cached_property
    def account_settings(self) -> "AccountSettingsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.account_settings import AccountSettingsResource
        return AccountSettingsResource(self)

    @cached_property
    def webhooks(self) -> "WebhooksResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.webhooks import WebhooksResource
        return WebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> StraddleAPIWithRawResponse:
        return StraddleAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StraddleAPIWithStreamedResponse:
        return StraddleAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {
            **self._bearer_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @property
    def _bearer_header_auth(self) -> dict[str, str]:
        value = self.bearer
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        raise TypeError(
            '"Could not resolve authentication method. Expected the bearer to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        bearer: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        return self.__class__(
            bearer=bearer or self.bearer,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncStraddleAPI(AsyncAPIClient):
    # client options
    bearer: str
    webhook_secret: str | None

    def __init__(
        self,
        *,
        bearer: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncStraddleAPI client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer` from `BEARER`
        - `webhook_secret` from `STRADDLE_WEBHOOK_SECRET`
        """
        if bearer is None:
            bearer = os.environ.get("BEARER")
        if bearer is None:
            raise StraddleAPIError(
                "The bearer client option must be set either by passing bearer to the client or by setting the BEARER environment variable"
            )
        self.bearer = bearer
        if webhook_secret is None:
            webhook_secret = os.environ.get("STRADDLE_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret
        if base_url is None:
            base_url = os.environ.get("STRADDLE_BASE_URL")
        if base_url is None:
            base_url = "https://sandbox.straddle.com"
        custom_headers_env = os.environ.get("STRADDLE_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self._idempotency_header = None
        self._default_stream_cls = AsyncStream

    @cached_property
    def accounts(self) -> "AsyncAccountsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.accounts import AsyncAccountsResource
        return AsyncAccountsResource(self)

    @cached_property
    def capability_requests(self) -> "AsyncCapabilityRequestsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.capability_requests import AsyncCapabilityRequestsResource
        return AsyncCapabilityRequestsResource(self)

    @cached_property
    def linked_bank_accounts(self) -> "AsyncLinkedBankAccountsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.linked_bank_accounts import AsyncLinkedBankAccountsResource
        return AsyncLinkedBankAccountsResource(self)

    @cached_property
    def organizations(self) -> "AsyncOrganizationsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organizations import AsyncOrganizationsResource
        return AsyncOrganizationsResource(self)

    @cached_property
    def representatives(self) -> "AsyncRepresentativesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.representatives import AsyncRepresentativesResource
        return AsyncRepresentativesResource(self)

    @cached_property
    def bridge(self) -> "AsyncBridgeResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.bridge import AsyncBridgeResource
        return AsyncBridgeResource(self)

    @cached_property
    def customers(self) -> "AsyncCustomersResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.customers import AsyncCustomersResource
        return AsyncCustomersResource(self)

    @cached_property
    def paykeys(self) -> "AsyncPaykeysResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.paykeys import AsyncPaykeysResource
        return AsyncPaykeysResource(self)

    @cached_property
    def charges(self) -> "AsyncChargesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.charges import AsyncChargesResource
        return AsyncChargesResource(self)

    @cached_property
    def funding_events(self) -> "AsyncFundingEventsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.funding_events import AsyncFundingEventsResource
        return AsyncFundingEventsResource(self)

    @cached_property
    def payments(self) -> "AsyncPaymentsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.payments import AsyncPaymentsResource
        return AsyncPaymentsResource(self)

    @cached_property
    def payouts(self) -> "AsyncPayoutsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.payouts import AsyncPayoutsResource
        return AsyncPayoutsResource(self)

    @cached_property
    def account_settings(self) -> "AsyncAccountSettingsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.account_settings import AsyncAccountSettingsResource
        return AsyncAccountSettingsResource(self)

    @cached_property
    def webhooks(self) -> "AsyncWebhooksResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.webhooks import AsyncWebhooksResource
        return AsyncWebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncStraddleAPIWithRawResponse:
        return AsyncStraddleAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStraddleAPIWithStreamedResponse:
        return AsyncStraddleAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {
            **self._bearer_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {}

    @property
    def _bearer_header_auth(self) -> dict[str, str]:
        value = self.bearer
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        raise TypeError(
            '"Could not resolve authentication method. Expected the bearer to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        bearer: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        return self.__class__(
            bearer=bearer or self.bearer,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class StraddleAPIWithRawResponse:
    _client: StraddleAPI

    def __init__(self, client: StraddleAPI) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.accounts import AccountsResourceWithRawResponse
        return AccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def capability_requests(self) -> capability_requests.CapabilityRequestsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.capability_requests import CapabilityRequestsResourceWithRawResponse
        return CapabilityRequestsResourceWithRawResponse(self._client.capability_requests)

    @cached_property
    def linked_bank_accounts(self) -> linked_bank_accounts.LinkedBankAccountsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.linked_bank_accounts import LinkedBankAccountsResourceWithRawResponse
        return LinkedBankAccountsResourceWithRawResponse(self._client.linked_bank_accounts)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organizations import OrganizationsResourceWithRawResponse
        return OrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def representatives(self) -> representatives.RepresentativesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.representatives import RepresentativesResourceWithRawResponse
        return RepresentativesResourceWithRawResponse(self._client.representatives)

    @cached_property
    def bridge(self) -> bridge.BridgeResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.bridge import BridgeResourceWithRawResponse
        return BridgeResourceWithRawResponse(self._client.bridge)

    @cached_property
    def customers(self) -> customers.CustomersResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.customers import CustomersResourceWithRawResponse
        return CustomersResourceWithRawResponse(self._client.customers)

    @cached_property
    def paykeys(self) -> paykeys.PaykeysResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.paykeys import PaykeysResourceWithRawResponse
        return PaykeysResourceWithRawResponse(self._client.paykeys)

    @cached_property
    def charges(self) -> charges.ChargesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.charges import ChargesResourceWithRawResponse
        return ChargesResourceWithRawResponse(self._client.charges)

    @cached_property
    def funding_events(self) -> funding_events.FundingEventsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.funding_events import FundingEventsResourceWithRawResponse
        return FundingEventsResourceWithRawResponse(self._client.funding_events)

    @cached_property
    def payments(self) -> payments.PaymentsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.payments import PaymentsResourceWithRawResponse
        return PaymentsResourceWithRawResponse(self._client.payments)

    @cached_property
    def payouts(self) -> payouts.PayoutsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.payouts import PayoutsResourceWithRawResponse
        return PayoutsResourceWithRawResponse(self._client.payouts)

    @cached_property
    def account_settings(self) -> account_settings.AccountSettingsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.account_settings import AccountSettingsResourceWithRawResponse
        return AccountSettingsResourceWithRawResponse(self._client.account_settings)


class AsyncStraddleAPIWithRawResponse:
    _client: AsyncStraddleAPI

    def __init__(self, client: AsyncStraddleAPI) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.accounts import AsyncAccountsResourceWithRawResponse
        return AsyncAccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def capability_requests(self) -> capability_requests.AsyncCapabilityRequestsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.capability_requests import AsyncCapabilityRequestsResourceWithRawResponse
        return AsyncCapabilityRequestsResourceWithRawResponse(self._client.capability_requests)

    @cached_property
    def linked_bank_accounts(self) -> linked_bank_accounts.AsyncLinkedBankAccountsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.linked_bank_accounts import AsyncLinkedBankAccountsResourceWithRawResponse
        return AsyncLinkedBankAccountsResourceWithRawResponse(self._client.linked_bank_accounts)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organizations import AsyncOrganizationsResourceWithRawResponse
        return AsyncOrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def representatives(self) -> representatives.AsyncRepresentativesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.representatives import AsyncRepresentativesResourceWithRawResponse
        return AsyncRepresentativesResourceWithRawResponse(self._client.representatives)

    @cached_property
    def bridge(self) -> bridge.AsyncBridgeResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.bridge import AsyncBridgeResourceWithRawResponse
        return AsyncBridgeResourceWithRawResponse(self._client.bridge)

    @cached_property
    def customers(self) -> customers.AsyncCustomersResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.customers import AsyncCustomersResourceWithRawResponse
        return AsyncCustomersResourceWithRawResponse(self._client.customers)

    @cached_property
    def paykeys(self) -> paykeys.AsyncPaykeysResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.paykeys import AsyncPaykeysResourceWithRawResponse
        return AsyncPaykeysResourceWithRawResponse(self._client.paykeys)

    @cached_property
    def charges(self) -> charges.AsyncChargesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.charges import AsyncChargesResourceWithRawResponse
        return AsyncChargesResourceWithRawResponse(self._client.charges)

    @cached_property
    def funding_events(self) -> funding_events.AsyncFundingEventsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.funding_events import AsyncFundingEventsResourceWithRawResponse
        return AsyncFundingEventsResourceWithRawResponse(self._client.funding_events)

    @cached_property
    def payments(self) -> payments.AsyncPaymentsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.payments import AsyncPaymentsResourceWithRawResponse
        return AsyncPaymentsResourceWithRawResponse(self._client.payments)

    @cached_property
    def payouts(self) -> payouts.AsyncPayoutsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.payouts import AsyncPayoutsResourceWithRawResponse
        return AsyncPayoutsResourceWithRawResponse(self._client.payouts)

    @cached_property
    def account_settings(self) -> account_settings.AsyncAccountSettingsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.account_settings import AsyncAccountSettingsResourceWithRawResponse
        return AsyncAccountSettingsResourceWithRawResponse(self._client.account_settings)


class StraddleAPIWithStreamedResponse:
    _client: StraddleAPI

    def __init__(self, client: StraddleAPI) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.accounts import AccountsResourceWithStreamingResponse
        return AccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def capability_requests(self) -> capability_requests.CapabilityRequestsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.capability_requests import CapabilityRequestsResourceWithStreamingResponse
        return CapabilityRequestsResourceWithStreamingResponse(self._client.capability_requests)

    @cached_property
    def linked_bank_accounts(self) -> linked_bank_accounts.LinkedBankAccountsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.linked_bank_accounts import LinkedBankAccountsResourceWithStreamingResponse
        return LinkedBankAccountsResourceWithStreamingResponse(self._client.linked_bank_accounts)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organizations import OrganizationsResourceWithStreamingResponse
        return OrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def representatives(self) -> representatives.RepresentativesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.representatives import RepresentativesResourceWithStreamingResponse
        return RepresentativesResourceWithStreamingResponse(self._client.representatives)

    @cached_property
    def bridge(self) -> bridge.BridgeResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.bridge import BridgeResourceWithStreamingResponse
        return BridgeResourceWithStreamingResponse(self._client.bridge)

    @cached_property
    def customers(self) -> customers.CustomersResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.customers import CustomersResourceWithStreamingResponse
        return CustomersResourceWithStreamingResponse(self._client.customers)

    @cached_property
    def paykeys(self) -> paykeys.PaykeysResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.paykeys import PaykeysResourceWithStreamingResponse
        return PaykeysResourceWithStreamingResponse(self._client.paykeys)

    @cached_property
    def charges(self) -> charges.ChargesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.charges import ChargesResourceWithStreamingResponse
        return ChargesResourceWithStreamingResponse(self._client.charges)

    @cached_property
    def funding_events(self) -> funding_events.FundingEventsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.funding_events import FundingEventsResourceWithStreamingResponse
        return FundingEventsResourceWithStreamingResponse(self._client.funding_events)

    @cached_property
    def payments(self) -> payments.PaymentsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.payments import PaymentsResourceWithStreamingResponse
        return PaymentsResourceWithStreamingResponse(self._client.payments)

    @cached_property
    def payouts(self) -> payouts.PayoutsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.payouts import PayoutsResourceWithStreamingResponse
        return PayoutsResourceWithStreamingResponse(self._client.payouts)

    @cached_property
    def account_settings(self) -> account_settings.AccountSettingsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.account_settings import AccountSettingsResourceWithStreamingResponse
        return AccountSettingsResourceWithStreamingResponse(self._client.account_settings)


class AsyncStraddleAPIWithStreamedResponse:
    _client: AsyncStraddleAPI

    def __init__(self, client: AsyncStraddleAPI) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.accounts import AsyncAccountsResourceWithStreamingResponse
        return AsyncAccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def capability_requests(self) -> capability_requests.AsyncCapabilityRequestsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.capability_requests import AsyncCapabilityRequestsResourceWithStreamingResponse
        return AsyncCapabilityRequestsResourceWithStreamingResponse(self._client.capability_requests)

    @cached_property
    def linked_bank_accounts(self) -> linked_bank_accounts.AsyncLinkedBankAccountsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.linked_bank_accounts import AsyncLinkedBankAccountsResourceWithStreamingResponse
        return AsyncLinkedBankAccountsResourceWithStreamingResponse(self._client.linked_bank_accounts)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.organizations import AsyncOrganizationsResourceWithStreamingResponse
        return AsyncOrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def representatives(self) -> representatives.AsyncRepresentativesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.representatives import AsyncRepresentativesResourceWithStreamingResponse
        return AsyncRepresentativesResourceWithStreamingResponse(self._client.representatives)

    @cached_property
    def bridge(self) -> bridge.AsyncBridgeResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.bridge import AsyncBridgeResourceWithStreamingResponse
        return AsyncBridgeResourceWithStreamingResponse(self._client.bridge)

    @cached_property
    def customers(self) -> customers.AsyncCustomersResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.customers import AsyncCustomersResourceWithStreamingResponse
        return AsyncCustomersResourceWithStreamingResponse(self._client.customers)

    @cached_property
    def paykeys(self) -> paykeys.AsyncPaykeysResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.paykeys import AsyncPaykeysResourceWithStreamingResponse
        return AsyncPaykeysResourceWithStreamingResponse(self._client.paykeys)

    @cached_property
    def charges(self) -> charges.AsyncChargesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.charges import AsyncChargesResourceWithStreamingResponse
        return AsyncChargesResourceWithStreamingResponse(self._client.charges)

    @cached_property
    def funding_events(self) -> funding_events.AsyncFundingEventsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.funding_events import AsyncFundingEventsResourceWithStreamingResponse
        return AsyncFundingEventsResourceWithStreamingResponse(self._client.funding_events)

    @cached_property
    def payments(self) -> payments.AsyncPaymentsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.payments import AsyncPaymentsResourceWithStreamingResponse
        return AsyncPaymentsResourceWithStreamingResponse(self._client.payments)

    @cached_property
    def payouts(self) -> payouts.AsyncPayoutsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.payouts import AsyncPayoutsResourceWithStreamingResponse
        return AsyncPayoutsResourceWithStreamingResponse(self._client.payouts)

    @cached_property
    def account_settings(self) -> account_settings.AsyncAccountSettingsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.account_settings import AsyncAccountSettingsResourceWithStreamingResponse
        return AsyncAccountSettingsResourceWithStreamingResponse(self._client.account_settings)


# Alias names for the documented `Client` / `AsyncClient` symbols.
Client = StraddleAPI
AsyncClient = AsyncStraddleAPI

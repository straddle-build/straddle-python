# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Optional, Union
from datetime import date
from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

from .payment_device_param import PaymentDeviceParam
from .payout_configuration_param import PayoutConfigurationParam

__all__ = ["PayoutCreateParams"]


class PayoutCreateParams(TypedDict, total=False):
    paykey: Required[str]
    """The paykey token that identifies the customer's bank account."""

    description: Required[Optional[str]]
    """Description shown on the customer's bank statement where supported."""

    amount: Required[int]
    """Amount in cents."""

    currency: Required[str]
    """Currency code. Only `USD` is supported."""

    payment_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Date when Straddle submits the payout for processing."""

    device: Required[PaymentDeviceParam]
    """Device used when the customer authorized the payout."""

    external_id: Required[str]
    """Your unique identifier for the payout. Must be unique across payouts."""

    config: PayoutConfigurationParam

    metadata: Optional[Dict[str, str]]
    """Up to 20 user-defined string key-value pairs."""

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

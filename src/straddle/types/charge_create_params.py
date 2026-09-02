# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Optional, Union
from datetime import date
from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

from .consent_type import ConsentType
from .payment_device_param import PaymentDeviceParam
from .charge_configuration_param import ChargeConfigurationParam

__all__ = ["ChargeCreateParams"]


class ChargeCreateParams(TypedDict, total=False):
    paykey: Required[str]
    """The paykey token that identifies the customer's bank account."""

    description: Required[Optional[str]]
    """Description shown on the customer's bank statement where supported."""

    amount: Required[int]
    """Amount in cents."""

    currency: Required[str]
    """Currency code. Only `USD` is supported."""

    payment_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Date when Straddle submits the charge for processing."""

    consent_type: Required[ConsentType]
    """How the customer authorized the charge. `internet` covers online and mobile authorization. `signed` covers written or PDF-signed agreements."""

    device: Required[PaymentDeviceParam]

    external_id: Required[str]
    """Your unique identifier for the charge. Must be unique across charges."""

    config: Required[ChargeConfigurationParam]

    metadata: Optional[Dict[str, str]]
    """Up to 20 user-defined string key-value pairs."""

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

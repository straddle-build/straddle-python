# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Optional, Union
from datetime import date
from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["PayoutUpdateParams"]


class PayoutUpdateParams(TypedDict, total=False):
    description: Required[Optional[str]]
    """Updated description for the payout."""

    amount: Required[int]
    """Amount in cents."""

    payment_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """New date for Straddle to submit the payout for processing."""

    metadata: Optional[Dict[str, str]]
    """Replacement metadata for the payout. Up to 20 user-defined string key-value pairs."""

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

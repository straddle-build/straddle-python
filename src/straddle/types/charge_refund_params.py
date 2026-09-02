# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Optional, Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ChargeRefundParams"]


class ChargeRefundParams(TypedDict, total=False):
    amount: Optional[int]
    """Refund amount in cents. `null` refunds the full original amount. A value must be greater than zero and no more than the original charge amount."""

    description: Optional[str]
    """Description for the refund payout. Defaults to a description that identifies the original charge."""

    external_id: Optional[str]
    """Your unique identifier for the refund. Defaults to a new value if omitted."""

    payment_date: Annotated[Optional[Union[str, date]], PropertyInfo(format="iso8601")]
    """Date when Straddle submits the refund payout for processing. Defaults to today if omitted."""

    metadata: Optional[Dict[str, str]]
    """User-defined string key-value pairs for the refund payout."""

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional, Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PayoutResubmitParams"]


class PayoutResubmitParams(TypedDict, total=False):
    description: Optional[str]
    """Description for the resubmitted payout. Defaults to the original description if omitted."""

    payment_date: Annotated[Optional[Union[str, date]], PropertyInfo(format="iso8601")]
    """Date when Straddle submits the resubmitted payout for processing. Defaults to today if omitted."""

    external_id: Optional[str]
    """Your unique identifier for the resubmitted payout. Defaults to a new value if omitted."""

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

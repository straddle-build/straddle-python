# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date, datetime
from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

from .sort_order import SortOrder
from .payment_type import PaymentType
from .payment_status import PaymentStatus
from .payment_status_reason import PaymentStatusReason
from .payment_status_source import PaymentStatusSource

__all__ = ["PaymentListParams"]


class PaymentListParams(TypedDict, total=False):
    page_number: int
    """Page number to return."""

    page_size: int
    """Number of results to return per page."""

    sort_by: Literal["created_at", "payment_date", "effective_at", "id", "amount", "updated_at"]
    """Field used to sort the results."""

    sort_order: SortOrder
    """Order in which to sort the results."""

    payment_type: List[PaymentType]
    """Filter by payment type."""

    payment_status: List[PaymentStatus]
    """Filter by payment status."""

    payment_id: str
    """Filter by the payment's unique identifier."""

    external_id: str
    """Filter by your external identifier for the payment."""

    customer_id: str
    """Filter by the unique identifier of the customer."""

    paykey_id: str
    """Filter by the unique identifier of the paykey."""

    paykey: str
    """Filter by the paykey token."""

    min_amount: int
    """Filter to payments with an amount in cents greater than or equal to this value."""

    max_amount: int
    """Filter to payments with an amount in cents less than or equal to this value."""

    min_payment_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Filter to payments with a payment date on or after this date."""

    max_payment_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Filter to payments with a payment date on or before this date."""

    min_created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to payments created at or after this timestamp."""

    max_created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to payments created at or before this timestamp."""

    min_effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to payments effective at or after this timestamp."""

    max_effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to payments effective at or before this timestamp."""

    funding_id: str
    """Filter by the unique identifier of a funding event."""

    search_text: str
    """Free-text search across payment fields."""

    default_page_size: int
    """Default number of results returned per page."""

    default_sort: Literal["created_at", "payment_date", "effective_at", "id", "amount", "updated_at"]
    """Default field used to sort the results."""

    default_sort_order: SortOrder
    """Default order in which to sort the results."""

    status_reason: List[PaymentStatusReason]
    """Filter by the reason for the most recent payment status change."""

    status_source: List[PaymentStatusSource]
    """Filter by the source of the most recent payment status change."""

    include_metadata: bool
    """Whether to include metadata in each returned payment. Defaults to false."""

    is_refund: bool
    """Filter payouts by whether they refund an original charge."""

    has_refund: bool
    """Filter charges by whether an associated payout has refunded them."""

    is_resubmit: bool
    """Filter payments by whether they resubmit an original payment."""

    has_resubmit: bool
    """Filter payments by whether they have been resubmitted."""

    min_updated_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to payments last updated on or after this timestamp."""

    max_updated_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter to payments last updated on or before this timestamp."""

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

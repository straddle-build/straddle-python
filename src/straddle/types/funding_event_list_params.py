# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional, Union
from datetime import date
from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

from .sort_order import SortOrder
from .transfer_direction import TransferDirection
from .funding_event_type import FundingEventType
from .payment_status import PaymentStatus
from .payment_status_reason import PaymentStatusReason
from .payment_status_source import PaymentStatusSource

__all__ = ["FundingEventListParams"]


class FundingEventListParams(TypedDict, total=False):
    page_number: int
    """Results page number. Starts at page 1."""

    page_size: int
    """Results page size. Max value: 1000."""

    sort_by: Literal["transfer_date", "id", "amount"]
    """Field used to sort the results."""

    sort_order: SortOrder
    """Order in which to sort the results."""

    created_from: Annotated[Optional[Union[str, date]], PropertyInfo(format="iso8601")]
    """Filter to funding events created on or after this date."""

    created_to: Annotated[Optional[Union[str, date]], PropertyInfo(format="iso8601")]
    """Filter to funding events created on or before this date."""

    direction: TransferDirection
    """Filter by transfer direction relative to the linked bank account."""

    event_type: FundingEventType
    """Filter by funding event type."""

    trace_number: Optional[str]
    """Filter by a network trace number assigned during processing."""

    search_text: Optional[str]
    """Free-text search across funding event fields."""

    status: Optional[List[PaymentStatus]]
    """Filter by funding event status."""

    trace_id: Optional[str]
    """Filter by a network-level trace identifier assigned during processing."""

    status_reason: Optional[List[PaymentStatusReason]]
    """Filter by the reason for the most recent status change."""

    status_source: Optional[List[PaymentStatusSource]]
    """Filter by the source of the most recent status change."""

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

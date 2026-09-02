# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

from .paykey_status import PaykeyStatus
from .sort_order import SortOrder
from .paykey_source import PaykeySource

__all__ = ["PaykeyListParams"]


class PaykeyListParams(TypedDict, total=False):
    customer_id: str
    """Filter paykeys by related customer ID."""

    page_number: int
    """Page number for paginated results. Starts at 1."""

    page_size: int
    """Number of results per page. Maximum: 1000."""

    status: List[PaykeyStatus]
    """Filter paykeys by their current status."""

    sort_by: Literal["institution_name", "expires_at", "created_at"]
    """Field used to sort the results."""

    sort_order: SortOrder
    """Order in which to sort the results."""

    source: List[PaykeySource]
    """Filter paykeys by their source."""

    unblock_eligible: bool
    """Filters paykeys by unblock eligibility. `true` returns blocked paykeys that are eligible because of an `R29` return and have not been unblocked before. `false` returns blocked paykeys that are not eligible."""

    search_text: str
    """General search term to filter paykeys."""

    created_from: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start date for filtering by creation date."""

    created_to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End date for filtering by creation date."""

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

from .sort_order import SortOrder

__all__ = ["FundingEventListPaymentsParams"]


class FundingEventListPaymentsParams(TypedDict, total=False):
    page_number: int
    """Results page number. Starts at 1. Defaults to 1."""

    page_size: int
    """Number of results per page. Maximum 1,000. Defaults to 100."""

    include_metadata: bool
    """When `true`, includes each payment's metadata. Defaults to `false`."""

    default_page_size: int
    """Default number of results returned per page."""

    default_sort: Literal["created_at", "payment_date", "effective_at", "id"]
    """Default field used to sort the results."""

    default_sort_order: SortOrder
    """Default order in which to sort the results."""

    sort_by: Literal["created_at", "payment_date", "effective_at", "id"]
    """Field used to sort the results."""

    sort_order: SortOrder
    """Order in which to sort the results."""

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

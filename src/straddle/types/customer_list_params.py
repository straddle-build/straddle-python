# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

from .sort_order import SortOrder
from .customer_status import CustomerStatus
from .customer_type import CustomerType

__all__ = ["CustomerListParams"]


class CustomerListParams(TypedDict, total=False):
    page_number: int
    """Page number for paginated results. Starts at 1."""

    page_size: int
    """Number of results per page. Maximum: 1000."""

    sort_by: Literal["name", "created_at"]
    """Field used to sort the results."""

    sort_order: SortOrder
    """Order in which to sort the results."""

    created_from: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start date for filtering by `created_at` date."""

    created_to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End date for filtering by `created_at` date."""

    name: str
    """Filter customers by `name` (partial match)."""

    external_id: str
    """Filter by your system's `external_id`."""

    email: str
    """Filter customers by `email` address."""

    status: List[CustomerStatus]
    """Filter customers by their current `status`."""

    search_text: str
    """General search term to filter customers."""

    types: List[CustomerType]
    """Filter by customer type `individual` or `business`."""

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

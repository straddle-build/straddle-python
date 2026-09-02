# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountListParams"]


class AccountListParams(TypedDict, total=False):
    page_number: int
    """Page number. Defaults to `1`."""

    page_size: int
    """Number of results per page. Defaults to `100`. Maximum `1000`."""

    sort_by: str
    """Field used to sort results. Defaults to `id`."""

    sort_order: Literal["asc", "desc"]
    """Sort direction. Defaults to `asc`."""

    search_text: str
    """Text to search for across account fields."""

    status: Literal["created", "onboarding", "active", "rejected", "inactive"]
    """Account status to return."""

    type: Literal["business"]
    """Account type to return."""

    external_id: str
    """Your external ID for the account."""

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

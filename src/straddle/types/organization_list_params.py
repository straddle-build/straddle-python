# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrganizationListParams"]


class OrganizationListParams(TypedDict, total=False):
    name: str
    """Organization name. Supports partial matches."""

    external_id: str
    """Your external ID for the organization."""

    page_number: int
    """Page number. Defaults to `1`."""

    page_size: int
    """Number of results per page. Defaults to `100`. Maximum `1000`."""

    sort_by: str
    """Field used to sort results. Defaults to `id`."""

    sort_order: Literal["asc", "desc"]
    """Sort direction. Defaults to `asc`."""

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

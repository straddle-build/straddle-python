# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["LinkedBankAccountListParams"]


class LinkedBankAccountListParams(TypedDict, total=False):
    account_id: str
    """Account ID used to filter the results."""

    page_number: int
    """Page number. Defaults to `1`."""

    page_size: int
    """Number of results per page. Defaults to `100`. Maximum `1000`."""

    sort_by: str
    """Field used to sort results. Defaults to `id`."""

    sort_order: Literal["asc", "desc"]
    """Sort direction. Defaults to `asc`."""

    level: Literal["account", "platform"]
    """Scope of linked bank accounts to return."""

    purpose: Literal["charges", "payouts", "billing"]
    """Linked bank account purpose. Accepted values are `charges`, `payouts`, and `billing`."""

    status: Literal["created", "onboarding", "active", "rejected", "inactive", "canceled"]
    """Linked bank account status. Accepted values are `created`, `onboarding`, `active`, `rejected`, `inactive`, and `canceled`."""

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

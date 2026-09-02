# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["CapabilityRequestCreateParams", "Charges", "Payouts", "Internet"]


class CapabilityRequestCreateParams(TypedDict, total=False):
    charges: Charges
    """Requested charge capability and limits."""

    payouts: Payouts
    """Requested payout capability and limits."""

    internet: Internet
    """Request to enable or disable internet and mobile payment authorization."""

    individuals: Internet
    """Request to enable or disable payments from individuals."""

    businesses: Internet
    """Request to enable or disable payments from businesses."""

    signed_agreement: Internet
    """Request to enable or disable signed-agreement payment authorization."""

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Internet(TypedDict, total=False):
    enable: Required[bool]
    """Whether the request enables or disables the capability."""


class Payouts(TypedDict, total=False):
    enable: Required[bool]
    """Whether to enable or disable payouts for the account."""

    max_amount: Required[float]
    """Maximum amount in cents for one payout."""

    daily_amount: Required[float]
    """Daily payout amount limit in cents."""

    monthly_count: Required[int]
    """Maximum number of payouts per calendar month."""

    monthly_amount: Required[float]
    """Monthly payout amount limit in cents."""


class Charges(TypedDict, total=False):
    enable: Required[bool]
    """Whether to enable or disable charges for the account."""

    max_amount: Required[float]
    """Maximum amount in cents for one charge."""

    daily_amount: Required[float]
    """Daily charge amount limit in cents."""

    monthly_count: Required[int]
    """Maximum number of charges per calendar month."""

    monthly_amount: Required[float]
    """Monthly charge amount limit in cents."""

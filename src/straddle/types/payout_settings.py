# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PayoutSettings"]


class PayoutSettings(BaseModel):
    max_amount: int
    """Maximum amount in cents for one payout."""

    monthly_amount: int
    """Monthly payout amount limit in cents."""

    daily_amount: int
    """Daily payout amount limit in cents."""

    monthly_count: int
    """Maximum number of payouts per calendar month."""

    funding_time: Optional[str] = None
    """Funding schedule applied to payouts."""

    linked_bank_account_id: Optional[str] = None
    """ID of the linked bank account used for payout settlement."""

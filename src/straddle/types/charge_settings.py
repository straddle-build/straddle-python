# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ChargeSettings"]


class ChargeSettings(BaseModel):
    max_amount: int
    """Maximum amount in cents for one charge."""

    monthly_amount: int
    """Monthly charge amount limit in cents."""

    daily_amount: int
    """Daily charge amount limit in cents."""

    monthly_count: int
    """Maximum number of charges per calendar month."""

    funding_time: Optional[str] = None
    """Funding schedule applied to charges."""

    linked_bank_account_id: Optional[str] = None
    """ID of the linked bank account used for charge settlement."""

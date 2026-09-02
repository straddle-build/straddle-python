# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountChargeSettings"]


class AccountChargeSettings(BaseModel):
    max_amount: int
    """Maximum amount in cents for one charge."""

    monthly_amount: int
    """Monthly charge amount limit in cents."""

    daily_amount: int
    """Daily charge amount limit in cents."""

    monthly_count: int
    """Maximum number of charges per calendar month."""

    funding_time: Literal["immediate", "next_day", "one_day", "two_day", "three_day", "four_day", "five_day"]
    """Funding schedule for charges. Straddle sets this value."""

    linked_bank_account_id: str
    """ID of the linked bank account used for charge settlement. Straddle sets this value."""

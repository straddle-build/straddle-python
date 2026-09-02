# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountPaymentTypeSettings"]


class AccountPaymentTypeSettings(BaseModel):
    charges: Literal["active", "inactive"]
    """Status of charge support for the account."""

    payouts: Literal["active", "inactive"]
    """Status of payout support for the account."""

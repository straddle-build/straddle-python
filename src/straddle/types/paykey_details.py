# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PaykeyDetails"]


class PaykeyDetails(BaseModel):
    id: str
    """Unique identifier for the paykey."""

    customer_id: str
    """Unique identifier for the customer associated with the paykey."""

    label: str
    """Display label combining the bank name and masked account number."""

    balance: Optional[int] = None
    """The most recent available balance in the smallest currency unit, if a balance check was performed."""

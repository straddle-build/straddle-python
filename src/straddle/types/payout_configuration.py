# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

from .simulated_payment_outcome import SimulatedPaymentOutcome

__all__ = ["PayoutConfiguration"]


class PayoutConfiguration(BaseModel):
    sandbox_outcome: Optional[SimulatedPaymentOutcome] = None
    """Payment will simulate processing if not Standard."""

    auto_hold: Optional[bool] = None
    """Whether to place the payout on hold automatically after creation."""

    auto_hold_message: Optional[str] = None
    """Reason for placing the payout on hold automatically."""

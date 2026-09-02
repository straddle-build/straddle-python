# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .simulated_payment_outcome import SimulatedPaymentOutcome

__all__ = ["PayoutConfigurationParam"]


class PayoutConfigurationParam(TypedDict, total=False):
    sandbox_outcome: SimulatedPaymentOutcome
    """Payment will simulate processing if not Standard."""

    auto_hold: Optional[bool]
    """Whether to place the payout on hold automatically after creation."""

    auto_hold_message: Optional[str]
    """Reason for placing the payout on hold automatically."""

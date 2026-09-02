# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .balance_check_mode import BalanceCheckMode
from .simulated_payment_outcome import SimulatedPaymentOutcome

__all__ = ["ChargeConfigurationParam"]


class ChargeConfigurationParam(TypedDict, total=False):
    balance_check: Required[BalanceCheckMode]
    """Balance check mode to use before processing the charge."""

    sandbox_outcome: SimulatedPaymentOutcome
    """Payment will simulate processing if not Standard."""

    auto_hold: Optional[bool]
    """Whether to place the charge on hold automatically after creation."""

    auto_hold_message: Optional[str]
    """Reason for placing the charge on hold automatically."""

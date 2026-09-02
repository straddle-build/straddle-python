# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

from .balance_check_mode import BalanceCheckMode
from .simulated_payment_outcome import SimulatedPaymentOutcome

__all__ = ["ChargeConfiguration"]


class ChargeConfiguration(BaseModel):
    balance_check: BalanceCheckMode
    """Balance check mode to use before processing the charge."""

    sandbox_outcome: Optional[SimulatedPaymentOutcome] = None
    """Payment will simulate processing if not Standard."""

    auto_hold: Optional[bool] = None
    """Whether to place the charge on hold automatically after creation."""

    auto_hold_message: Optional[str] = None
    """Reason for placing the charge on hold automatically."""

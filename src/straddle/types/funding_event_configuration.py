# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

from .simulated_payment_outcome import SimulatedPaymentOutcome

__all__ = ["FundingEventConfiguration"]


class FundingEventConfiguration(BaseModel):
    sandbox_outcome: Optional[SimulatedPaymentOutcome] = None
    """Processing outcome configured for this simulated funding event."""

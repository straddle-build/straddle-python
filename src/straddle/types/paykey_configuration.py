# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

from .simulated_paykey_outcome import SimulatedPaykeyOutcome
from .paykey_processing_mode import PaykeyProcessingMode

__all__ = ["PaykeyConfiguration"]


class PaykeyConfiguration(BaseModel):
    sandbox_outcome: Optional[SimulatedPaykeyOutcome] = None

    processing_method: Optional[PaykeyProcessingMode] = None

# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

from .simulated_customer_outcome import SimulatedCustomerOutcome
from .paykey_processing_mode import PaykeyProcessingMode

__all__ = ["CustomerConfiguration"]


class CustomerConfiguration(BaseModel):
    sandbox_outcome: Optional[SimulatedCustomerOutcome] = None

    processing_method: Optional[PaykeyProcessingMode] = None

# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .simulated_customer_outcome import SimulatedCustomerOutcome
from .paykey_processing_mode import PaykeyProcessingMode

__all__ = ["CustomerConfigurationParam"]


class CustomerConfigurationParam(TypedDict, total=False):
    sandbox_outcome: SimulatedCustomerOutcome

    processing_method: PaykeyProcessingMode

# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .simulated_paykey_outcome import SimulatedPaykeyOutcome
from .paykey_processing_mode import PaykeyProcessingMode

__all__ = ["PaykeyConfigurationParam"]


class PaykeyConfigurationParam(TypedDict, total=False):
    sandbox_outcome: SimulatedPaykeyOutcome

    processing_method: PaykeyProcessingMode

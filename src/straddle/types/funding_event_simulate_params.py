# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

from .simulated_payment_outcome import SimulatedPaymentOutcome

__all__ = ["FundingEventSimulateParams"]


class FundingEventSimulateParams(TypedDict, total=False):
    funding_event_job_type: Required[Literal["charges", "payouts"]]
    """Required. Selects charge or payout activity for the simulated funding event."""

    sandbox_outcome: SimulatedPaymentOutcome
    """Optional. Sets the processing outcome for the simulated funding event. Defaults to `standard`."""

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

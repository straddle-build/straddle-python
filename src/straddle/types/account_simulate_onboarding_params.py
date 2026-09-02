# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountSimulateOnboardingParams"]


class AccountSimulateOnboardingParams(TypedDict, total=False):
    final_status: Literal["onboarding", "active"]
    """Final account status to produce in the sandbox simulation."""

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

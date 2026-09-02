# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

from .paykey_configuration_param import PaykeyConfigurationParam

__all__ = ["BridgeCreateTokenParams"]


class BridgeCreateTokenParams(TypedDict, total=False):
    customer_id: Required[str]
    """Unique identifier for the customer associated with the Bridge session."""

    config: PaykeyConfigurationParam

    external_id: Optional[str]
    """Unique identifier for the paykey in your system."""

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

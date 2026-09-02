# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

from .account_type import AccountType
from .paykey_configuration_param import PaykeyConfigurationParam

__all__ = ["BridgeCreateBankAccountPaykeyParams"]


class BridgeCreateBankAccountPaykeyParams(TypedDict, total=False):
    customer_id: Required[str]
    """Unique identifier for the customer associated with the paykey."""

    routing_number: Required[str]
    """Bank routing number."""

    account_number: Required[str]
    """Bank account number."""

    account_type: Required[AccountType]

    metadata: Optional[Dict[str, str]]
    """Up to 20 user-defined key-value pairs associated with the paykey."""

    config: PaykeyConfigurationParam

    external_id: Optional[str]
    """Unique identifier for the paykey in your system."""

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

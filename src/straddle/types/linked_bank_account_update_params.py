# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["LinkedBankAccountUpdateParams", "BankAccount"]


class LinkedBankAccountUpdateParams(TypedDict, total=False):
    bank_account: Required[BankAccount]

    metadata: Optional[Dict[str, Optional[str]]]
    """Up to 20 user-defined key-value pairs."""

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class BankAccount(TypedDict, total=False):
    account_holder: Required[str]
    """Account holder name as it appears on the bank account. This is usually the business's legal name."""

    routing_number: Required[str]
    """Nine-digit ABA routing number."""

    account_number: Required[str]
    """The bank account number."""

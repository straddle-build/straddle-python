# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["LinkedBankAccountCreateParams", "BankAccount"]


class LinkedBankAccountCreateParams(TypedDict, total=False):
    account_id: Optional[str]
    """ID of the account that will own the linked bank account. Omit this field to assign ownership to the platform in the authenticated request context."""

    bank_account: Required[BankAccount]

    metadata: Optional[Dict[str, Optional[str]]]
    """Up to 20 user-defined key-value pairs."""

    platform_id: Optional[str]
    """ID of the platform to associate with the linked bank account."""

    purposes: Optional[List[Literal["charges", "payouts", "billing"]]]
    """Payment purposes for the linked bank account. Defaults to `charges`, `payouts`, and `billing`."""

    description: Optional[str]
    """Your description for the linked bank account."""

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

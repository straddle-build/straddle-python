# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

from .linked_bank_account_status_detail import LinkedBankAccountStatusDetail
from .masked_linked_bank_account_details import MaskedLinkedBankAccountDetails

__all__ = ["LinkedBankAccount"]


class LinkedBankAccount(BaseModel):
    id: str
    """Straddle's unique ID for the linked bank account."""

    account_id: Optional[str] = None
    """ID of the related account, if this is an account-level linked bank account."""

    status: Literal["created", "onboarding", "active", "rejected", "inactive", "canceled"]
    """Status of the linked bank account."""

    status_detail: LinkedBankAccountStatusDetail

    bank_account: MaskedLinkedBankAccountDetails

    metadata: Optional[Dict[str, Optional[str]]] = None
    """Up to 20 user-defined key-value pairs."""

    created_at: datetime
    """Date and time when Straddle created the linked bank account."""

    updated_at: datetime
    """Date and time of the most recent linked bank account update."""

    platform_id: Optional[str] = None
    """ID of the related platform, if this is a platform-level linked bank account."""

    purposes: List[Literal["charges", "payouts", "billing"]]
    """Payment purposes assigned to the linked bank account."""

    description: Optional[str] = None
    """Your description for the linked bank account."""

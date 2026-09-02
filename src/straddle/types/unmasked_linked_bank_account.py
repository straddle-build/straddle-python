# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

from .linked_bank_account_status_detail import LinkedBankAccountStatusDetail
from .unmasked_linked_bank_account_details import UnmaskedLinkedBankAccountDetails

__all__ = ["UnmaskedLinkedBankAccount"]


class UnmaskedLinkedBankAccount(BaseModel):
    id: str
    """Straddle's unique ID for the linked bank account."""

    account_id: str
    """ID of the Straddle account associated with the linked bank account."""

    status: Literal["created", "onboarding", "active", "rejected", "inactive", "canceled"]
    """Status of the linked bank account."""

    status_detail: LinkedBankAccountStatusDetail
    """Details about the linked bank account's status."""

    bank_account: UnmaskedLinkedBankAccountDetails
    """Unmasked bank account details."""

    metadata: Optional[Dict[str, Optional[str]]] = None

    created_at: datetime
    """Date and time when Straddle created the linked bank account."""

    updated_at: datetime
    """Date and time of the most recent linked bank account update."""

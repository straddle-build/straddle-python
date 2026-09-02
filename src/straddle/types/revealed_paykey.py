# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

from .paykey_source import PaykeySource
from .paykey_status import PaykeyStatus
from .payment_status_details import PaymentStatusDetails
from .paykey_bank_details import PaykeyBankDetails
from .paykey_configuration import PaykeyConfiguration
from .paykey_balance_details import PaykeyBalanceDetails

__all__ = ["RevealedPaykey"]


class RevealedPaykey(BaseModel):
    id: str
    """Unique identifier for the paykey."""

    paykey: str
    """Full paykey value for creating payments. Store this value securely."""

    customer_id: Optional[str] = None
    """Unique identifier for the customer associated with the paykey."""

    label: str
    """Display label combining the bank name and masked account number."""

    source: PaykeySource

    institution_name: Optional[str] = None
    """Name of the financial institution."""

    status: PaykeyStatus

    status_details: Optional[PaymentStatusDetails] = None

    expires_at: Optional[datetime] = None
    """Expiration date and time of the paykey, if applicable."""

    created_at: datetime
    """Timestamp of when the paykey was created."""

    updated_at: datetime
    """Timestamp of the most recent update to the paykey."""

    bank_data: Optional[PaykeyBankDetails] = None

    metadata: Optional[Dict[str, str]] = None
    """Up to 20 user-defined key-value pairs associated with the paykey."""

    config: PaykeyConfiguration

    balance: Optional[PaykeyBalanceDetails] = None

    external_id: Optional[str] = None
    """Unique identifier for the paykey in your system."""

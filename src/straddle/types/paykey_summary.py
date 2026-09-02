# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

from .paykey_source import PaykeySource
from .paykey_status import PaykeyStatus
from .payment_status_details import PaymentStatusDetails
from .paykey_bank_details import PaykeyBankDetails
from .paykey_configuration import PaykeyConfiguration

__all__ = ["PaykeySummary"]


class PaykeySummary(BaseModel):
    id: str
    """Unique identifier for the paykey."""

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

    paykey: str
    """Masked paykey value."""

    config: PaykeyConfiguration

    external_id: Optional[str] = None
    """Unique identifier for the paykey in your system."""

    unblock_eligible: Optional[bool] = None
    """Whether the paykey is eligible for client-initiated unblocking. `true` only when the paykey is blocked by an `R29` return and has not been unblocked before. `false` for other blocked paykeys. `null` when the paykey is not blocked."""

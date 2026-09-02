# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional
from datetime import date, datetime

from .._models import BaseModel

from .transfer_direction import TransferDirection
from .funding_event_type import FundingEventType
from .payment_status import PaymentStatus
from .payment_status_details import PaymentStatusDetails

__all__ = ["FundingEventSummary"]


class FundingEventSummary(BaseModel):
    id: str
    """Unique identifier for this funding event."""

    amount: int
    """Total funding event amount in the smallest currency unit. For example, `1000` is $10.00 USD."""

    direction: TransferDirection
    """Transfer direction relative to the linked bank account. `deposit` moves funds into the account, and `withdrawal` moves funds out."""

    event_type: FundingEventType
    """Reason for the funding event. `charge_deposit` settles collected charges to the linked bank account. `charge_reversal` withdraws funds for reversed charges. `payout_withdrawal` withdraws funds for payouts. `payout_return` deposits returned payout funds."""

    trace_number: Optional[str] = None
    """The trace number of the funding event."""

    payment_count: int
    """Number of payments included in this funding event."""

    transfer_date: date
    """The date the funds transfer was initiated."""

    trace_numbers: List[str]
    """Network trace numbers associated with payments in this funding event."""

    created_at: datetime
    """Timestamp when this funding event was created."""

    updated_at: datetime
    """Timestamp when this funding event was last updated."""

    trace_ids: Dict[str, str]
    """Network-level trace identifiers assigned during processing. Keys vary by payment rail."""

    status: Optional[PaymentStatus] = None
    """Current status of this funding event."""

    status_details: Optional[PaymentStatusDetails] = None
    """Reason, source, and message for the most recent status change."""

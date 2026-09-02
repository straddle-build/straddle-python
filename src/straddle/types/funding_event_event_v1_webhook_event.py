# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

from .funding_event_transfer_direction import FundingEventTransferDirection
from .funding_event_type import FundingEventType
from .payment_status_source import PaymentStatusSource

__all__ = ["FundingEventEventV1WebhookEvent", "Data", "DataStatusDetails", "DataStatusHistory"]


class DataStatusHistory(BaseModel):
    reason: Literal[
        "insufficient_funds",
        "closed_bank_account",
        "invalid_bank_account",
        "invalid_routing",
        "disputed",
        "payment_stopped",
        "owner_deceased",
        "frozen_bank_account",
        "risk_review",
        "fraudulent",
        "duplicate_entry",
        "invalid_paykey",
        "payment_blocked",
        "amount_too_large",
        "too_many_attempts",
        "internal_system_error",
        "user_request",
        "ok",
        "other_network_return",
        "payout_refused",
        "validating",
        "auto_hold",
    ]

    source: PaymentStatusSource

    message: str
    """A human-readable description of the status."""

    code: Optional[str] = None
    """The status code if applicable."""

    changed_at: datetime
    """The time the status change occurred."""

    status: Literal["created", "scheduled", "failed", "cancelled", "on_hold", "pending", "paid", "reversed"]


class DataStatusDetails(BaseModel):
    message: str
    """A human-readable description of the current status."""

    reason: Literal[
        "insufficient_funds",
        "closed_bank_account",
        "invalid_bank_account",
        "invalid_routing",
        "disputed",
        "payment_stopped",
        "owner_deceased",
        "frozen_bank_account",
        "risk_review",
        "fraudulent",
        "duplicate_entry",
        "invalid_paykey",
        "payment_blocked",
        "amount_too_large",
        "too_many_attempts",
        "internal_system_error",
        "user_request",
        "ok",
        "other_network_return",
        "payout_refused",
        "validating",
        "auto_hold",
    ]

    source: PaymentStatusSource

    code: Optional[str] = None
    """The status code if applicable."""

    changed_at: datetime
    """The time the status change occurred."""


class Data(BaseModel):
    id: str
    """Unique identifier for this funding event."""

    amount: int
    """Total funding event amount in the smallest currency unit. For example, `1000` is $10.00 USD."""

    direction: FundingEventTransferDirection
    """Transfer direction relative to the linked bank account. `deposit` moves funds into the account, and `withdrawal` moves funds out."""

    event_type: FundingEventType
    """Reason for the funding event. `charge_deposit` settles collected charges to the linked bank account. `charge_reversal` withdraws funds for reversed charges. `payout_withdrawal` withdraws funds for payouts. `payout_return` deposits returned payout funds."""

    trace_ids: Dict[str, str]
    """Network-level trace identifiers assigned during processing. Keys vary by payment rail."""

    payment_count: int
    """Number of payments included in this funding event."""

    transfer_date: date
    """The date the funds transfer was initiated."""

    created_at: datetime
    """Timestamp when this funding event was created."""

    updated_at: datetime
    """Timestamp when this funding event was last updated."""

    status: Optional[
        Literal["created", "scheduled", "failed", "cancelled", "on_hold", "pending", "paid", "reversed"]
    ] = None
    """Current status of this funding event."""

    status_details: Optional[DataStatusDetails] = None
    """Reason, source, and message for the most recent status change."""

    status_history: List[DataStatusHistory]
    """Complete ordered history of all status changes for this funding event."""


class FundingEventEventV1WebhookEvent(BaseModel):
    event_type: str
    """Type of this event."""

    event_id: str
    """Unique identifier for this event."""

    account_id: str
    """Unique identifier for the account associated with this event."""

    data: Data

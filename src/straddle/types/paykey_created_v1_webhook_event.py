# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

from .paykey_source import PaykeySource
from .payment_status_source import PaymentStatusSource
from .account_type import AccountType
from .paykey_balance_refresh_status import PaykeyBalanceRefreshStatus

__all__ = ["PaykeyCreatedV1WebhookEvent", "Data", "DataStatusDetails", "DataBankData", "DataBalance"]


class DataBalance(BaseModel):
    account_balance: Optional[float] = None
    """Most recently retrieved account balance in dollars."""

    updated_at: Optional[datetime] = None
    """Timestamp of the most recent account balance update."""

    status: PaykeyBalanceRefreshStatus


class DataBankData(BaseModel):
    routing_number: str
    """Bank routing number."""

    account_number: str
    """Masked bank account number."""

    account_type: AccountType


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
    """Unique identifier for the paykey."""

    customer_id: Optional[str] = None
    """Unique identifier for the customer associated with the paykey."""

    label: str
    """Human-readable label for the paykey."""

    source: PaykeySource

    institution_name: Optional[str] = None
    """Name of the financial institution."""

    status: Literal["pending", "active", "inactive", "rejected", "review", "blocked"]

    status_details: Optional[DataStatusDetails] = None

    expires_at: Optional[datetime] = None
    """Expiration date and time of the paykey, if applicable."""

    created_at: datetime
    """Timestamp of when the paykey was created."""

    updated_at: datetime
    """Timestamp of the most recent update to the paykey."""

    paykey: str
    """Full paykey value for creating payments. Store this value securely."""

    bank_data: Optional[DataBankData] = None

    metadata: Optional[Dict[str, Optional[str]]] = None
    """Up to 20 user-defined key-value pairs associated with the paykey."""

    balance: Optional[DataBalance] = None


class PaykeyCreatedV1WebhookEvent(BaseModel):
    event_type: str
    """Type of this event."""

    event_id: str
    """Unique identifier for this event."""

    account_id: str
    """Unique identifier for the account associated with this event."""

    data: Data

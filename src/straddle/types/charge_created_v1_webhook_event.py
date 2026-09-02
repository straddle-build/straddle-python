# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

from .customer_type import CustomerType
from .masked_payment_device import MaskedPaymentDevice
from .balance_check_mode import BalanceCheckMode
from .payment_status_source import PaymentStatusSource
from .related_payment import RelatedPayment
from .payment_authorization_proof import PaymentAuthorizationProof

__all__ = [
    "ChargeCreatedV1WebhookEvent",
    "Data",
    "DataPaykeyDetails",
    "DataCustomerDetails",
    "DataConfig",
    "DataStatusDetails",
    "DataStatusHistory",
]


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


class DataConfig(BaseModel):
    balance_check: BalanceCheckMode


class DataCustomerDetails(BaseModel):
    id: str
    """Unique identifier for the customer."""

    name: str
    """Customer's full name or business name."""

    email: str
    """Customer's email address."""

    phone: str
    """Customer's phone number in E.164 format."""

    customer_type: CustomerType
    """Whether the customer is an individual or a business."""


class DataPaykeyDetails(BaseModel):
    id: str
    """Unique identifier for the paykey."""

    customer_id: str
    """Unique identifier for the customer associated with the paykey."""

    label: str
    """Display label combining the bank name and masked account number."""

    balance: Optional[int] = None
    """Available balance in cents when a balance check was performed. Null otherwise."""


class Data(BaseModel):
    id: str
    """Unique identifier for this charge."""

    paykey: str
    """The masked paykey token used for this charge."""

    description: Optional[str] = None
    """A human-readable description of the charge."""

    payment_rail: Optional[Literal["ach"]] = None

    paykey_details: Optional[DataPaykeyDetails] = None

    customer_details: Optional[DataCustomerDetails] = None

    amount: int
    """Amount in cents."""

    currency: str
    """Currency code. Only `USD` is supported."""

    payment_date: date
    """Date when Straddle submits the charge for processing."""

    consent_type: Literal["internet", "signed"]

    device: MaskedPaymentDevice

    external_id: Optional[str] = None
    """Your unique identifier for this charge, used to correlate with your internal records."""

    config: DataConfig

    created_at: Optional[datetime] = None
    """Timestamp when this charge was created."""

    updated_at: Optional[datetime] = None
    """Timestamp when this charge was last updated."""

    processed_at: Optional[datetime] = None
    """Timestamp when this charge was submitted to the payment network. Null until processed."""

    effective_at: Optional[datetime] = None
    """Timestamp when funds were settled. Null until settlement is confirmed."""

    status: Literal["created", "scheduled", "failed", "cancelled", "on_hold", "pending", "paid", "reversed"]

    status_details: DataStatusDetails

    status_history: List[DataStatusHistory]
    """Complete ordered history of all status changes for this charge."""

    metadata: Optional[Dict[str, Optional[str]]] = None
    """Key-value metadata stored with this charge."""

    funding_ids: List[str]
    """IDs of the funding events that included this charge."""

    related_payments: Optional[List[RelatedPayment]] = None
    """Related payments and their relationship to this charge."""

    is_resubmit: bool
    """Whether this charge resubmits an original charge."""

    has_resubmit: bool
    """Whether this charge has been resubmitted."""

    has_refund: bool
    """Whether an associated payout has refunded this charge."""

    documents: Optional[List[PaymentAuthorizationProof]] = None
    """Authorization documents for this charge, ordered by upload time."""


class ChargeCreatedV1WebhookEvent(BaseModel):
    event_type: str
    """Type of this event."""

    event_id: str
    """Unique identifier for this event."""

    account_id: str
    """Unique identifier for the account associated with this event."""

    data: Data

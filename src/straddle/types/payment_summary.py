# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional
from datetime import date, datetime

from .._models import BaseModel

from .payment_type import PaymentType
from .customer_details import CustomerDetails
from .paykey_details import PaykeyDetails
from .payment_status import PaymentStatus
from .payment_status_details import PaymentStatusDetails
from .related_payment import RelatedPayment

__all__ = ["PaymentSummary"]


class PaymentSummary(BaseModel):
    id: str
    """Unique identifier for this charge or payout."""

    payment_type: PaymentType
    """Whether this payment is a charge or payout."""

    payment_date: date
    """Date when Straddle submits the payment for processing."""

    effective_at: Optional[datetime] = None
    """Timestamp when funds settled. Null until settlement is confirmed."""

    description: Optional[str] = None
    """Human-readable description of the payment."""

    external_id: str
    """Your unique identifier for the charge or payout."""

    amount: int
    """Amount in cents."""

    currency: str
    """Currency code. Only `USD` is supported."""

    customer_details: Optional[CustomerDetails] = None
    """Information about the customer associated with the charge or payout."""

    paykey: str
    """Masked paykey token used for the charge or payout."""

    paykey_details: Optional[PaykeyDetails] = None
    """Details of the paykey used for the charge or payout."""

    status: PaymentStatus
    """Current status of the charge or payout."""

    status_details: PaymentStatusDetails
    """Reason, source, and message for the most recent status change."""

    funding_id: Optional[str] = None
    """Unique identifier for the funding event associated with the `charge` or `payout`."""

    created_at: datetime
    """Timestamp when the charge or payout was created."""

    updated_at: datetime
    """Timestamp when the charge or payout was last updated."""

    funding_ids: List[str]
    """IDs of the funding events that included this payment."""

    trace_ids: Dict[str, str]
    """Network-level trace identifiers assigned during processing. Keys vary by payment rail."""

    metadata: Optional[Dict[str, str]] = None
    """Key-value metadata for the payment. Included only when `include_metadata` is true."""

    related_payments: Optional[List[RelatedPayment]] = None
    """Related payments and their relationship to this charge or payout."""

    is_refund: bool
    """Whether this payment is a payout that refunds an original charge."""

    has_refund: bool
    """Whether this payment is a charge refunded by an associated payout."""

    is_resubmit: bool
    """Whether this payment resubmits an original payment."""

    has_resubmit: bool
    """Whether this payment has been resubmitted."""

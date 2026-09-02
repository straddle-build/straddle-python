# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional
from datetime import date, datetime

from .._models import BaseModel

from .payment_rail import PaymentRail
from .customer_details import CustomerDetails
from .paykey_details import PaykeyDetails
from .payment_device import PaymentDevice
from .payout_configuration import PayoutConfiguration
from .payment_status import PaymentStatus
from .payment_status_details import PaymentStatusDetails
from .payment_status_history import PaymentStatusHistory
from .related_payment import RelatedPayment
from .payment_authorization_proof import PaymentAuthorizationProof

__all__ = ["UnmaskedPayout"]


class UnmaskedPayout(BaseModel):
    id: str
    """Unique identifier for this payout."""

    description: Optional[str] = None
    """A human-readable description of the payout."""

    payment_rail: Optional[PaymentRail] = None
    """The payment rail used for the charge or payout."""

    customer_details: Optional[CustomerDetails] = None
    """Information about the customer associated with the charge or payout."""

    paykey_details: Optional[PaykeyDetails] = None

    amount: int
    """Amount in cents."""

    currency: str
    """Currency code. Only `USD` is supported."""

    payment_date: date
    """Date when Straddle submits the payout for processing."""

    device: PaymentDevice

    external_id: str
    """Your unique identifier for this payout, used to correlate with your internal records."""

    config: PayoutConfiguration

    created_at: Optional[datetime] = None
    """Timestamp when this payout was created."""

    updated_at: Optional[datetime] = None
    """Timestamp when this payout was last updated."""

    processed_at: Optional[datetime] = None
    """Timestamp when this payout was submitted to the payment network. Null until processed."""

    effective_at: Optional[datetime] = None
    """Timestamp when funds were settled. Null until settlement is confirmed."""

    status: PaymentStatus
    """The current status of the `charge` or `payout`."""

    status_details: PaymentStatusDetails

    status_history: List[PaymentStatusHistory]
    """Complete ordered history of all status changes for this payout."""

    metadata: Optional[Dict[str, str]] = None
    """Key-value metadata stored with this payout."""

    funding_ids: List[str]
    """IDs of the funding events that included this payout."""

    paykey: str
    """Unmasked paykey token used for this payout."""

    trace_ids: Dict[str, str]
    """Trace identifiers from the payment network. Keys depend on the payment rail."""

    related_payments: Optional[List[RelatedPayment]] = None
    """Related payments and their relationship to this payout."""

    is_refund: bool
    """Whether this payout refunds an original charge."""

    is_resubmit: bool
    """Whether this payout resubmits an original payout."""

    has_resubmit: bool
    """Whether this payout has been resubmitted."""

    documents: Optional[List[PaymentAuthorizationProof]] = None
    """Authorization documents for this payout, ordered by upload time."""

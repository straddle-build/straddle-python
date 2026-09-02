# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional
from datetime import date, datetime

from .._models import BaseModel

from .payment_rail import PaymentRail
from .paykey_details import PaykeyDetails
from .customer_details import CustomerDetails
from .consent_type import ConsentType
from .payment_device import PaymentDevice
from .charge_configuration import ChargeConfiguration
from .payment_status import PaymentStatus
from .payment_status_details import PaymentStatusDetails
from .payment_status_history import PaymentStatusHistory
from .related_payment import RelatedPayment
from .payment_authorization_proof import PaymentAuthorizationProof

__all__ = ["UnmaskedCharge"]


class UnmaskedCharge(BaseModel):
    id: str
    """Unique identifier for this charge."""

    description: Optional[str] = None
    """A human-readable description of the charge."""

    payment_rail: Optional[PaymentRail] = None
    """The payment rail used for the charge or payout."""

    paykey_details: Optional[PaykeyDetails] = None

    customer_details: Optional[CustomerDetails] = None
    """Information about the customer associated with the charge or payout."""

    amount: int
    """Amount in cents."""

    currency: str
    """Currency code. Only `USD` is supported."""

    payment_date: date
    """Date when Straddle submits the charge for processing."""

    consent_type: ConsentType
    """How the customer authorized the charge. `internet` covers online and mobile authorization. `signed` covers written or PDF-signed agreements."""

    device: PaymentDevice

    external_id: str
    """Your unique identifier for this charge, used to correlate with your internal records."""

    config: ChargeConfiguration

    created_at: datetime
    """Timestamp when this charge was created."""

    updated_at: datetime
    """Timestamp when this charge was last updated."""

    processed_at: Optional[datetime] = None
    """Timestamp when this charge was submitted to the payment network. Null until processed."""

    effective_at: Optional[datetime] = None
    """Timestamp when funds were settled. Null until settlement is confirmed."""

    status: PaymentStatus
    """The current status of the `charge` or `payout`."""

    status_details: PaymentStatusDetails

    status_history: List[PaymentStatusHistory]
    """Complete ordered history of all status changes for this charge."""

    metadata: Optional[Dict[str, str]] = None
    """Key-value metadata stored with this charge."""

    funding_ids: List[str]
    """IDs of the funding events that included this charge."""

    paykey: str
    """Unmasked paykey token used for this charge."""

    trace_ids: Dict[str, str]
    """Trace identifiers from the payment network. Keys depend on the payment rail."""

    related_payments: Optional[List[RelatedPayment]] = None
    """Related payments and their relationship to this charge."""

    has_refund: bool
    """Whether an associated payout has refunded this charge."""

    is_resubmit: bool
    """Whether this charge resubmits an original charge."""

    has_resubmit: bool
    """Whether this charge has been resubmitted."""

    documents: Optional[List[PaymentAuthorizationProof]] = None
    """Authorization documents for this charge, ordered by upload time."""

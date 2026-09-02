# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, Optional
from datetime import date

from .._models import BaseModel

from .payment_type import PaymentType
from .funding_event_payment_reason import FundingEventPaymentReason
from .customer_details import CustomerDetails
from .paykey_details import PaykeyDetails
from .payment_status import PaymentStatus

__all__ = ["FundingEventPayment"]


class FundingEventPayment(BaseModel):
    id: str
    """Unique identifier for this payment."""

    payment_type: PaymentType
    """Whether this payment is a charge or payout."""

    payment_date: date
    """The date on which this payment was submitted for processing."""

    currency: str
    """Three-letter ISO 4217 currency code."""

    funding_amount: int
    """Portion of the payment amount included in this funding event, in the smallest currency unit."""

    reason: FundingEventPaymentReason
    """Reason this payment was included in the funding event."""

    payment_amount: int
    """Total payment amount in the smallest currency unit (e.g. 1000 = $10.00 USD)."""

    customer_details: Optional[CustomerDetails] = None
    """Details of the customer associated with this payment."""

    paykey_details: Optional[PaykeyDetails] = None
    """Details of the paykey used for this payment."""

    status: PaymentStatus
    """Current status of this payment."""

    external_id: str
    """Your unique identifier for this payment, used to correlate with your internal records."""

    metadata: Optional[Dict[str, str]] = None
    """Key-value metadata for this payment. Included only when `include_metadata` is `true`."""

    trace_ids: Dict[str, str]
    """Network-level trace identifiers assigned during processing. Keys vary by payment rail."""

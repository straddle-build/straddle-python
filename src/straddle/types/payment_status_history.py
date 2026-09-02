# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

from .payment_status_reason import PaymentStatusReason
from .payment_status_source import PaymentStatusSource
from .payment_status import PaymentStatus

__all__ = ["PaymentStatusHistory"]


class PaymentStatusHistory(BaseModel):
    reason: PaymentStatusReason
    """Machine-readable reason for the status."""

    source: PaymentStatusSource
    """Source of the status change."""

    message: str
    """Human-readable status description."""

    code: Optional[str] = None
    """Status code, when available."""

    changed_at: datetime
    """Timestamp when the status changed."""

    status: PaymentStatus
    """The current status of the `charge` or `payout`."""

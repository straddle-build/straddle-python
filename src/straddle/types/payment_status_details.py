# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

from .payment_status_reason import PaymentStatusReason
from .payment_status_source import PaymentStatusSource

__all__ = ["PaymentStatusDetails"]


class PaymentStatusDetails(BaseModel):
    message: str
    """Human-readable status description."""

    reason: PaymentStatusReason
    """Machine-readable reason for the status."""

    source: PaymentStatusSource
    """Source of the status change."""

    changed_at: datetime
    """Timestamp when the status changed."""

    code: Optional[str] = None
    """Status code, when available."""

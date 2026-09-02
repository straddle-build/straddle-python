# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict
from datetime import datetime

from ..._models import BaseModel

from .paykey_verification_result import PaykeyVerificationResult
from .paykey_verification_breakdown import PaykeyVerificationBreakdown

__all__ = ["PaykeyVerificationDetails"]


class PaykeyVerificationDetails(BaseModel):
    id: str
    """Unique identifier for the verification details."""

    decision: PaykeyVerificationResult

    messages: Dict[str, str]
    """Messages returned by the paykey verification process."""

    breakdown: PaykeyVerificationBreakdown

    created_at: datetime
    """Timestamp of when the verification was initiated."""

    updated_at: datetime
    """Timestamp of the most recent update to the verification details."""

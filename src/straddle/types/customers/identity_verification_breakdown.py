# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

from .verification_decision import VerificationDecision
from .correlation_bucket import CorrelationBucket

__all__ = ["IdentityVerificationBreakdown"]


class IdentityVerificationBreakdown(BaseModel):
    decision: Optional[VerificationDecision] = None

    codes: Optional[List[str]] = None
    """List of specific result codes from the fraud and risk screening."""

    risk_score: Optional[float] = None
    """Predicts the inherent risk associated with the customer for a given module. A higher score indicates a greater likelihood of fraud."""

    correlation_score: Optional[float] = None
    """Represents the strength of the correlation between provided and known information. A higher score indicates a stronger correlation."""

    correlation: Optional[CorrelationBucket] = None

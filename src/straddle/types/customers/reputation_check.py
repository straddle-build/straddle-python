# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

from .verification_decision import VerificationDecision
from .reputation_insights import ReputationInsights

__all__ = ["ReputationCheck"]


class ReputationCheck(BaseModel):
    decision: Optional[VerificationDecision] = None

    codes: Optional[List[str]] = None
    """Specific codes related to the Straddle reputation screening results."""

    risk_score: Optional[float] = None
    """Risk score produced by the reputation check."""

    insights: Optional[ReputationInsights] = None

# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

from .verification_decision import VerificationDecision

__all__ = ["IdentityVerificationAlerts"]


class IdentityVerificationAlerts(BaseModel):
    decision: Optional[VerificationDecision] = None

    codes: Optional[List[str]] = None
    """List of specific result codes from the consortium alert screening."""

    alerts: Optional[List[str]] = None
    """Any alerts or flags raised during the consortium alert screening."""

# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

from .paykey_verification_result import PaykeyVerificationResult

__all__ = ["AccountNameMatchDetails"]


class AccountNameMatchDetails(BaseModel):
    names_on_account: Optional[List[str]] = None
    """Account-holder names returned by the financial institution."""

    matched_name: Optional[str] = None
    """Account-holder name that matched the customer record."""

    customer_name: Optional[str] = None
    """Customer name evaluated during account verification."""

    correlation_score: Optional[float] = None
    """Strength of the match between the customer name and account-holder names."""

    decision: PaykeyVerificationResult

    reason: Optional[str] = None
    """Reason for the name-match decision."""

    codes: List[str]
    """Result codes returned by the name-match check."""

# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

from .paykey_verification_result import PaykeyVerificationResult

__all__ = ["AccountValidationDetails"]


class AccountValidationDetails(BaseModel):
    decision: PaykeyVerificationResult

    reason: Optional[str] = None
    """Reason for the account-validation decision."""

    codes: List[str]
    """Result codes returned by the account-validation check."""

# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel

from .verification_decision import VerificationDecision
from .identity_verification_alerts import IdentityVerificationAlerts
from .identity_verification_watchlist import IdentityVerificationWatchlist
from .customer_kyc_verification import CustomerKYCVerification
from .reputation_check import ReputationCheck
from .identity_verification_breakdown import IdentityVerificationBreakdown

__all__ = ["CustomerIdentityVerification", "Breakdown"]


class Breakdown(BaseModel):
    address: Optional[IdentityVerificationBreakdown] = None

    email: Optional[IdentityVerificationBreakdown] = None

    fraud: Optional[IdentityVerificationBreakdown] = None

    phone: Optional[IdentityVerificationBreakdown] = None

    synthetic: Optional[IdentityVerificationBreakdown] = None

    business_identification: Optional[IdentityVerificationBreakdown] = None

    business_validation: Optional[IdentityVerificationBreakdown] = None

    business_evaluation: Optional[IdentityVerificationBreakdown] = None


class CustomerIdentityVerification(BaseModel):
    review_id: str
    """Unique identifier for the review."""

    decision: VerificationDecision

    messages: Optional[Dict[str, str]] = None
    """Messages returned by the customer verification process."""

    breakdown: Breakdown
    """Results for each customer verification check, including decisions, risk scores, and correlation scores."""

    network_alerts: Optional[IdentityVerificationAlerts] = None

    watch_list: Optional[IdentityVerificationWatchlist] = None

    kyc: Optional[CustomerKYCVerification] = None

    created_at: datetime
    """Timestamp of when the review was initiated."""

    updated_at: datetime
    """Timestamp of the most recent update to the review."""

    reputation: Optional[ReputationCheck] = None

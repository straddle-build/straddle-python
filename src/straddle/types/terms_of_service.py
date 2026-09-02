# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TermsOfService"]


class TermsOfService(BaseModel):
    accepted_date: datetime
    """Date and time when the account accepted the Terms of Service."""

    accepted_ip: Optional[str] = None
    """IP address used to accept the Terms of Service."""

    accepted_user_agent: Optional[str] = None
    """User agent of the browser or application that accepted the Terms of Service."""

    agreement_url: Optional[str] = None
    """URL of the accepted agreement."""

    agreement_type: Literal["embedded", "direct"]
    """Agreement type. Use `embedded` unless Straddle has enabled the platform for `direct` agreements."""

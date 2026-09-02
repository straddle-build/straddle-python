# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

from .representative_status_detail import RepresentativeStatusDetail
from .representative_relationship import RepresentativeRelationship

__all__ = ["UnmaskedRepresentative"]


class UnmaskedRepresentative(BaseModel):
    id: str
    """Straddle's unique ID for the representative."""

    account_id: str
    """ID of the account associated with the representative."""

    user_id: Optional[str] = None
    """ID of the Straddle user linked to the representative, if any."""

    status: Literal["created", "onboarding", "active", "rejected", "inactive"]
    """Status of the representative."""

    status_detail: RepresentativeStatusDetail

    first_name: str
    """Representative's first name."""

    last_name: str
    """Representative's last name."""

    dob: date
    """Representative's date of birth in `YYYY-MM-DD` format."""

    email: str
    """Representative's email address."""

    mobile_number: str
    """Representative's mobile phone number."""

    relationship: RepresentativeRelationship

    external_id: Optional[str] = None
    """Your unique ID for the representative."""

    created_at: datetime
    """Date and time when Straddle created the representative."""

    updated_at: datetime
    """Date and time of the most recent representative update."""

    ssn_last4: str
    """Last four digits of the representative's Social Security number."""

    metadata: Optional[Dict[str, str]] = None
    """Up to 20 user-defined key-value pairs."""

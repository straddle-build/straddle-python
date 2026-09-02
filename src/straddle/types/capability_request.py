# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CapabilityRequest"]


class CapabilityRequest(BaseModel):
    id: str
    """Straddle's unique ID for the capability request."""

    account_id: str
    """ID of the account associated with the capability request."""

    type: Literal["charges", "payouts", "individuals", "businesses", "signed_agreement", "internet"]
    """Capability type requested within the category."""

    category: Literal["payment_type", "customer_type", "consent_type"]
    """Groups the requested capability. `payment_type` covers `charges` and `payouts`. `customer_type` covers `individuals` and `businesses`. `consent_type` covers `signed_agreement` and `internet` authorization."""

    settings: Optional[Dict[str, object]] = None
    """Limits and other settings requested for the capability."""

    status: Literal["active", "inactive", "in_review", "rejected", "approved", "reviewing"]
    """Status of the capability request."""

    created_at: datetime
    """Date and time when Straddle created the capability request."""

    updated_at: datetime
    """Date and time of the most recent capability request update."""

    enable: bool
    """Whether the request enables or disables the capability."""

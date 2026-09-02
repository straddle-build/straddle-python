# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

from .account_status_detail import AccountStatusDetail
from .account_business_profile import AccountBusinessProfile
from .account_capabilities import AccountCapabilities
from .account_payment_settings import AccountPaymentSettings
from .terms_of_service import TermsOfService

__all__ = ["Account"]


class Account(BaseModel):
    id: str
    """Straddle's unique ID for the account."""

    organization_id: str
    """ID of the organization that owns the account."""

    type: Literal["business"]
    """The account type. Only `business` is supported."""

    status: Literal["created", "onboarding", "active", "rejected", "inactive"]
    """The current lifecycle status of the account."""

    status_detail: AccountStatusDetail

    business_profile: Optional[AccountBusinessProfile] = None

    capabilities: Optional[AccountCapabilities] = None

    settings: Optional[AccountPaymentSettings] = None

    terms_of_service: Optional[TermsOfService] = None

    metadata: Optional[Dict[str, Optional[str]]] = None
    """Up to 20 user-defined key-value pairs."""

    access_level: Literal["standard", "managed"]
    """The account access level. `standard` provides normal account access, including access to the Straddle dashboard. `managed` means the platform manages the account and account users cannot access the Straddle dashboard."""

    external_id: Optional[str] = None
    """Your unique ID for the account."""

    created_at: Optional[datetime] = None
    """Date and time when Straddle created the account."""

    updated_at: Optional[datetime] = None
    """Date and time of the most recent account update."""

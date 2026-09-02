# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

from .account_capability import AccountCapability

__all__ = ["AccountConsentCapabilities"]


class AccountConsentCapabilities(BaseModel):
    signed_agreement: AccountCapability
    """Signed-agreement payment authorization capability for the account."""

    internet: AccountCapability
    """Internet payment authorization capability for the account."""

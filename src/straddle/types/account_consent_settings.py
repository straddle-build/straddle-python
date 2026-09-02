# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountConsentSettings"]


class AccountConsentSettings(BaseModel):
    internet: Literal["active", "inactive"]
    """Status of internet authorization support for the account."""

    signed_agreement: Literal["active", "inactive"]
    """Status of signed-agreement authorization support for the account."""

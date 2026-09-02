# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["AccountPolicyControls"]


class AccountPolicyControls(BaseModel):
    allow_data_unmask: bool
    """Whether the account can retrieve unmasked sensitive fields."""

    allow_duplicate_email: bool
    """Whether multiple customers can share one email address."""

    allow_customer_identity_skip: bool
    """Whether customer identity verification can be skipped."""

    allow_paykey_verification_skip: bool
    """Whether paykey verification can be skipped."""

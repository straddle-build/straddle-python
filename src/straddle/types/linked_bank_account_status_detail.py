# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LinkedBankAccountStatusDetail"]


class LinkedBankAccountStatusDetail(BaseModel):
    reason: Literal["unverified", "in_review", "pending", "stuck", "verified", "failed_verification", "disabled", "new"]
    """Machine-readable reason for the linked bank account's status."""

    source: Literal["watchtower"]
    """System that produced the linked bank account status detail."""

    code: str
    """Machine-readable status code from the source."""

    message: str
    """Human-readable description of the linked bank account's status."""

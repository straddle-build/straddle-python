# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountStatusDetail"]


class AccountStatusDetail(BaseModel):
    reason: Literal[
        "unverified",
        "in_review",
        "pending",
        "stuck",
        "verified",
        "failed_verification",
        "disabled",
        "terminated",
        "new",
    ]
    """Machine-readable reason for the account's status."""

    source: Literal["watchtower"]
    """System that produced the account status detail."""

    code: str
    """Machine-readable status code from the source."""

    message: str
    """Human-readable description of the account's status."""

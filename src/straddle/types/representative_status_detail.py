# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RepresentativeStatusDetail"]


class RepresentativeStatusDetail(BaseModel):
    reason: Literal["unverified", "in_review", "pending", "stuck", "verified", "failed_verification", "disabled", "new"]
    """Machine-readable reason for the representative's status."""

    source: Literal["watchtower"]
    """System that produced the representative status detail."""

    code: str
    """Machine-readable status code from the source."""

    message: str
    """Human-readable description of the representative's status."""

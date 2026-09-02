# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["BusinessCustomerRepresentativeParam"]


class BusinessCustomerRepresentativeParam(TypedDict, total=False):
    name: Required[str]
    """Full name of the representative."""

    email: Optional[str]
    """Email address of the representative."""

    phone: Optional[str]
    """Phone number of the representative."""

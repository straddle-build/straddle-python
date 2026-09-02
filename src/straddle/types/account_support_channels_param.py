# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AccountSupportChannelsParam"]


class AccountSupportChannelsParam(TypedDict, total=False):
    email: Optional[str]
    """Email address for customer support."""

    phone: Optional[str]
    """Customer support phone number in E.164 format."""

    url: Optional[str]
    """URL of the business's customer support page or contact form."""

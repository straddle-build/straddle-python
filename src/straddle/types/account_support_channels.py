# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AccountSupportChannels"]


class AccountSupportChannels(BaseModel):
    email: Optional[str] = None
    """Email address for customer support."""

    phone: Optional[str] = None
    """Customer support phone number in E.164 format."""

    url: Optional[str] = None
    """URL of the business's customer support page or contact form."""

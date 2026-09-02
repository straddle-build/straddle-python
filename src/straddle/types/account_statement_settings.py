# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AccountStatementSettings"]


class AccountStatementSettings(BaseModel):
    company_name: Optional[str] = None
    """Company name used in statement records."""

    company_id: Optional[str] = None
    """Company identifier used in ACH records."""

    default_descriptor: Optional[str] = None
    """Default descriptor for account payments."""

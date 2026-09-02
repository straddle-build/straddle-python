# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AccountIndustry"]


class AccountIndustry(BaseModel):
    mcc: Optional[str] = None
    """Merchant category code (MCC) that best describes the business. If omitted, provide both `sector` and `category`."""

    sector: Optional[str] = None
    """Business sector. Required when `mcc` is omitted."""

    category: Optional[str] = None
    """Industry category. Required when `mcc` is omitted."""

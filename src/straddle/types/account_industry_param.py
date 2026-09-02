# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AccountIndustryParam"]


class AccountIndustryParam(TypedDict, total=False):
    mcc: Optional[str]
    """Merchant category code (MCC) that best describes the business. If omitted, provide both `sector` and `category`."""

    sector: Optional[str]
    """Business sector. Required when `mcc` is omitted."""

    category: Optional[str]
    """Industry category. Required when `mcc` is omitted."""

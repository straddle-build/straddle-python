# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AccountAddressParam"]


class AccountAddressParam(TypedDict, total=False):
    line1: Required[Optional[str]]
    """Primary address line, such as a street address or PO Box."""

    line2: Optional[str]
    """Secondary address line, such as an apartment, suite, unit, or building."""

    city: Required[Optional[str]]
    """City, district, suburb, town, or village."""

    state: Required[Optional[str]]
    """Two-letter state code."""

    postal_code: Required[Optional[str]]
    """Postal or ZIP code."""

    country: Optional[str]
    """Two-letter ISO 3166-1 country code. If omitted, Straddle applies US address validation."""

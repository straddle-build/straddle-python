# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AccountAddress"]


class AccountAddress(BaseModel):
    """Optional business address. If provided, `line1`, `city`, `state`, and `postal_code` are required."""

    line1: Optional[str] = None
    """Primary address line, such as a street address or PO Box."""

    line2: Optional[str] = None
    """Secondary address line, such as an apartment, suite, unit, or building."""

    city: Optional[str] = None
    """City, district, suburb, town, or village."""

    state: Optional[str] = None
    """Two-letter state code."""

    postal_code: Optional[str] = None
    """Postal or ZIP code."""

    country: Optional[str] = None
    """Two-letter ISO 3166-1 country code. If omitted, Straddle applies US address validation."""

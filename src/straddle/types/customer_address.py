# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CustomerAddress"]


class CustomerAddress(BaseModel):
    """Customer postal address. When provided, the object must include all required fields."""

    address1: str
    """Primary address line, such as a street address or PO Box."""

    address2: Optional[str] = None
    """Secondary address line, such as an apartment, suite, unit, or building."""

    city: str
    """City, district, suburb, town, or village."""

    state: str
    """Two-letter state code."""

    zip: str
    """ZIP or postal code."""

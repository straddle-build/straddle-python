# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CustomerAddressParam"]


class CustomerAddressParam(TypedDict, total=False):
    address1: Required[str]
    """Primary address line, such as a street address or PO Box."""

    address2: Optional[str]
    """Secondary address line, such as an apartment, suite, unit, or building."""

    city: Required[str]
    """City, district, suburb, town, or village."""

    state: Required[str]
    """Two-letter state code."""

    zip: Required[str]
    """ZIP or postal code."""

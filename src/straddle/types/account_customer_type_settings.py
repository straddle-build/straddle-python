# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountCustomerTypeSettings"]


class AccountCustomerTypeSettings(BaseModel):
    individuals: Literal["active", "inactive"]
    """Status of individual-customer support for the account."""

    businesses: Literal["active", "inactive"]
    """Status of business-customer support for the account."""

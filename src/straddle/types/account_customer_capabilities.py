# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

from .account_capability import AccountCapability

__all__ = ["AccountCustomerCapabilities"]


class AccountCustomerCapabilities(BaseModel):
    individuals: AccountCapability

    businesses: AccountCapability

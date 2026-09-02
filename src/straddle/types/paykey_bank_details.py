# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

from .account_type import AccountType

__all__ = ["PaykeyBankDetails"]


class PaykeyBankDetails(BaseModel):
    routing_number: str
    """Bank routing number."""

    account_number: str
    """Masked bank account number."""

    account_type: AccountType

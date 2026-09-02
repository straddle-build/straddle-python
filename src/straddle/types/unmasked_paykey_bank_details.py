# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

from .account_type import AccountType

__all__ = ["UnmaskedPaykeyBankDetails"]


class UnmaskedPaykeyBankDetails(BaseModel):
    routing_number: str
    """Bank routing number."""

    account_number: str
    """Bank account number."""

    account_type: AccountType

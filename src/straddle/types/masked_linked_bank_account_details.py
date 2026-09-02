# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["MaskedLinkedBankAccountDetails"]


class MaskedLinkedBankAccountDetails(BaseModel):
    institution_name: str
    """Name of the financial institution."""

    account_holder: str
    """Name of the account holder as it appears on the bank account."""

    routing_number: str
    """Nine-digit ABA routing number for the bank account."""

    account_mask: str
    """Last four digits of the bank account number."""

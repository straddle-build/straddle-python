# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["MaskedCustomerDevice"]


class MaskedCustomerDevice(BaseModel):
    ip_address: str
    """Masked IP address of the customer's device at the time of profile creation."""

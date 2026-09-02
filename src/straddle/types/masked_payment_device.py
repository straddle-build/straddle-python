# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["MaskedPaymentDevice"]


class MaskedPaymentDevice(BaseModel):
    ip_address: str
    """Masked IP address of the device used when the customer authorized the charge or payout."""

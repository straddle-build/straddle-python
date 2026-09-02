# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["CustomerDevice"]


class CustomerDevice(BaseModel):
    ip_address: str
    """Customer IP address at profile creation. `0.0.0.0` represents an offline registration."""

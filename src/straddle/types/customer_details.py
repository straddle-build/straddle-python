# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

from .customer_type import CustomerType

__all__ = ["CustomerDetails"]


class CustomerDetails(BaseModel):
    """Information about the customer associated with the charge or payout."""

    id: str
    """Unique identifier for the customer."""

    name: str
    """Customer's full name or business name."""

    customer_type: CustomerType
    """Whether the customer is an individual or a business."""

    email: str
    """Customer's email address."""

    phone: str
    """Customer's phone number in E.164 format."""

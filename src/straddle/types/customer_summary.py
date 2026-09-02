# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

from .customer_type import CustomerType
from .customer_status import CustomerStatus

__all__ = ["CustomerSummary"]


class CustomerSummary(BaseModel):
    id: str
    """Unique identifier for the customer."""

    name: str
    """Full name for an individual customer or business name for a business customer."""

    type: CustomerType

    email: str
    """The customer's email address."""

    phone: str
    """The customer's phone number in E.164 format."""

    external_id: Optional[str] = None
    """Unique identifier for the customer in your system."""

    status: CustomerStatus

    created_at: datetime
    """Timestamp of when the customer record was created."""

    updated_at: datetime
    """Timestamp of the most recent update to the customer record."""

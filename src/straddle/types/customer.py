# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

from .customer_type import CustomerType
from .customer_status import CustomerStatus
from .compliance_profile import ComplianceProfile
from .masked_customer_device import MaskedCustomerDevice
from .customer_configuration import CustomerConfiguration
from .customer_address import CustomerAddress

__all__ = ["Customer"]


class Customer(BaseModel):
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

    address: Optional[CustomerAddress] = None
    """Customer postal address. When provided, the object must include all required fields."""

    compliance_profile: Optional[ComplianceProfile] = None

    device: Optional[MaskedCustomerDevice] = None

    metadata: Optional[Dict[str, str]] = None
    """Up to 20 user-defined key-value pairs associated with the customer."""

    config: Optional[CustomerConfiguration] = None

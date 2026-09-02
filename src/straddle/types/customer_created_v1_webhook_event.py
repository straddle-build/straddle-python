# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

from .masked_customer_device import MaskedCustomerDevice
from .customer_type import CustomerType

__all__ = ["CustomerCreatedV1WebhookEvent", "Data", "DataAddress", "DataComplianceProfile"]


class DataComplianceProfile(BaseModel):
    dob: Optional[str] = None
    """Masked date of birth for an individual customer in `****-**-**` format."""

    ssn: Optional[str] = None
    """Masked Social Security number for an individual customer in `***-**-****` format."""

    ein: Optional[str] = None
    """Masked Employer Identification Number for a business customer in `**-*******` format."""

    legal_business_name: Optional[str] = None
    """Official registered name of the business customer."""

    website: Optional[str] = None
    """Official website URL for the business customer."""


class DataAddress(BaseModel):
    address1: str
    """Primary address line, such as a street address or PO Box."""

    address2: Optional[str] = None
    """Secondary address line, such as an apartment, suite, unit, or building."""

    city: str
    """City, district, suburb, town, or village."""

    state: str
    """Two-letter state code."""

    zip: str
    """ZIP or postal code."""


class Data(BaseModel):
    id: str
    """Unique identifier for the customer."""

    address: Optional[DataAddress] = None

    compliance_profile: Optional[DataComplianceProfile] = None

    device: MaskedCustomerDevice

    name: str
    """Full name for an individual customer or business name for a business customer."""

    type: CustomerType

    email: str
    """Customer email address."""

    phone: str
    """Customer phone number in E.164 format."""

    external_id: Optional[str] = None
    """Unique identifier for the customer in your system."""

    status: Literal["pending", "review", "verified", "inactive", "rejected"]

    created_at: datetime
    """Timestamp of when the customer record was created."""

    updated_at: datetime
    """Timestamp of the most recent update to the customer record."""

    metadata: Optional[Dict[str, Optional[str]]] = None
    """Up to 20 user-defined key-value pairs associated with the customer."""


class CustomerCreatedV1WebhookEvent(BaseModel):
    event_type: str
    """Type of this event."""

    event_id: str
    """Unique identifier for this event."""

    account_id: str
    """Unique identifier for the account associated with this event."""

    data: Data

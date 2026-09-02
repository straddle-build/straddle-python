# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "PlatformEventV1WebhookEvent",
    "Data",
    "DataStatusDetail",
    "DataBusinessProfile",
    "DataBusinessProfileAddress",
    "DataBusinessProfileIndustry",
    "DataBusinessProfileSupportChannels",
]


class DataBusinessProfileSupportChannels(BaseModel):
    email: Optional[str] = None
    """Customer support email address."""

    phone: Optional[str] = None
    """Customer support phone number."""

    url: Optional[str] = None
    """URL of the customer support page or contact form."""


class DataBusinessProfileIndustry(BaseModel):
    mcc: Optional[str] = None
    """Merchant Category Code assigned to the business."""

    sector: Optional[str] = None
    """Industry sector of the business."""

    category: Optional[str] = None
    """Industry category of the business."""


class DataBusinessProfileAddress(BaseModel):
    line1: Optional[str] = None
    """Primary street address."""

    line2: Optional[str] = None
    """Additional address information, such as a suite or unit."""

    city: Optional[str] = None
    """City for the address."""

    state: Optional[str] = None
    """State or region for the address."""

    postal_code: Optional[str] = None
    """Postal code for the address."""

    country: Optional[str] = None
    """Two-letter ISO 3166-1 country code."""


class DataBusinessProfile(BaseModel):
    name: str
    """Display name of the business."""

    website: str
    """URL of the business website."""

    legal_name: Optional[str] = None
    """Registered legal name of the business."""

    description: Optional[str] = None
    """Description of the business."""

    use_case: Optional[str] = None
    """Description of how the business uses Straddle."""

    tax_id: Optional[str] = None
    """Tax identification number of the business."""

    phone: Optional[str] = None
    """Primary phone number for the business."""

    address: Optional[DataBusinessProfileAddress] = None

    industry: Optional[DataBusinessProfileIndustry] = None

    support_channels: Optional[DataBusinessProfileSupportChannels] = None


class DataStatusDetail(BaseModel):
    reason: Literal[
        "unverified",
        "new",
        "in_review",
        "pending",
        "stuck",
        "verified",
        "failed_verification",
        "disabled",
        "terminated",
    ]
    """Machine-readable reason for the current platform status."""

    source: Literal["watchtower"]
    """Source that produced the current platform status."""

    code: str
    """Machine-readable code for the current platform status."""

    message: str
    """Human-readable explanation of the current platform status."""


class Data(BaseModel):
    id: str
    """Unique identifier for the platform."""

    status: Literal["created", "onboarding", "active", "rejected", "inactive"]
    """Current lifecycle status of the platform."""

    status_detail: DataStatusDetail

    business_profile: Optional[DataBusinessProfile] = None

    metadata: Optional[Dict[str, Optional[str]]] = None
    """Key-value metadata associated with the platform."""

    external_id: Optional[str] = None
    """Your unique identifier for the platform."""

    created_at: Optional[datetime] = None
    """Timestamp when the platform was created."""

    updated_at: Optional[datetime] = None
    """Timestamp when the platform was last updated."""


class PlatformEventV1WebhookEvent(BaseModel):
    event_type: str
    """Type of this event."""

    event_id: str
    """Unique identifier for this event."""

    account_id: str
    """Unique identifier for the account associated with this event."""

    data: Data

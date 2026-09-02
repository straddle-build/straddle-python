# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UserCreatedV1WebhookEvent", "Data", "DataMembership"]


class DataMembership(BaseModel):
    level: Literal["none", "onboarding", "account", "organization", "platform", "straddle"]
    """Entity level at which the membership applies."""

    entity_id: Optional[str] = None
    """Unique identifier of the entity associated with the membership."""

    entity_name: str
    """Display name of the entity associated with the membership."""

    roles: List[Literal["none", "member", "developer", "admin"]]
    """Roles granted by the membership."""

    authenticator_organization_id: str
    """Organization identifier used by the authentication provider."""


class Data(BaseModel):
    id: str
    """The unique identifier of the user."""

    organization_id: Optional[str] = None
    """The unique identifier of the organization this user belongs to."""

    platform_id: Optional[str] = None
    """The unique identifier of the organization this user belongs to."""

    authenticator_id: Optional[str] = None
    """The unique identifier used for authentication purposes."""

    status: Literal["invited", "active", "onboarding", "inactive"]
    """The current status of the user."""

    first_name: str
    """The first name of the user."""

    last_name: str
    """The last name of the user."""

    email: str
    """The email address of the user."""

    level: Literal["none", "onboarding", "straddle", "platform", "organization"]
    """The current status of the user."""

    roles: List[Literal["none", "member", "developer", "admin"]]
    """The role assigned to the user, determining their permissions within the system."""

    created_at: datetime
    """Timestamp of when the user was created."""

    updated_at: datetime
    """Timestamp of the most recent update to the user."""

    memberships: List[DataMembership]
    """Memberships that grant the user access to Straddle entities."""


class UserCreatedV1WebhookEvent(BaseModel):
    event_type: str
    """Type of this event."""

    event_id: str
    """Unique identifier for this event."""

    account_id: str
    """Unique identifier for the account associated with this event."""

    data: Data

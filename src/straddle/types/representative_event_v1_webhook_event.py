# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

from .representative import Representative

__all__ = ["RepresentativeEventV1WebhookEvent"]


class RepresentativeEventV1WebhookEvent(BaseModel):
    event_type: str
    """Type of this event."""

    event_id: str
    """Unique identifier for this event."""

    account_id: str
    """Unique identifier for the account associated with this event."""

    data: Representative

# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

from .account import Account

__all__ = ["AccountEventV1WebhookEvent"]


class AccountEventV1WebhookEvent(BaseModel):
    event_type: str
    """Type of this event."""

    event_id: str
    """Unique identifier for this event."""

    account_id: str
    """Unique identifier for the account associated with this event."""

    data: Account

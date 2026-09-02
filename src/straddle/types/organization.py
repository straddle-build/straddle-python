# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Organization"]


class Organization(BaseModel):
    id: str
    """Straddle's unique ID for the organization."""

    name: str
    """The name of the organization."""

    external_id: Optional[str] = None
    """Your unique ID for the organization."""

    metadata: Optional[Dict[str, Optional[str]]] = None
    """Up to 20 user-defined key-value pairs."""

    created_at: datetime
    """Date and time when Straddle created the organization."""

    updated_at: datetime
    """Date and time of the most recent organization update."""

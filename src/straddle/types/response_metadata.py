# File generated from our OpenAPI spec by Scalar. See README.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["ResponseMetadata"]


class ResponseMetadata(BaseModel):
    """Metadata for an API request."""

    api_request_id: str
    """Unique identifier for the API request."""

    api_request_timestamp: datetime
    """UTC timestamp for the API request."""

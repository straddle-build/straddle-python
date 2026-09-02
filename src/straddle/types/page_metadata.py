# File generated from our OpenAPI spec by Scalar. See README.md for details.

from datetime import datetime

from .._models import BaseModel

from .sort_order import SortOrder

__all__ = ["PageMetadata"]


class PageMetadata(BaseModel):
    """Metadata for an API request and a page of results."""

    api_request_id: str
    """Unique identifier for the API request."""

    api_request_timestamp: datetime
    """UTC timestamp for the API request."""

    total_items: int
    """Total number of items available across all pages."""

    page_number: int
    """Current page number."""

    page_size: int
    """Number of items per page."""

    max_page_size: int
    """Maximum page size allowed for this endpoint."""

    sort_by: str
    """Field used to sort the results."""

    sort_order: SortOrder
    """Sort direction for the results."""

    total_pages: int
    """Total number of pages available."""

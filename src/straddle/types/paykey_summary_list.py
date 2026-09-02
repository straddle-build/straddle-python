# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from .._models import BaseModel

from .page_metadata import PageMetadata
from .response_type import ResponseType
from .paykey_summary import PaykeySummary

__all__ = ["PaykeySummaryList"]


class PaykeySummaryList(BaseModel):
    meta: PageMetadata
    """Metadata for an API request and a page of results."""

    response_type: ResponseType
    """
    Shape of the response envelope.
    - `object` means `data` contains one JSON object.
    - `array` means `data` contains an array of JSON objects.
    - `error` means `error` contains the error details.
    - `none` means the response contains no data.
    """

    data: List[PaykeySummary]
    """The `data` field contains the paykeys on this page."""

# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

from .page_metadata import PageMetadata
from .capability_request import CapabilityRequest

__all__ = ["CapabilityRequestList"]


class CapabilityRequestList(BaseModel):
    meta: PageMetadata
    """Metadata for an API request and a page of results."""

    response_type: Literal["object", "array", "error", "none"]
    """
    Indicates how the response content is structured.
    - `object` means `data` contains one JSON object.
    - `array` means `data` contains an array of objects.
    - `error` means `error` contains error details.
    - `none` means the response has no data.
    """

    data: List[CapabilityRequest]
    """Capability requests returned for this page."""

# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

from .response_metadata import ResponseMetadata
from .response_type import ResponseType
from .bridge_token import BridgeToken

__all__ = ["BridgeTokenResponse"]


class BridgeTokenResponse(BaseModel):
    meta: ResponseMetadata
    """Metadata for an API request."""

    response_type: ResponseType
    """
    Shape of the response envelope.
    - `object` means `data` contains one JSON object.
    - `array` means `data` contains an array of JSON objects.
    - `error` means `error` contains the error details.
    - `none` means the response contains no data.
    """

    data: BridgeToken

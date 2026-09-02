# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from .._models import BaseModel

from .response_metadata import ResponseMetadata
from .unmasked_linked_bank_account import UnmaskedLinkedBankAccount

__all__ = ["UnmaskedLinkedBankAccountResponse"]


class UnmaskedLinkedBankAccountResponse(BaseModel):
    meta: ResponseMetadata
    """Metadata for an API request."""

    response_type: Literal["object", "array", "error", "none"]
    """
    Indicates how the response content is structured.
    - `object` means `data` contains one JSON object.
    - `array` means `data` contains an array of objects.
    - `error` means `error` contains error details.
    - `none` means the response has no data.
    """

    data: UnmaskedLinkedBankAccount

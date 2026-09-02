# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict
from .._types import FileTypes

from .._utils import PropertyInfo

__all__ = ["ChargeUploadAuthorizationProofParams"]


class ChargeUploadAuthorizationProofParams(TypedDict, total=False):
    file: Required[Annotated[FileTypes, PropertyInfo(alias="File")]]
    """The document file to upload as proof of authorization for this charge. Supported file types are PDF (.pdf), PNG (.png), JPEG (.jpg, .jpeg), Word (.doc), and Word (.docx), with a maximum file size of 10 MiB (10,485,760 bytes). Empty (0-byte) files are rejected. Uploaded files are validated for matching file signatures (magic bytes) and file extension agreement."""

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

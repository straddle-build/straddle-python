# File generated from our OpenAPI spec by Scalar. See README.md for details.

from datetime import datetime

from .._models import BaseModel

from .payment_document_type import PaymentDocumentType

__all__ = ["PaymentAuthorizationProof"]


class PaymentAuthorizationProof(BaseModel):
    document_id: str
    """Unique identifier for this document."""

    document_name: str
    """The file name of this document as uploaded."""

    document_type: PaymentDocumentType

    document_size: int
    """The size of this document in bytes."""

    uploaded_at: datetime
    """The UTC timestamp when this document was uploaded."""

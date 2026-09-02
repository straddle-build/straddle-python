# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

from .payment_relationship import PaymentRelationship
from .payment_type import PaymentType

__all__ = ["RelatedPayment"]


class RelatedPayment(BaseModel):
    id: str
    """Unique identifier of the related payment."""

    relationship: PaymentRelationship

    payment_type: PaymentType
    """The type of payment."""

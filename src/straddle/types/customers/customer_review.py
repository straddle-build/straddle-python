# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from ..._models import BaseModel

from ..customer import Customer
from .customer_identity_verification import CustomerIdentityVerification

__all__ = ["CustomerReview"]


class CustomerReview(BaseModel):
    customer_details: Customer

    identity_details: Optional[CustomerIdentityVerification] = None

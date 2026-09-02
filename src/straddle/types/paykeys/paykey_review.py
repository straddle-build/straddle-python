# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from ..._models import BaseModel

from ..paykey import Paykey
from .paykey_verification_details import PaykeyVerificationDetails

__all__ = ["PaykeyReview"]


class PaykeyReview(BaseModel):
    paykey_details: Paykey

    verification_details: Optional[PaykeyVerificationDetails] = None

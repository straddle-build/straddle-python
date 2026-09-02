# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from ..._models import BaseModel

from .account_name_match_details import AccountNameMatchDetails
from .account_validation_details import AccountValidationDetails

__all__ = ["PaykeyVerificationBreakdown"]


class PaykeyVerificationBreakdown(BaseModel):
    name_match: Optional[AccountNameMatchDetails] = None

    account_validation: Optional[AccountValidationDetails] = None

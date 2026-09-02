# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

from .paykey_balance_refresh_status import PaykeyBalanceRefreshStatus

__all__ = ["PaykeyBalanceDetails"]


class PaykeyBalanceDetails(BaseModel):
    account_balance: Optional[int] = None
    """Most recently retrieved account balance in cents."""

    updated_at: Optional[datetime] = None
    """Timestamp of the most recent account balance update."""

    status: PaykeyBalanceRefreshStatus

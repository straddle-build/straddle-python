# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

from .account_charge_settings import AccountChargeSettings
from .account_payout_settings import AccountPayoutSettings

__all__ = ["AccountPaymentSettings"]


class AccountPaymentSettings(BaseModel):
    charges: AccountChargeSettings

    payouts: AccountPayoutSettings

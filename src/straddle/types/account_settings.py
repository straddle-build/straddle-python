# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

from .charge_settings import ChargeSettings
from .payout_settings import PayoutSettings
from .account_statement_settings import AccountStatementSettings
from .account_payment_type_settings import AccountPaymentTypeSettings
from .account_customer_type_settings import AccountCustomerTypeSettings
from .account_consent_settings import AccountConsentSettings
from .account_policy_controls import AccountPolicyControls

__all__ = ["AccountSettings"]


class AccountSettings(BaseModel):
    charges: ChargeSettings

    payouts: PayoutSettings

    statement_settings: AccountStatementSettings

    payment_types: AccountPaymentTypeSettings

    customer_types: AccountCustomerTypeSettings

    consent_types: AccountConsentSettings

    configuration: AccountPolicyControls

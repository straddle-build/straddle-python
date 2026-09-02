# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

from .account_payment_capabilities import AccountPaymentCapabilities
from .account_customer_capabilities import AccountCustomerCapabilities
from .account_consent_capabilities import AccountConsentCapabilities

__all__ = ["AccountCapabilities"]


class AccountCapabilities(BaseModel):
    payment_types: AccountPaymentCapabilities

    customer_types: AccountCustomerCapabilities

    consent_types: AccountConsentCapabilities

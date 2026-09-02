# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["SimulatedPaymentOutcome"]

SimulatedPaymentOutcome: TypeAlias = Literal[
    "standard",
    "paid",
    "on_hold_daily_limit",
    "cancelled_for_fraud_risk",
    "cancelled_for_balance_check",
    "failed_insufficient_funds",
    "reversed_insufficient_funds",
    "failed_customer_dispute",
    "reversed_customer_dispute",
    "failed_closed_bank_account",
    "reversed_closed_bank_account",
    "failed_not_authorized",
    "reversed_not_authorized",
]

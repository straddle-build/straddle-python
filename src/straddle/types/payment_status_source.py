# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["PaymentStatusSource"]

PaymentStatusSource: TypeAlias = Literal["watchtower", "bank_decline", "customer_dispute", "user_action", "system"]

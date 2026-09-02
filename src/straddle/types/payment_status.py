# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["PaymentStatus"]

PaymentStatus: TypeAlias = Literal[
    "created", "scheduled", "failed", "cancelled", "on_hold", "pending", "paid", "reversed", "validating"
]

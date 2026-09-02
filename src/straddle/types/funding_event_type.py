# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["FundingEventType"]

FundingEventType: TypeAlias = Literal["charge_deposit", "charge_reversal", "payout_return", "payout_withdrawal"]

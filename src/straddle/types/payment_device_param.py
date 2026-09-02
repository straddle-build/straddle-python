# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PaymentDeviceParam"]


class PaymentDeviceParam(TypedDict, total=False):
    ip_address: Required[str]
    """The IP address of the device used when the customer authorized the charge or payout. Use `0.0.0.0` to represent an offline consent interaction."""

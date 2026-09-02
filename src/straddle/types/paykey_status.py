# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["PaykeyStatus"]

PaykeyStatus: TypeAlias = Literal["pending", "active", "inactive", "rejected", "review", "blocked"]

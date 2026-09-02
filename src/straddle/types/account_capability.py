# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountCapability"]


class AccountCapability(BaseModel):
    capability_status: Literal["active", "inactive"]
    """Status of the capability for the account."""

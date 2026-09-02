# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

from .account_business_profile_param import AccountBusinessProfileParam

__all__ = ["AccountUpdateParams"]


class AccountUpdateParams(TypedDict, total=False):
    business_profile: Required[AccountBusinessProfileParam]

    metadata: Optional[Dict[str, Optional[str]]]
    """Up to 20 user-defined key-value pairs."""

    external_id: Optional[str]
    """Your unique ID for the account."""

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

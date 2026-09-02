# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

from .account_business_profile_param import AccountBusinessProfileParam

__all__ = ["AccountCreateParams"]


class AccountCreateParams(TypedDict, total=False):
    organization_id: Required[str]
    """ID of the organization that will own the account."""

    account_type: Required[Literal["business"]]
    """Account type. The only accepted value is `business`."""

    business_profile: Required[AccountBusinessProfileParam]

    access_level: Required[Literal["standard", "managed"]]
    """The account access level. `standard` provides normal account access, including access to the Straddle dashboard. `managed` means the platform manages the account and account users cannot access the Straddle dashboard."""

    metadata: Optional[Dict[str, Optional[str]]]
    """Up to 20 user-defined key-value pairs."""

    external_id: Optional[str]
    """Your unique ID for the account."""

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

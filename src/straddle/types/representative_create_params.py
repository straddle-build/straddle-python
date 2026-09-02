# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Optional, Union
from datetime import date
from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

from .representative_relationship_param import RepresentativeRelationshipParam

__all__ = ["RepresentativeCreateParams"]


class RepresentativeCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """ID of the account associated with the representative."""

    first_name: Required[str]
    """Representative's first name."""

    last_name: Required[str]
    """Representative's last name."""

    dob: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Representative's date of birth in `YYYY-MM-DD` format."""

    ssn_last4: Required[str]
    """Last four digits of the representative's Social Security number."""

    email: Required[str]
    """Representative's company email address."""

    mobile_number: Required[str]
    """Representative's mobile phone number in E.164 format."""

    relationship: Required[RepresentativeRelationshipParam]

    external_id: Optional[str]
    """Your unique ID for the representative."""

    metadata: Optional[Dict[str, str]]
    """Up to 20 user-defined key-value pairs."""

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

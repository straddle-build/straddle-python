# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypedDict

from .._utils import PropertyInfo

__all__ = ["TermsOfServiceParam"]


class TermsOfServiceParam(TypedDict, total=False):
    accepted_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Date and time when the account accepted the Terms of Service."""

    accepted_ip: Optional[str]
    """IP address used to accept the Terms of Service."""

    accepted_user_agent: Optional[str]
    """User agent of the browser or application that accepted the Terms of Service."""

    agreement_url: Required[Optional[str]]
    """URL of the accepted agreement."""

    agreement_type: Required[Literal["embedded", "direct"]]
    """Agreement type. Use `embedded` unless Straddle has enabled the platform for `direct` agreements."""

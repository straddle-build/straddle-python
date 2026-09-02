# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Optional, Union
from datetime import date
from typing_extensions import Annotated, Required, TypeAlias, TypedDict

from .._utils import PropertyInfo

from .business_customer_representative_param import BusinessCustomerRepresentativeParam

__all__ = ["UnmaskedComplianceProfileParam", "IndividualComplianceProfile", "BusinessComplianceProfile"]


class BusinessComplianceProfile(TypedDict, total=False):
    ein: Required[Optional[str]]
    """Employer Identification Number in `XX-XXXXXXX` format. Required for Patriot Act-compliant KYB verification."""

    legal_business_name: Required[Optional[str]]
    """Official business name registered with the IRS."""

    website: Optional[str]
    """Official business website URL."""

    representatives: Optional[Iterable[BusinessCustomerRepresentativeParam]]
    """Representatives associated with the business. Valid only for `business` customers."""


class IndividualComplianceProfile(TypedDict, total=False):
    ssn: Required[Optional[str]]
    """Social Security number in `XXX-XX-XXXX` format. Required for Patriot Act-compliant KYC verification."""

    dob: Required[Annotated[Optional[Union[str, date]], PropertyInfo(format="iso8601")]]
    """Date of birth in `YYYY-MM-DD` format. Required for Patriot Act-compliant KYC verification."""


UnmaskedComplianceProfileParam: TypeAlias = Union[IndividualComplianceProfile, BusinessComplianceProfile]

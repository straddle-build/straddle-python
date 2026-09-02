# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional, Union
from datetime import date
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["UnmaskedComplianceProfile", "IndividualComplianceProfile", "BusinessComplianceProfile"]


class BusinessComplianceProfile(BaseModel):
    ein: Optional[str] = None
    """Employer Identification Number in `XX-XXXXXXX` format. Required for Patriot Act-compliant KYB verification."""

    legal_business_name: Optional[str] = None
    """Official business name registered with the IRS."""

    website: Optional[str] = None
    """Official business website URL."""

    representatives: Optional[List[object]] = None
    """Representatives associated with the business. Valid only for `business` customers."""


class IndividualComplianceProfile(BaseModel):
    ssn: Optional[str] = None
    """Social Security number in `XXX-XX-XXXX` format. Required for Patriot Act-compliant KYC verification."""

    dob: Optional[date] = None
    """Date of birth in `YYYY-MM-DD` format. Required for Patriot Act-compliant KYC verification."""


UnmaskedComplianceProfile: TypeAlias = Union[IndividualComplianceProfile, BusinessComplianceProfile]

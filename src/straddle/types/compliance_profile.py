# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional, Union
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["ComplianceProfile", "IndividualComplianceProfile", "BusinessComplianceProfile"]


class BusinessComplianceProfile(BaseModel):
    ein: Optional[str] = None
    """Masked Employer Identification Number in `**-*******` format."""

    legal_business_name: Optional[str] = None
    """Official registered business name associated with `ein`."""

    website: Optional[str] = None
    """Official business website URL."""

    representatives: Optional[List[object]] = None
    """Representatives associated with the business. Valid only for `business` customers."""


class IndividualComplianceProfile(BaseModel):
    dob: Optional[str] = None
    """Masked date of birth in `****-**-**` format."""

    ssn: Optional[str] = None
    """Masked Social Security number in `***-**-****` format."""


ComplianceProfile: TypeAlias = Union[IndividualComplianceProfile, BusinessComplianceProfile]

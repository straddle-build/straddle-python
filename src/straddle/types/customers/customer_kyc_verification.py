# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

from .verification_decision import VerificationDecision

__all__ = ["CustomerKYCVerification", "Validations"]


class Validations(BaseModel):
    first_name: Optional[bool] = None
    """Whether the customer's first name passed validation."""

    last_name: Optional[bool] = None
    """Whether the customer's last name passed validation."""

    address: Optional[bool] = None
    """Whether the customer's address passed validation."""

    city: Optional[bool] = None
    """Whether the customer's city passed validation."""

    state: Optional[bool] = None
    """Whether the customer's state passed validation."""

    zip: Optional[bool] = None
    """Whether the customer's ZIP code passed validation."""

    phone: Optional[bool] = None
    """Whether the customer's phone passed validation."""

    dob: Optional[bool] = None
    """Whether the customer's date of birth passed validation."""

    ssn: Optional[bool] = None
    """Whether the customer's Social Security number passed validation."""

    email: Optional[bool] = None
    """Whether the customer's email passed validation."""


class CustomerKYCVerification(BaseModel):
    decision: Optional[VerificationDecision] = None

    codes: Optional[List[str]] = None
    """Result codes from Know Your Customer (KYC) screening."""

    validations: Validations
    """Results for each Know Your Customer (KYC) validation."""

# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

from .account_industry import AccountIndustry
from .account_support_channels import AccountSupportChannels
from .account_address import AccountAddress

__all__ = ["AccountBusinessProfile"]


class AccountBusinessProfile(BaseModel):
    name: str
    """The operating or trade name of the business."""

    website: str
    """URL of the business's primary website."""

    legal_name: Optional[str] = None
    """The official registered name of the business."""

    description: Optional[str] = None
    """Description of the business and its products or services."""

    use_case: Optional[str] = None
    """How the business plans to use Straddle."""

    tax_id: Optional[str] = None
    """Business tax identification number, such as a US Employer Identification Number (EIN)."""

    phone: Optional[str] = None
    """Primary business phone number in E.164 format."""

    address: Optional[AccountAddress] = None
    """Optional business address. If provided, `line1`, `city`, `state`, and `postal_code` are required."""

    industry: Optional[AccountIndustry] = None

    support_channels: Optional[AccountSupportChannels] = None

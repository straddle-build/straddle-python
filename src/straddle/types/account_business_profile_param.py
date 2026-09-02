# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .account_address_param import AccountAddressParam
from .account_industry_param import AccountIndustryParam
from .account_support_channels_param import AccountSupportChannelsParam

__all__ = ["AccountBusinessProfileParam"]


class AccountBusinessProfileParam(TypedDict, total=False):
    name: Required[str]
    """The operating or trade name of the business."""

    website: Required[str]
    """URL of the business's primary website."""

    legal_name: Optional[str]
    """The official registered name of the business."""

    description: Optional[str]
    """Description of the business and its products or services."""

    use_case: Optional[str]
    """How the business plans to use Straddle."""

    tax_id: Optional[str]
    """Business tax identification number, such as a US Employer Identification Number (EIN)."""

    phone: Optional[str]
    """Primary business phone number in E.164 format."""

    address: Optional[AccountAddressParam]
    """Optional business address. If provided, `line1`, `city`, `state`, and `postal_code` are required."""

    industry: AccountIndustryParam

    support_channels: AccountSupportChannelsParam

# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

from .customer_type import CustomerType
from .customer_address_param import CustomerAddressParam
from .unmasked_compliance_profile_param import UnmaskedComplianceProfileParam
from .customer_device_param import CustomerDeviceParam
from .customer_configuration_param import CustomerConfigurationParam

__all__ = ["CustomerCreateParams"]


class CustomerCreateParams(TypedDict, total=False):
    name: Required[str]
    """Full name for an individual customer or business name for a business customer."""

    type: Required[CustomerType]

    email: Required[str]
    """Customer email address."""

    address: Optional[CustomerAddressParam]
    """Customer postal address. When provided, the object must include all required fields."""

    phone: Required[str]
    """Customer phone number in E.164 format. A mobile number is preferred."""

    compliance_profile: Optional[UnmaskedComplianceProfileParam]
    """Customer compliance profile. When provided, the object must include all fields required for the customer type."""

    external_id: Optional[str]
    """Unique identifier for the customer in your system."""

    device: Required[CustomerDeviceParam]

    metadata: Optional[Dict[str, str]]
    """Up to 20 user-defined key-value pairs associated with the customer."""

    config: CustomerConfigurationParam

    straddle_account_id: Annotated[str, PropertyInfo(alias="Straddle-Account-Id")]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

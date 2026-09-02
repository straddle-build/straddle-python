# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from .._utils import PropertyInfo

from .terms_of_service_param import TermsOfServiceParam

__all__ = ["AccountOnboardParams"]


class AccountOnboardParams(TypedDict, total=False):
    terms_of_service: Required[TermsOfServiceParam]

    request_id: Annotated[str, PropertyInfo(alias="Request-Id")]

    correlation_id: Annotated[str, PropertyInfo(alias="Correlation-Id")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

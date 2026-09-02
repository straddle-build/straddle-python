# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List

from ..._models import BaseModel

from .correlation_bucket import CorrelationBucket

__all__ = ["IdentityVerificationWatchlistMatch"]


class IdentityVerificationWatchlistMatch(BaseModel):
    list_name: str
    """Name of the watchlist that contains the matching record."""

    urls: List[str]
    """Source URLs associated with the match."""

    match_fields: List[str]
    """Customer fields that match the watchlist record."""

    correlation: CorrelationBucket

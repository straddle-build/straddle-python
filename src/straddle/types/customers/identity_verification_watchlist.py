# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

from .verification_decision import VerificationDecision
from .identity_verification_watchlist_match import IdentityVerificationWatchlistMatch

__all__ = ["IdentityVerificationWatchlist"]


class IdentityVerificationWatchlist(BaseModel):
    decision: Optional[VerificationDecision] = None

    codes: Optional[List[str]] = None
    """Result codes from Straddle watchlist screening."""

    matched: Optional[List[str]] = None
    """Names of watchlists with matches."""

    matches: Optional[List[IdentityVerificationWatchlistMatch]] = None
    """Details for matches found during watchlist screening."""

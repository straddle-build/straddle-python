# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["ReputationInsights"]


class ReputationInsights(BaseModel):
    ach_fraud_transactions_count: Optional[int] = None
    """Number of fraudulent ACH transactions."""

    ach_fraud_transactions_total_amount: Optional[float] = None
    """Total amount of fraudulent ACH transactions."""

    ach_fraud_transactions_dates: Optional[List[date]] = None
    """Dates when fraudulent ACH transactions occurred."""

    ach_returned_transactions_count: Optional[int] = None
    """Number of returned ACH transactions."""

    ach_returned_transactions_total_amount: Optional[float] = None
    """Total amount of returned ACH transactions."""

    ach_returned_transactions_dates: Optional[List[date]] = None
    """Dates when ACH transactions were returned."""

    card_fraud_transactions_count: Optional[int] = None
    """Number of fraudulent card transactions."""

    card_fraud_transactions_total_amount: Optional[float] = None
    """Total amount of fraudulent card transactions."""

    card_fraud_transactions_dates: Optional[List[date]] = None
    """Dates when fraudulent card transactions occurred."""

    card_disputed_transactions_count: Optional[int] = None
    """Number of disputed card transactions."""

    card_disputed_transactions_total_amount: Optional[float] = None
    """Total amount of disputed card transactions."""

    card_disputed_transactions_dates: Optional[List[date]] = None
    """Dates when card transactions were disputed."""

    card_stopped_transactions_count: Optional[int] = None
    """Number of stopped card transactions."""

    card_stopped_transactions_dates: Optional[List[date]] = None
    """Dates when card transactions were stopped."""

    accounts_count: Optional[int] = None
    """Number of accounts associated with the identity."""

    accounts_active_count: Optional[int] = None
    """Number of active accounts associated with the identity."""

    accounts_closed_count: Optional[int] = None
    """Number of closed accounts associated with the identity."""

    accounts_closed_dates: Optional[List[date]] = None
    """Dates when accounts associated with the identity were closed."""

    accounts_fraud_count: Optional[int] = None
    """Number of accounts associated with fraud."""

    accounts_fraud_loss_total_amount: Optional[float] = None
    """Total fraud loss associated with the accounts."""

    accounts_fraud_labeled_dates: Optional[List[date]] = None
    """Dates when accounts were labeled as fraudulent."""

    applications_count: Optional[int] = None
    """Number of applications associated with the identity."""

    applications_dates: Optional[List[date]] = None
    """Dates when applications associated with the identity were submitted."""

    applications_approved_count: Optional[int] = None
    """Number of approved applications associated with the identity."""

    applications_declined_count: Optional[int] = None
    """Number of declined applications associated with the identity."""

    applications_fraud_count: Optional[int] = None
    """Number of applications associated with fraud."""

    user_institution_count: Optional[int] = None
    """Number of financial institutions associated with the identity."""

    user_dob_count: Optional[int] = None
    """Number of dates of birth associated with the identity."""

    user_mobile_count: Optional[int] = None
    """Number of mobile numbers associated with the identity."""

    user_email_count: Optional[int] = None
    """Number of email addresses associated with the identity."""

    user_address_count: Optional[int] = None
    """Number of addresses associated with the identity."""

    user_active_profile_count: Optional[int] = None
    """Number of active profiles associated with the identity."""

    user_closed_profile_count: Optional[int] = None
    """Number of closed profiles associated with the identity."""

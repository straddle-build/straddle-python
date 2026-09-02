# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke test: calls every generated operation once to confirm the SDK can reach each endpoint.
# Run it from this repo with `python tests/smoke-test.py`. The generator also runs this file
# against a mock server and reads the JSON report produced via SCALAR_SMOKE_REPORT.
from __future__ import annotations

import json
import os
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable, TypedDict

from straddle import StraddleAPI

# The shared smoke-test runner injects base URL and credentials through the same
# environment variables the generated client reads in normal use.
client = StraddleAPI(max_retries=0, timeout=30)


class SmokeResult(TypedDict, total=False):
    operation: str
    method: str
    path: str
    label: str
    status: str
    durationMs: int
    error: str


class _SmokeCaseBase(TypedDict):
    operation: str
    method: str
    path: str
    run: Callable[[], Any]


# `label` says which of an operation's two calls this is — "required params" or "all params".
# It sits in a total=False extension because it is absent when the operation contributed a
# single case, while the fields above are always present.
class SmokeCase(_SmokeCaseBase, total=False):
    label: str


def _smoke_case_0() -> None:
    account = client.accounts.retrieve(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_1() -> None:
    account = client.accounts.retrieve(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_2() -> None:
    account = client.accounts.update(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        business_profile={"name": "", "website": "https://example.com"},
    )


def _smoke_case_3() -> None:
    account = client.accounts.update(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        business_profile={
            "name": "",
            "website": "https://example.com",
            "legal_name": "",
            "description": "",
            "use_case": "",
            "tax_id": "",
            "phone": "",
            "address": {"line1": "", "city": "", "state": "", "postal_code": ""},
            "industry": {},
            "support_channels": {},
        },
        metadata={},
        external_id="",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_4() -> None:
    account = client.accounts.create(
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        account_type="business",
        business_profile={"name": "", "website": "https://example.com"},
        access_level="standard",
    )


def _smoke_case_5() -> None:
    account = client.accounts.create(
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        account_type="business",
        business_profile={
            "name": "",
            "website": "https://example.com",
            "legal_name": "",
            "description": "",
            "use_case": "",
            "tax_id": "",
            "phone": "",
            "address": {"line1": "", "city": "", "state": "", "postal_code": ""},
            "industry": {},
            "support_channels": {},
        },
        access_level="standard",
        metadata={},
        external_id="",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_6() -> None:
    account = client.accounts.list(
        page_number=1,
        page_size=100,
        sort_by="id",
        sort_order="asc",
    )


def _smoke_case_7() -> None:
    account = client.accounts.list(
        page_number=1,
        page_size=100,
        sort_by="id",
        sort_order="asc",
        search_text="search_text",
        status="created",
        type="business",
        external_id="external_id",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_8() -> None:
    account = client.accounts.onboard(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        terms_of_service={
            "accepted_date": "2024-01-01T00:00:00.000Z",
            "agreement_url": "",
            "agreement_type": "embedded",
        },
    )


def _smoke_case_9() -> None:
    account = client.accounts.onboard(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        terms_of_service={
            "accepted_date": "2024-01-01T00:00:00.000Z",
            "accepted_ip": "",
            "accepted_user_agent": "",
            "agreement_url": "",
            "agreement_type": "embedded",
        },
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_10() -> None:
    account = client.accounts.simulate_onboarding(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_11() -> None:
    account = client.accounts.simulate_onboarding(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        final_status="onboarding",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_12() -> None:
    capability_request = client.capability_requests.create(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_13() -> None:
    capability_request = client.capability_requests.create(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        charges={"enable": False, "max_amount": 0, "daily_amount": 0, "monthly_count": 0, "monthly_amount": 0},
        payouts={"enable": False, "max_amount": 0, "daily_amount": 0, "monthly_count": 0, "monthly_amount": 0},
        internet={"enable": False},
        individuals={"enable": False},
        businesses={"enable": False},
        signed_agreement={"enable": False},
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_14() -> None:
    capability_request = client.capability_requests.list(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        page_number=1,
        page_size=100,
        sort_by="id",
        sort_order="asc",
    )


def _smoke_case_15() -> None:
    capability_request = client.capability_requests.list(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        type="charges",
        category="payment_type",
        status="active",
        page_number=1,
        page_size=100,
        sort_by="id",
        sort_order="asc",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_16() -> None:
    linked_bank_account = client.linked_bank_accounts.create(
        bank_account={"account_holder": "", "routing_number": "xxxxxxxxx", "account_number": ""},
    )


def _smoke_case_17() -> None:
    linked_bank_account = client.linked_bank_accounts.create(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        bank_account={"account_holder": "", "routing_number": "xxxxxxxxx", "account_number": ""},
        metadata={},
        platform_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        purposes=[],
        description="",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_18() -> None:
    linked_bank_account = client.linked_bank_accounts.list(
        page_number=1,
        page_size=100,
        sort_by="id",
        sort_order="asc",
    )


def _smoke_case_19() -> None:
    linked_bank_account = client.linked_bank_accounts.list(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        page_number=1,
        page_size=100,
        sort_by="id",
        sort_order="asc",
        level="account",
        purpose="charges",
        status="created",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_20() -> None:
    linked_bank_account = client.linked_bank_accounts.update(
        linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        bank_account={"account_holder": "", "routing_number": "xxxxxxxxx", "account_number": ""},
    )


def _smoke_case_21() -> None:
    linked_bank_account = client.linked_bank_accounts.update(
        linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        bank_account={"account_holder": "", "routing_number": "xxxxxxxxx", "account_number": ""},
        metadata={},
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_22() -> None:
    linked_bank_account = client.linked_bank_accounts.retrieve(
        linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_23() -> None:
    linked_bank_account = client.linked_bank_accounts.retrieve(
        linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_24() -> None:
    linked_bank_account = client.linked_bank_accounts.list_unmasked(
        linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_25() -> None:
    linked_bank_account = client.linked_bank_accounts.list_unmasked(
        linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_26() -> None:
    linked_bank_account = client.linked_bank_accounts.cancel(
        linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_27() -> None:
    linked_bank_account = client.linked_bank_accounts.cancel(
        linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_28() -> None:
    organization = client.organizations.create(
        name="",
    )


def _smoke_case_29() -> None:
    organization = client.organizations.create(
        name="",
        metadata={},
        external_id="",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_30() -> None:
    organization = client.organizations.list(
        page_number=1,
        page_size=100,
        sort_by="id",
        sort_order="asc",
    )


def _smoke_case_31() -> None:
    organization = client.organizations.list(
        name="name",
        external_id="external_id",
        page_number=1,
        page_size=100,
        sort_by="id",
        sort_order="asc",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_32() -> None:
    organization = client.organizations.retrieve(
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_33() -> None:
    organization = client.organizations.retrieve(
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_34() -> None:
    representative = client.representatives.create(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        first_name="",
        last_name="",
        dob="1980-01-01",
        ssn_last4="1234",
        email="ron.swanson@pawnee.com",
        mobile_number="+12128675309",
        relationship={"primary": False, "control": False, "owner": False},
    )


def _smoke_case_35() -> None:
    representative = client.representatives.create(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        first_name="",
        last_name="",
        dob="1980-01-01",
        ssn_last4="1234",
        email="ron.swanson@pawnee.com",
        mobile_number="+12128675309",
        relationship={"primary": False, "control": False, "owner": False, "percent_ownership": 0, "title": ""},
        external_id="",
        metadata={},
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_36() -> None:
    representative = client.representatives.list(
        page_number=1,
        page_size=100,
        sort_by="id",
        sort_order="asc",
    )


def _smoke_case_37() -> None:
    representative = client.representatives.list(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        page_number=1,
        page_size=100,
        sort_by="id",
        sort_order="asc",
        platform_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        level="account",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_38() -> None:
    representative = client.representatives.update(
        representative_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        first_name="Ron",
        last_name="Swanson",
        dob="1980-01-01",
        ssn_last4="1234",
        email="ron.swanson@pawnee.com",
        mobile_number="+12128675309",
        relationship={"primary": False, "control": False, "owner": False},
    )


def _smoke_case_39() -> None:
    representative = client.representatives.update(
        representative_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        first_name="Ron",
        last_name="Swanson",
        dob="1980-01-01",
        ssn_last4="1234",
        email="ron.swanson@pawnee.com",
        mobile_number="+12128675309",
        relationship={"primary": False, "control": False, "owner": False, "percent_ownership": 0, "title": ""},
        external_id="",
        metadata={},
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_40() -> None:
    representative = client.representatives.retrieve(
        representative_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_41() -> None:
    representative = client.representatives.retrieve(
        representative_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_42() -> None:
    representative = client.representatives.list_unmasked(
        representative_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_43() -> None:
    representative = client.representatives.list_unmasked(
        representative_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_44() -> None:
    bridge = client.bridge.create_bank_account_paykey(
        customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        routing_number="xxxxxxxxx",
        account_number="",
        account_type="checking",
    )


def _smoke_case_45() -> None:
    bridge = client.bridge.create_bank_account_paykey(
        customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        routing_number="xxxxxxxxx",
        account_number="",
        account_type="checking",
        metadata={},
        config={"sandbox_outcome": "standard", "processing_method": "inline"},
        external_id="",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_46() -> None:
    bridge = client.bridge.create_plaid_paykey(
        customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        plaid_token="",
    )


def _smoke_case_47() -> None:
    bridge = client.bridge.create_plaid_paykey(
        customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        plaid_token="",
        metadata={},
        config={"sandbox_outcome": "standard", "processing_method": "inline"},
        external_id="",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_48() -> None:
    bridge = client.bridge.create_token(
        customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_49() -> None:
    bridge = client.bridge.create_token(
        customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        config={"sandbox_outcome": "standard", "processing_method": "inline"},
        external_id="",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_50() -> None:
    bridge = client.bridge.create_quiltt_paykey(
        customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        quiltt_token="",
    )


def _smoke_case_51() -> None:
    bridge = client.bridge.create_quiltt_paykey(
        customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        quiltt_token="",
        metadata={},
        config={"sandbox_outcome": "standard", "processing_method": "inline"},
        external_id="",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_52() -> None:
    customer = client.customers.retrieve(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_53() -> None:
    customer = client.customers.retrieve(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_54() -> None:
    customer = client.customers.update(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="",
        email="user@example.com",
        phone="",
        device={"ip_address": "192.168.1.1"},
        status="verified",
    )


def _smoke_case_55() -> None:
    customer = client.customers.update(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        name="",
        email="user@example.com",
        address={"address1": "123 Main St", "address2": "Apt 1", "city": "Anytown", "state": "CA", "zip": "12345"},
        phone="",
        compliance_profile={"ssn": "123-45-6789", "dob": "1969-04-20"},
        external_id="",
        device={"ip_address": "192.168.1.1"},
        status="verified",
        metadata={},
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_56() -> None:
    customer = client.customers.delete(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_57() -> None:
    customer = client.customers.delete(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_58() -> None:
    customer = client.customers.list(
        page_number=1,
        page_size=100,
        sort_order="asc",
    )


def _smoke_case_59() -> None:
    customer = client.customers.list(
        page_number=1,
        page_size=100,
        sort_by="name",
        sort_order="asc",
        created_from="2024-01-01T00:00:00.000Z",
        created_to="2024-01-01T00:00:00.000Z",
        name="name",
        external_id="external_id",
        email="email",
        status=["pending"],
        search_text="search_text",
        types=["individual"],
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_60() -> None:
    customer = client.customers.create(
        name="Ron Swanson",
        type="individual",
        email="ron.swanson@pawnee.com",
        address={"address1": "123 Main St", "city": "Anytown", "state": "CA", "zip": "94105"},
        phone="+12128675309",
        external_id="customer_123",
        device={"ip_address": "192.168.1.1"},
        metadata={},
    )


def _smoke_case_61() -> None:
    customer = client.customers.create(
        name="Ron Swanson",
        type="individual",
        email="ron.swanson@pawnee.com",
        address={"address1": "123 Main St", "city": "Anytown", "state": "CA", "zip": "94105"},
        phone="+12128675309",
        compliance_profile={"ssn": "123-45-6789", "dob": "1969-04-20"},
        external_id="customer_123",
        device={"ip_address": "192.168.1.1"},
        metadata={},
        config={"sandbox_outcome": "standard", "processing_method": "inline"},
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_62() -> None:
    customer = client.customers.list_unmasked(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_63() -> None:
    customer = client.customers.list_unmasked(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_64() -> None:
    customer = client.customers.refresh_review(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_65() -> None:
    customer = client.customers.refresh_review(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_66() -> None:
    review = client.customers.review.list(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_67() -> None:
    review = client.customers.review.list(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_68() -> None:
    review = client.customers.review.set_verification_decision(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        status="verified",
    )


def _smoke_case_69() -> None:
    review = client.customers.review.set_verification_decision(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        status="verified",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_70() -> None:
    paykey = client.paykeys.retrieve(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_71() -> None:
    paykey = client.paykeys.retrieve(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_72() -> None:
    paykey = client.paykeys.list_unmasked(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_73() -> None:
    paykey = client.paykeys.list_unmasked(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_74() -> None:
    paykey = client.paykeys.list(
        page_number=1,
        page_size=100,
        sort_order="asc",
    )


def _smoke_case_75() -> None:
    paykey = client.paykeys.list(
        customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        page_number=1,
        page_size=100,
        status=["pending"],
        sort_by="institution_name",
        sort_order="asc",
        source=["bank_account"],
        unblock_eligible=True,
        search_text="search_text",
        created_from="2024-01-01T00:00:00.000Z",
        created_to="2024-01-01T00:00:00.000Z",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_76() -> None:
    paykey = client.paykeys.reveal(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_77() -> None:
    paykey = client.paykeys.reveal(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_78() -> None:
    paykey = client.paykeys.cancel(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_79() -> None:
    paykey = client.paykeys.cancel(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        reason="",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_80() -> None:
    paykey = client.paykeys.refresh_review(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_81() -> None:
    paykey = client.paykeys.refresh_review(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_82() -> None:
    paykey = client.paykeys.refresh_balance(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_83() -> None:
    paykey = client.paykeys.refresh_balance(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_84() -> None:
    paykey = client.paykeys.unblock(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_85() -> None:
    paykey = client.paykeys.unblock(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        message="",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_86() -> None:
    review = client.paykeys.review.set_verification_decision(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        status="active",
    )


def _smoke_case_87() -> None:
    review = client.paykeys.review.set_verification_decision(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        status="active",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_88() -> None:
    review = client.paykeys.review.list(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_89() -> None:
    review = client.paykeys.review.list(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_90() -> None:
    charge = client.charges.retrieve(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_91() -> None:
    charge = client.charges.retrieve(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_92() -> None:
    charge = client.charges.update(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        description="Monthly subscription fee",
        amount=10000,
        payment_date="2024-01-01",
    )


def _smoke_case_93() -> None:
    charge = client.charges.update(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        description="Monthly subscription fee",
        amount=10000,
        payment_date="2024-01-01",
        metadata={},
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_94() -> None:
    charge = client.charges.create(
        paykey="",
        description="Monthly subscription fee",
        amount=10000,
        currency="USD",
        payment_date="2024-01-01",
        consent_type="internet",
        device={"ip_address": "192.168.1.1"},
        external_id="",
        config={"balance_check": "enabled"},
    )


def _smoke_case_95() -> None:
    charge = client.charges.create(
        paykey="",
        description="Monthly subscription fee",
        amount=10000,
        currency="USD",
        payment_date="2024-01-01",
        consent_type="internet",
        device={"ip_address": "192.168.1.1"},
        external_id="",
        config={"balance_check": "enabled", "sandbox_outcome": "standard", "auto_hold": False, "auto_hold_message": ""},
        metadata={},
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_96() -> None:
    charge = client.charges.hold(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_97() -> None:
    charge = client.charges.hold(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        reason="",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_98() -> None:
    charge = client.charges.release(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_99() -> None:
    charge = client.charges.release(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        reason="",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_100() -> None:
    charge = client.charges.cancel(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_101() -> None:
    charge = client.charges.cancel(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        reason="",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_102() -> None:
    charge = client.charges.list_unmasked(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_103() -> None:
    charge = client.charges.list_unmasked(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_104() -> None:
    charge = client.charges.resubmit(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_105() -> None:
    charge = client.charges.resubmit(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        description="",
        payment_date="2024-01-01",
        external_id="",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_106() -> None:
    charge = client.charges.refund(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_107() -> None:
    charge = client.charges.refund(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        amount=5000,
        description="",
        external_id="",
        payment_date="2024-01-01",
        metadata={},
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_108() -> None:
    charge = client.charges.upload_authorization_proof(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        file=b"",
    )


def _smoke_case_109() -> None:
    charge = client.charges.upload_authorization_proof(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        file=b"",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_110() -> None:
    funding_event = client.funding_events.list(
        page_number=1,
        page_size=100,
        sort_order="asc",
    )


def _smoke_case_111() -> None:
    funding_event = client.funding_events.list(
        page_number=1,
        page_size=100,
        sort_by="transfer_date",
        sort_order="asc",
        created_from="2024-01-01",
        created_to="2024-01-01",
        direction="deposit",
        event_type="charge_deposit",
        trace_number="trace_number",
        search_text="search_text",
        status=["created"],
        trace_id="trace_id",
        status_reason=["insufficient_funds"],
        status_source=["watchtower"],
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_112() -> None:
    funding_event = client.funding_events.retrieve(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_113() -> None:
    funding_event = client.funding_events.retrieve(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_114() -> None:
    funding_event = client.funding_events.simulate(
        funding_event_job_type="charges",
    )


def _smoke_case_115() -> None:
    funding_event = client.funding_events.simulate(
        funding_event_job_type="charges",
        sandbox_outcome="standard",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_116() -> None:
    funding_event = client.funding_events.list_payments(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        default_sort_order="asc",
        sort_order="asc",
    )


def _smoke_case_117() -> None:
    funding_event = client.funding_events.list_payments(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        page_number=1,
        page_size=1,
        include_metadata=True,
        default_page_size=1,
        default_sort="created_at",
        default_sort_order="asc",
        sort_by="created_at",
        sort_order="asc",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_118() -> None:
    payment = client.payments.list(
        page_number=1,
        page_size=100,
        sort_by="id",
        sort_order="asc",
        default_sort="id",
        default_sort_order="asc",
    )


def _smoke_case_119() -> None:
    payment = client.payments.list(
        page_number=1,
        page_size=100,
        sort_by="id",
        sort_order="asc",
        payment_type=["charge"],
        payment_status=["created"],
        payment_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        external_id="external_id",
        customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        paykey_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        paykey="paykey",
        min_amount=1,
        max_amount=1,
        min_payment_date="2024-01-01",
        max_payment_date="2024-01-01",
        min_created_at="2024-01-01T00:00:00.000Z",
        max_created_at="2024-01-01T00:00:00.000Z",
        min_effective_at="2024-01-01T00:00:00.000Z",
        max_effective_at="2024-01-01T00:00:00.000Z",
        funding_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        search_text="search_text",
        default_page_size=1,
        default_sort="id",
        default_sort_order="asc",
        status_reason=["insufficient_funds"],
        status_source=["watchtower"],
        include_metadata=True,
        is_refund=True,
        has_refund=True,
        is_resubmit=True,
        has_resubmit=True,
        min_updated_at="2024-01-01T00:00:00.000Z",
        max_updated_at="2024-01-01T00:00:00.000Z",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_120() -> None:
    payout = client.payouts.retrieve(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_121() -> None:
    payout = client.payouts.retrieve(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_122() -> None:
    payout = client.payouts.update(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        description="",
        amount=10000,
        payment_date="2024-01-01",
    )


def _smoke_case_123() -> None:
    payout = client.payouts.update(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        description="",
        amount=10000,
        payment_date="2024-01-01",
        metadata={},
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_124() -> None:
    payout = client.payouts.create(
        paykey="",
        description="Vendor invoice payment",
        amount=10000,
        currency="USD",
        payment_date="2024-01-01",
        device={"ip_address": "192.168.1.1"},
        external_id="",
    )


def _smoke_case_125() -> None:
    payout = client.payouts.create(
        paykey="",
        description="Vendor invoice payment",
        amount=10000,
        currency="USD",
        payment_date="2024-01-01",
        device={"ip_address": "192.168.1.1"},
        external_id="",
        config={"sandbox_outcome": "standard", "auto_hold": False, "auto_hold_message": ""},
        metadata={},
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_126() -> None:
    payout = client.payouts.hold(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_127() -> None:
    payout = client.payouts.hold(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        reason="",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_128() -> None:
    payout = client.payouts.release(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_129() -> None:
    payout = client.payouts.release(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        reason="",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_130() -> None:
    payout = client.payouts.cancel(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_131() -> None:
    payout = client.payouts.cancel(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        reason="",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_132() -> None:
    payout = client.payouts.list_unmasked(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_133() -> None:
    payout = client.payouts.list_unmasked(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


def _smoke_case_134() -> None:
    payout = client.payouts.resubmit(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_135() -> None:
    payout = client.payouts.resubmit(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        description="",
        payment_date="2024-01-01",
        external_id="",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_136() -> None:
    payout = client.payouts.upload_authorization_proof(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        file=b"",
    )


def _smoke_case_137() -> None:
    payout = client.payouts.upload_authorization_proof(
        id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        file=b"",
        straddle_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
        idempotency_key="idempotency_key",
    )


def _smoke_case_138() -> None:
    account_setting = client.account_settings.retrieve(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    )


def _smoke_case_139() -> None:
    account_setting = client.account_settings.retrieve(
        account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
        request_id="request_id",
        correlation_id="correlation_id",
    )


cases: list[SmokeCase] = [
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/accounts/{account_id}",
        "label": "required params",
        "run": _smoke_case_0,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/accounts/{account_id}",
        "label": "all params",
        "run": _smoke_case_1,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/accounts/{account_id}",
        "label": "required params",
        "run": _smoke_case_2,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/accounts/{account_id}",
        "label": "all params",
        "run": _smoke_case_3,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/accounts",
        "label": "required params",
        "run": _smoke_case_4,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/accounts",
        "label": "all params",
        "run": _smoke_case_5,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/accounts",
        "label": "required params",
        "run": _smoke_case_6,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/accounts",
        "label": "all params",
        "run": _smoke_case_7,
    },
    {
        "operation": "onboard",
        "method": "POST",
        "path": "/v1/accounts/{account_id}/onboard",
        "label": "required params",
        "run": _smoke_case_8,
    },
    {
        "operation": "onboard",
        "method": "POST",
        "path": "/v1/accounts/{account_id}/onboard",
        "label": "all params",
        "run": _smoke_case_9,
    },
    {
        "operation": "simulateOnboarding",
        "method": "POST",
        "path": "/v1/accounts/{account_id}/simulate",
        "label": "required params",
        "run": _smoke_case_10,
    },
    {
        "operation": "simulateOnboarding",
        "method": "POST",
        "path": "/v1/accounts/{account_id}/simulate",
        "label": "all params",
        "run": _smoke_case_11,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/accounts/{account_id}/capability_requests",
        "label": "required params",
        "run": _smoke_case_12,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/accounts/{account_id}/capability_requests",
        "label": "all params",
        "run": _smoke_case_13,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/accounts/{account_id}/capability_requests",
        "label": "required params",
        "run": _smoke_case_14,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/accounts/{account_id}/capability_requests",
        "label": "all params",
        "run": _smoke_case_15,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/linked_bank_accounts",
        "label": "required params",
        "run": _smoke_case_16,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/linked_bank_accounts",
        "label": "all params",
        "run": _smoke_case_17,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/linked_bank_accounts",
        "label": "required params",
        "run": _smoke_case_18,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/linked_bank_accounts",
        "label": "all params",
        "run": _smoke_case_19,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/linked_bank_accounts/{linked_bank_account_id}",
        "label": "required params",
        "run": _smoke_case_20,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/linked_bank_accounts/{linked_bank_account_id}",
        "label": "all params",
        "run": _smoke_case_21,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/linked_bank_accounts/{linked_bank_account_id}",
        "label": "required params",
        "run": _smoke_case_22,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/linked_bank_accounts/{linked_bank_account_id}",
        "label": "all params",
        "run": _smoke_case_23,
    },
    {
        "operation": "listUnmasked",
        "method": "GET",
        "path": "/v1/linked_bank_accounts/{linked_bank_account_id}/unmask",
        "label": "required params",
        "run": _smoke_case_24,
    },
    {
        "operation": "listUnmasked",
        "method": "GET",
        "path": "/v1/linked_bank_accounts/{linked_bank_account_id}/unmask",
        "label": "all params",
        "run": _smoke_case_25,
    },
    {
        "operation": "cancel",
        "method": "PATCH",
        "path": "/v1/linked_bank_accounts/{linked_bank_account_id}/cancel",
        "label": "required params",
        "run": _smoke_case_26,
    },
    {
        "operation": "cancel",
        "method": "PATCH",
        "path": "/v1/linked_bank_accounts/{linked_bank_account_id}/cancel",
        "label": "all params",
        "run": _smoke_case_27,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/organizations",
        "label": "required params",
        "run": _smoke_case_28,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/organizations",
        "label": "all params",
        "run": _smoke_case_29,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/organizations",
        "label": "required params",
        "run": _smoke_case_30,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/organizations",
        "label": "all params",
        "run": _smoke_case_31,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/organizations/{organization_id}",
        "label": "required params",
        "run": _smoke_case_32,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/organizations/{organization_id}",
        "label": "all params",
        "run": _smoke_case_33,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/representatives",
        "label": "required params",
        "run": _smoke_case_34,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/representatives",
        "label": "all params",
        "run": _smoke_case_35,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/representatives",
        "label": "required params",
        "run": _smoke_case_36,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/representatives",
        "label": "all params",
        "run": _smoke_case_37,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/representatives/{representative_id}",
        "label": "required params",
        "run": _smoke_case_38,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/representatives/{representative_id}",
        "label": "all params",
        "run": _smoke_case_39,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/representatives/{representative_id}",
        "label": "required params",
        "run": _smoke_case_40,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/representatives/{representative_id}",
        "label": "all params",
        "run": _smoke_case_41,
    },
    {
        "operation": "listUnmasked",
        "method": "GET",
        "path": "/v1/representatives/{representative_id}/unmask",
        "label": "required params",
        "run": _smoke_case_42,
    },
    {
        "operation": "listUnmasked",
        "method": "GET",
        "path": "/v1/representatives/{representative_id}/unmask",
        "label": "all params",
        "run": _smoke_case_43,
    },
    {
        "operation": "createBankAccountPaykey",
        "method": "POST",
        "path": "/v1/bridge/bank_account",
        "label": "required params",
        "run": _smoke_case_44,
    },
    {
        "operation": "createBankAccountPaykey",
        "method": "POST",
        "path": "/v1/bridge/bank_account",
        "label": "all params",
        "run": _smoke_case_45,
    },
    {
        "operation": "createPlaidPaykey",
        "method": "POST",
        "path": "/v1/bridge/plaid",
        "label": "required params",
        "run": _smoke_case_46,
    },
    {
        "operation": "createPlaidPaykey",
        "method": "POST",
        "path": "/v1/bridge/plaid",
        "label": "all params",
        "run": _smoke_case_47,
    },
    {
        "operation": "createToken",
        "method": "POST",
        "path": "/v1/bridge/initialize",
        "label": "required params",
        "run": _smoke_case_48,
    },
    {
        "operation": "createToken",
        "method": "POST",
        "path": "/v1/bridge/initialize",
        "label": "all params",
        "run": _smoke_case_49,
    },
    {
        "operation": "createQuilttPaykey",
        "method": "POST",
        "path": "/v1/bridge/quiltt",
        "label": "required params",
        "run": _smoke_case_50,
    },
    {
        "operation": "createQuilttPaykey",
        "method": "POST",
        "path": "/v1/bridge/quiltt",
        "label": "all params",
        "run": _smoke_case_51,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/customers/{id}",
        "label": "required params",
        "run": _smoke_case_52,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/customers/{id}",
        "label": "all params",
        "run": _smoke_case_53,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/customers/{id}",
        "label": "required params",
        "run": _smoke_case_54,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/customers/{id}",
        "label": "all params",
        "run": _smoke_case_55,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/customers/{id}",
        "label": "required params",
        "run": _smoke_case_56,
    },
    {
        "operation": "delete",
        "method": "DELETE",
        "path": "/v1/customers/{id}",
        "label": "all params",
        "run": _smoke_case_57,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/customers",
        "label": "required params",
        "run": _smoke_case_58,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/customers",
        "label": "all params",
        "run": _smoke_case_59,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/customers",
        "label": "required params",
        "run": _smoke_case_60,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/customers",
        "label": "all params",
        "run": _smoke_case_61,
    },
    {
        "operation": "listUnmasked",
        "method": "GET",
        "path": "/v1/customers/{id}/unmasked",
        "label": "required params",
        "run": _smoke_case_62,
    },
    {
        "operation": "listUnmasked",
        "method": "GET",
        "path": "/v1/customers/{id}/unmasked",
        "label": "all params",
        "run": _smoke_case_63,
    },
    {
        "operation": "refreshReview",
        "method": "PUT",
        "path": "/v1/customers/{id}/refresh_review",
        "label": "required params",
        "run": _smoke_case_64,
    },
    {
        "operation": "refreshReview",
        "method": "PUT",
        "path": "/v1/customers/{id}/refresh_review",
        "label": "all params",
        "run": _smoke_case_65,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/customers/{id}/review",
        "label": "required params",
        "run": _smoke_case_66,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/customers/{id}/review",
        "label": "all params",
        "run": _smoke_case_67,
    },
    {
        "operation": "setVerificationDecision",
        "method": "PATCH",
        "path": "/v1/customers/{id}/review",
        "label": "required params",
        "run": _smoke_case_68,
    },
    {
        "operation": "setVerificationDecision",
        "method": "PATCH",
        "path": "/v1/customers/{id}/review",
        "label": "all params",
        "run": _smoke_case_69,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/paykeys/{id}",
        "label": "required params",
        "run": _smoke_case_70,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/paykeys/{id}",
        "label": "all params",
        "run": _smoke_case_71,
    },
    {
        "operation": "listUnmasked",
        "method": "GET",
        "path": "/v1/paykeys/{id}/unmasked",
        "label": "required params",
        "run": _smoke_case_72,
    },
    {
        "operation": "listUnmasked",
        "method": "GET",
        "path": "/v1/paykeys/{id}/unmasked",
        "label": "all params",
        "run": _smoke_case_73,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/paykeys",
        "label": "required params",
        "run": _smoke_case_74,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/paykeys",
        "label": "all params",
        "run": _smoke_case_75,
    },
    {
        "operation": "reveal",
        "method": "GET",
        "path": "/v1/paykeys/{id}/reveal",
        "label": "required params",
        "run": _smoke_case_76,
    },
    {
        "operation": "reveal",
        "method": "GET",
        "path": "/v1/paykeys/{id}/reveal",
        "label": "all params",
        "run": _smoke_case_77,
    },
    {
        "operation": "cancel",
        "method": "PUT",
        "path": "/v1/paykeys/{id}/cancel",
        "label": "required params",
        "run": _smoke_case_78,
    },
    {
        "operation": "cancel",
        "method": "PUT",
        "path": "/v1/paykeys/{id}/cancel",
        "label": "all params",
        "run": _smoke_case_79,
    },
    {
        "operation": "refreshReview",
        "method": "PUT",
        "path": "/v1/paykeys/{id}/refresh_review",
        "label": "required params",
        "run": _smoke_case_80,
    },
    {
        "operation": "refreshReview",
        "method": "PUT",
        "path": "/v1/paykeys/{id}/refresh_review",
        "label": "all params",
        "run": _smoke_case_81,
    },
    {
        "operation": "refreshBalance",
        "method": "PUT",
        "path": "/v1/paykeys/{id}/refresh_balance",
        "label": "required params",
        "run": _smoke_case_82,
    },
    {
        "operation": "refreshBalance",
        "method": "PUT",
        "path": "/v1/paykeys/{id}/refresh_balance",
        "label": "all params",
        "run": _smoke_case_83,
    },
    {
        "operation": "unblock",
        "method": "PATCH",
        "path": "/v1/paykeys/{id}/unblock",
        "label": "required params",
        "run": _smoke_case_84,
    },
    {
        "operation": "unblock",
        "method": "PATCH",
        "path": "/v1/paykeys/{id}/unblock",
        "label": "all params",
        "run": _smoke_case_85,
    },
    {
        "operation": "setVerificationDecision",
        "method": "PATCH",
        "path": "/v1/paykeys/{id}/review",
        "label": "required params",
        "run": _smoke_case_86,
    },
    {
        "operation": "setVerificationDecision",
        "method": "PATCH",
        "path": "/v1/paykeys/{id}/review",
        "label": "all params",
        "run": _smoke_case_87,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/paykeys/{id}/review",
        "label": "required params",
        "run": _smoke_case_88,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/paykeys/{id}/review",
        "label": "all params",
        "run": _smoke_case_89,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/charges/{id}",
        "label": "required params",
        "run": _smoke_case_90,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/charges/{id}",
        "label": "all params",
        "run": _smoke_case_91,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/charges/{id}",
        "label": "required params",
        "run": _smoke_case_92,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/charges/{id}",
        "label": "all params",
        "run": _smoke_case_93,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/charges",
        "label": "required params",
        "run": _smoke_case_94,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/charges",
        "label": "all params",
        "run": _smoke_case_95,
    },
    {
        "operation": "hold",
        "method": "PUT",
        "path": "/v1/charges/{id}/hold",
        "label": "required params",
        "run": _smoke_case_96,
    },
    {
        "operation": "hold",
        "method": "PUT",
        "path": "/v1/charges/{id}/hold",
        "label": "all params",
        "run": _smoke_case_97,
    },
    {
        "operation": "release",
        "method": "PUT",
        "path": "/v1/charges/{id}/release",
        "label": "required params",
        "run": _smoke_case_98,
    },
    {
        "operation": "release",
        "method": "PUT",
        "path": "/v1/charges/{id}/release",
        "label": "all params",
        "run": _smoke_case_99,
    },
    {
        "operation": "cancel",
        "method": "PUT",
        "path": "/v1/charges/{id}/cancel",
        "label": "required params",
        "run": _smoke_case_100,
    },
    {
        "operation": "cancel",
        "method": "PUT",
        "path": "/v1/charges/{id}/cancel",
        "label": "all params",
        "run": _smoke_case_101,
    },
    {
        "operation": "listUnmasked",
        "method": "GET",
        "path": "/v1/charges/{id}/unmask",
        "label": "required params",
        "run": _smoke_case_102,
    },
    {
        "operation": "listUnmasked",
        "method": "GET",
        "path": "/v1/charges/{id}/unmask",
        "label": "all params",
        "run": _smoke_case_103,
    },
    {
        "operation": "resubmit",
        "method": "POST",
        "path": "/v1/charges/{id}/resubmit",
        "label": "required params",
        "run": _smoke_case_104,
    },
    {
        "operation": "resubmit",
        "method": "POST",
        "path": "/v1/charges/{id}/resubmit",
        "label": "all params",
        "run": _smoke_case_105,
    },
    {
        "operation": "refund",
        "method": "POST",
        "path": "/v1/charges/{id}/refund",
        "label": "required params",
        "run": _smoke_case_106,
    },
    {
        "operation": "refund",
        "method": "POST",
        "path": "/v1/charges/{id}/refund",
        "label": "all params",
        "run": _smoke_case_107,
    },
    {
        "operation": "uploadAuthorizationProof",
        "method": "POST",
        "path": "/v1/charges/{id}/authorization",
        "label": "required params",
        "run": _smoke_case_108,
    },
    {
        "operation": "uploadAuthorizationProof",
        "method": "POST",
        "path": "/v1/charges/{id}/authorization",
        "label": "all params",
        "run": _smoke_case_109,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/funding_events",
        "label": "required params",
        "run": _smoke_case_110,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/funding_events",
        "label": "all params",
        "run": _smoke_case_111,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/funding_events/{id}",
        "label": "required params",
        "run": _smoke_case_112,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/funding_events/{id}",
        "label": "all params",
        "run": _smoke_case_113,
    },
    {
        "operation": "simulate",
        "method": "POST",
        "path": "/v1/funding_events/simulate",
        "label": "required params",
        "run": _smoke_case_114,
    },
    {
        "operation": "simulate",
        "method": "POST",
        "path": "/v1/funding_events/simulate",
        "label": "all params",
        "run": _smoke_case_115,
    },
    {
        "operation": "listPayments",
        "method": "GET",
        "path": "/v1/funding_event_payments/{id}",
        "label": "required params",
        "run": _smoke_case_116,
    },
    {
        "operation": "listPayments",
        "method": "GET",
        "path": "/v1/funding_event_payments/{id}",
        "label": "all params",
        "run": _smoke_case_117,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/payments",
        "label": "required params",
        "run": _smoke_case_118,
    },
    {
        "operation": "list",
        "method": "GET",
        "path": "/v1/payments",
        "label": "all params",
        "run": _smoke_case_119,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/payouts/{id}",
        "label": "required params",
        "run": _smoke_case_120,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/payouts/{id}",
        "label": "all params",
        "run": _smoke_case_121,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/payouts/{id}",
        "label": "required params",
        "run": _smoke_case_122,
    },
    {
        "operation": "update",
        "method": "PUT",
        "path": "/v1/payouts/{id}",
        "label": "all params",
        "run": _smoke_case_123,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/payouts",
        "label": "required params",
        "run": _smoke_case_124,
    },
    {
        "operation": "create",
        "method": "POST",
        "path": "/v1/payouts",
        "label": "all params",
        "run": _smoke_case_125,
    },
    {
        "operation": "hold",
        "method": "PUT",
        "path": "/v1/payouts/{id}/hold",
        "label": "required params",
        "run": _smoke_case_126,
    },
    {
        "operation": "hold",
        "method": "PUT",
        "path": "/v1/payouts/{id}/hold",
        "label": "all params",
        "run": _smoke_case_127,
    },
    {
        "operation": "release",
        "method": "PUT",
        "path": "/v1/payouts/{id}/release",
        "label": "required params",
        "run": _smoke_case_128,
    },
    {
        "operation": "release",
        "method": "PUT",
        "path": "/v1/payouts/{id}/release",
        "label": "all params",
        "run": _smoke_case_129,
    },
    {
        "operation": "cancel",
        "method": "PUT",
        "path": "/v1/payouts/{id}/cancel",
        "label": "required params",
        "run": _smoke_case_130,
    },
    {
        "operation": "cancel",
        "method": "PUT",
        "path": "/v1/payouts/{id}/cancel",
        "label": "all params",
        "run": _smoke_case_131,
    },
    {
        "operation": "listUnmasked",
        "method": "GET",
        "path": "/v1/payouts/{id}/unmask",
        "label": "required params",
        "run": _smoke_case_132,
    },
    {
        "operation": "listUnmasked",
        "method": "GET",
        "path": "/v1/payouts/{id}/unmask",
        "label": "all params",
        "run": _smoke_case_133,
    },
    {
        "operation": "resubmit",
        "method": "POST",
        "path": "/v1/payouts/{id}/resubmit",
        "label": "required params",
        "run": _smoke_case_134,
    },
    {
        "operation": "resubmit",
        "method": "POST",
        "path": "/v1/payouts/{id}/resubmit",
        "label": "all params",
        "run": _smoke_case_135,
    },
    {
        "operation": "uploadAuthorizationProof",
        "method": "POST",
        "path": "/v1/payouts/{id}/authorization",
        "label": "required params",
        "run": _smoke_case_136,
    },
    {
        "operation": "uploadAuthorizationProof",
        "method": "POST",
        "path": "/v1/payouts/{id}/authorization",
        "label": "all params",
        "run": _smoke_case_137,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/account_settings/{account_id}",
        "label": "required params",
        "run": _smoke_case_138,
    },
    {
        "operation": "retrieve",
        "method": "GET",
        "path": "/v1/account_settings/{account_id}",
        "label": "all params",
        "run": _smoke_case_139,
    },
]

DEFAULT_SMOKE_CONCURRENCY = 32


def _selected_cases() -> list[SmokeCase]:
    filter_value = os.environ.get("SCALAR_SMOKE_FILTER")
    needles = [needle.strip() for needle in filter_value.split(",") if needle.strip()] if filter_value else []
    if not needles:
        return cases
    return [case for case in cases if any(needle in case["operation"] or needle in case["path"] for needle in needles)]


def _smoke_concurrency(case_count: int) -> int:
    override = os.environ.get("SCALAR_SMOKE_CONCURRENCY")
    if override:
        try:
            parsed = int(override)
            if parsed > 0:
                return min(parsed, case_count)
        except ValueError:
            pass
    return min(DEFAULT_SMOKE_CONCURRENCY, case_count)


def _case_identity(case: SmokeCase) -> SmokeResult:
    # `label` is carried through only when the operation contributed both of its calls, so a
    # single-case operation reports exactly as it did before there were two.
    identity: SmokeResult = {
        "operation": case["operation"],
        "method": case["method"],
        "path": case["path"],
    }
    label = case.get("label")
    if label:
        identity["label"] = label
    return identity


def _run_case(case: SmokeCase) -> SmokeResult:
    started_at = time.monotonic()
    identity = _case_identity(case)
    try:
        case["run"]()
        return {
            **identity,
            "status": "passed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
        }
    except Exception:
        return {
            **identity,
            "status": "failed",
            "durationMs": int((time.monotonic() - started_at) * 1000),
            "error": traceback.format_exc(),
        }


def main() -> None:
    selected = _selected_cases()
    if selected:
        # Keep enough parallelism to catch generated SDK concurrency bugs without overwhelming
        # CI runners or the in-process mock server for large SDKs.
        with ThreadPoolExecutor(max_workers=_smoke_concurrency(len(selected))) as executor:
            results = list(executor.map(_run_case, selected))
    else:
        results = []
    failed = [result for result in results if result["status"] == "failed"]

    report_path = os.environ.get("SCALAR_SMOKE_REPORT")
    if report_path:
        Path(report_path).write_text(
            json.dumps({"total": len(results), "failed": len(failed), "results": results}), encoding="utf-8"
        )
    else:
        for result in results:
            suffix = f" [{result['label']}]" if result.get("label") else ""
            if result["status"] == "passed":
                print(
                    f"PASS {result['operation']}{suffix} ({result['method']} {result['path']}) {result['durationMs']}ms"
                )
            else:
                print(
                    f"FAIL {result['operation']}{suffix} ({result['method']} {result['path']})\n{result.get('error', '')}",
                    file=sys.stderr,
                )
        if not results:
            print("No code samples ran (empty SDK or a SCALAR_SMOKE_FILTER that matched nothing).", file=sys.stderr)
        else:
            print(f"\n{len(results) - len(failed)}/{len(results)} samples passed")

    if failed or not results:
        sys.exit(1)


if __name__ == "__main__":
    main()

# Straddle Python API

Complete reference of every operation, grouped by resource. See [the README](./README.md) for usage and configuration.

## Contents

- [`Accounts`](#accounts)
  - [Get an account](#get-an-account)
  - [Update an account](#update-an-account)
  - [Create an account](#create-an-account)
  - [List accounts](#list-accounts)
  - [Onboard an account](#onboard-an-account)
  - [Simulate status transitions for a sandbox account](#simulate-status-transitions-for-a-sandbox-account)
- [`CapabilityRequests`](#capabilityrequests)
  - [Create capability requests](#create-capability-requests)
  - [List capability requests](#list-capability-requests)
- [`LinkedBankAccounts`](#linkedbankaccounts)
  - [Create a linked bank account](#create-a-linked-bank-account)
  - [List linked bank accounts](#list-linked-bank-accounts)
  - [Update a linked bank account](#update-a-linked-bank-account)
  - [Get a linked bank account](#get-a-linked-bank-account)
  - [Get an unmasked linked bank account](#get-an-unmasked-linked-bank-account)
  - [Cancel a linked bank account](#cancel-a-linked-bank-account)
- [`Organizations`](#organizations)
  - [Create an organization](#create-an-organization)
  - [List organizations](#list-organizations)
  - [Get an organization](#get-an-organization)
- [`Representatives`](#representatives)
  - [Create a representative](#create-a-representative)
  - [List representatives](#list-representatives)
  - [Update a representative](#update-a-representative)
  - [Get a representative](#get-a-representative)
  - [Get an unmasked representative](#get-an-unmasked-representative)
- [`Bridge`](#bridge)
  - [Create a paykey from bank account details](#create-a-paykey-from-bank-account-details)
  - [Create a paykey from a Plaid token](#create-a-paykey-from-a-plaid-token)
  - [Create a Bridge widget session token](#create-a-bridge-widget-session-token)
  - [Create a paykey from a Quiltt token](#create-a-paykey-from-a-quiltt-token)
- [`Customers`](#customers)
  - [Get a customer](#get-a-customer)
  - [Update a customer](#update-a-customer)
  - [Delete a customer](#delete-a-customer)
  - [List customers](#list-customers)
  - [Create a customer](#create-a-customer)
  - [Get an unmasked customer](#get-an-unmasked-customer)
  - [Refresh a customer review](#refresh-a-customer-review)
  - [`Customers Review`](#customers-review)
    - [Get a customer review](#get-a-customer-review)
    - [Set a customer verification decision](#set-a-customer-verification-decision)
- [`Paykeys`](#paykeys)
  - [Get a paykey](#get-a-paykey)
  - [Get an unmasked paykey](#get-an-unmasked-paykey)
  - [List paykeys](#list-paykeys)
  - [Reveal a paykey token](#reveal-a-paykey-token)
  - [Cancel a paykey](#cancel-a-paykey)
  - [Refresh a paykey review](#refresh-a-paykey-review)
  - [Refresh a paykey balance](#refresh-a-paykey-balance)
  - [Unblock a paykey](#unblock-a-paykey)
  - [`Paykeys Review`](#paykeys-review)
    - [Set a paykey verification decision](#set-a-paykey-verification-decision)
    - [Get a paykey review](#get-a-paykey-review)
- [`Charges`](#charges)
  - [Get a charge](#get-a-charge)
  - [Update a charge](#update-a-charge)
  - [Create a charge](#create-a-charge)
  - [Hold a charge](#hold-a-charge)
  - [Release a charge](#release-a-charge)
  - [Cancel a charge](#cancel-a-charge)
  - [Get an unmasked charge](#get-an-unmasked-charge)
  - [Resubmit a charge](#resubmit-a-charge)
  - [Refund a paid charge](#refund-a-paid-charge)
  - [Upload a proof-of-authorization document for a charge](#upload-a-proof-of-authorization-document-for-a-charge)
- [`FundingEvents`](#fundingevents)
  - [List funding events](#list-funding-events)
  - [Get a funding event](#get-a-funding-event)
  - [Simulate a funding event](#simulate-a-funding-event)
  - [List funding event payments](#list-funding-event-payments)
- [`Payments`](#payments)
  - [List payments](#list-payments)
- [`Payouts`](#payouts)
  - [Get a payout](#get-a-payout)
  - [Update a payout](#update-a-payout)
  - [Create a payout](#create-a-payout)
  - [Hold a payout](#hold-a-payout)
  - [Release a payout](#release-a-payout)
  - [Cancel a payout](#cancel-a-payout)
  - [Get an unmasked payout](#get-an-unmasked-payout)
  - [Resubmit a payout](#resubmit-a-payout)
  - [Upload a proof-of-authorization document for a payout](#upload-a-proof-of-authorization-document-for-a-payout)
- [`AccountSettings`](#accountsettings)
  - [Get account settings](#get-account-settings)

## Setup

```python
import os

from straddle import StraddleAPI

client = StraddleAPI(
    bearer=os.environ.get("BEARER"),
)
```

## `Accounts`

Accounts represent businesses that use Straddle through a platform.

### Get an account

Returns the account with the specified ID.

| Direction | Type |
| --- | --- |
| Response | [`AccountResponse`](./src/straddle/types/account_response.py) |

```python
account = client.accounts.retrieve(
    account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Update an account

Updates an account's business profile, metadata, and external ID, then returns the account.

| Direction | Type |
| --- | --- |
| Request | [`AccountUpdateParams`](./src/straddle/types/account_update_params.py) |
| Response | [`AccountResponse`](./src/straddle/types/account_response.py) |

```python
account = client.accounts.update(
    account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    business_profile={"name": "", "website": "https://example.com"},
)
```

### Create an account

Creates a business account in the specified organization and returns the account.

| Direction | Type |
| --- | --- |
| Request | [`AccountCreateParams`](./src/straddle/types/account_create_params.py) |
| Response | [`AccountResponse`](./src/straddle/types/account_response.py) |

```python
account = client.accounts.create(
    organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    account_type="business",
    business_profile={"name": "", "website": "https://example.com"},
    access_level="standard",
)
```

### List accounts

Returns a paginated list of accounts for your platform. Filter the list by status, type, external ID, or text search.

| Direction | Type |
| --- | --- |
| Request | [`AccountListParams`](./src/straddle/types/account_list_params.py) |
| Response | [`AccountList`](./src/straddle/types/account_list.py) |

```python
account = client.accounts.list(
    page_number=1,
    page_size=100,
    sort_by="id",
    sort_order="asc",
)
```

### Onboard an account

Starts onboarding and records the account's acceptance of Straddle's Terms of Service. The account must have at least one representative and one linked bank account. This operation also moves all associated representatives and linked bank accounts to `onboarding`.

| Direction | Type |
| --- | --- |
| Request | [`AccountOnboardParams`](./src/straddle/types/account_onboard_params.py) |
| Response | [`AccountResponse`](./src/straddle/types/account_response.py) |

```python
account = client.accounts.onboard(
    account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    terms_of_service={"accepted_date": "2024-01-01T00:00:00.000Z", "agreement_url": "", "agreement_type": "embedded"},
)
```

### Simulate status transitions for a sandbox account

Simulates an account status transition to `onboarding` or `active` in the sandbox and returns the account.

| Direction | Type |
| --- | --- |
| Request | [`AccountSimulateOnboardingParams`](./src/straddle/types/account_simulate_onboarding_params.py) |
| Response | [`AccountResponse`](./src/straddle/types/account_response.py) |

```python
account = client.accounts.simulate_onboarding(
    account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

## `CapabilityRequests`

Capability requests change the payment, customer, and consent types available to an account.

### Create capability requests

Creates one or more capability requests for an account and returns the resulting requests.

| Direction | Type |
| --- | --- |
| Request | [`CapabilityRequestCreateParams`](./src/straddle/types/capability_request_create_params.py) |
| Response | [`CapabilityRequestList`](./src/straddle/types/capability_request_list.py) |

```python
capability_request = client.capability_requests.create(
    account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### List capability requests

Returns a paginated list of capability requests for an account. Filter the list by capability type, category, or status.

| Direction | Type |
| --- | --- |
| Request | [`CapabilityRequestListParams`](./src/straddle/types/capability_request_list_params.py) |
| Response | [`CapabilityRequestList`](./src/straddle/types/capability_request_list.py) |

```python
capability_request = client.capability_requests.list(
    account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    page_number=1,
    page_size=100,
    sort_by="id",
    sort_order="asc",
)
```

## `LinkedBankAccounts`

Linked bank accounts connect external bank accounts to an account or platform for charges, payouts, or billing.

### Create a linked bank account

Creates a linked bank account for an account or platform, assigns its payment purposes, and returns the linked bank account.

| Direction | Type |
| --- | --- |
| Request | [`LinkedBankAccountCreateParams`](./src/straddle/types/linked_bank_account_create_params.py) |
| Response | [`LinkedBankAccountResponse`](./src/straddle/types/linked_bank_account_response.py) |

```python
linked_bank_account = client.linked_bank_accounts.create(
    bank_account={"account_holder": "", "routing_number": "xxxxxxxxx", "account_number": ""},
)
```

### List linked bank accounts

Returns a paginated list of linked bank accounts. Filter the list by account, scope, purpose, or status.

| Direction | Type |
| --- | --- |
| Request | [`LinkedBankAccountListParams`](./src/straddle/types/linked_bank_account_list_params.py) |
| Response | [`LinkedBankAccountList`](./src/straddle/types/linked_bank_account_list.py) |

```python
linked_bank_account = client.linked_bank_accounts.list(
    page_number=1,
    page_size=100,
    sort_by="id",
    sort_order="asc",
)
```

### Update a linked bank account

Updates bank account details and metadata, then returns the linked bank account. The linked bank account must have status `created`, or status `onboarding` with `status_detail.reason` set to `stuck`.

| Direction | Type |
| --- | --- |
| Request | [`LinkedBankAccountUpdateParams`](./src/straddle/types/linked_bank_account_update_params.py) |
| Response | [`LinkedBankAccountResponse`](./src/straddle/types/linked_bank_account_response.py) |

```python
linked_bank_account = client.linked_bank_accounts.update(
    linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    bank_account={"account_holder": "", "routing_number": "xxxxxxxxx", "account_number": ""},
)
```

### Get a linked bank account

Returns the linked bank account with the specified ID. The response masks the account number.

| Direction | Type |
| --- | --- |
| Response | [`LinkedBankAccountResponse`](./src/straddle/types/linked_bank_account_response.py) |

```python
linked_bank_account = client.linked_bank_accounts.retrieve(
    linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Get an unmasked linked bank account

Returns the linked bank account with the specified ID without masking its account number. This endpoint is available only when Straddle enables data unmasking for the account.

| Direction | Type |
| --- | --- |
| Response | [`UnmaskedLinkedBankAccountResponse`](./src/straddle/types/unmasked_linked_bank_account_response.py) |

```python
linked_bank_account = client.linked_bank_accounts.list_unmasked(
    linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Cancel a linked bank account

Cancels a linked bank account and returns it with status `canceled`. The linked bank account must have status `created`.

| Direction | Type |
| --- | --- |
| Response | [`LinkedBankAccountResponse`](./src/straddle/types/linked_bank_account_response.py) |

```python
linked_bank_account = client.linked_bank_accounts.cancel(
    linked_bank_account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

## `Organizations`

Organizations group related Straddle accounts.

### Create an organization

Creates an organization for your platform and returns it. Organizations group related accounts and users.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationCreateParams`](./src/straddle/types/organization_create_params.py) |
| Response | [`OrganizationResponse`](./src/straddle/types/organization_response.py) |

```python
organization = client.organizations.create(
    name="",
)
```

### List organizations

Returns a paginated list of organizations for your platform. Filter the list by name or external ID.

| Direction | Type |
| --- | --- |
| Request | [`OrganizationListParams`](./src/straddle/types/organization_list_params.py) |
| Response | [`OrganizationList`](./src/straddle/types/organization_list.py) |

```python
organization = client.organizations.list(
    page_number=1,
    page_size=100,
    sort_by="id",
    sort_order="asc",
)
```

### Get an organization

Returns the organization with the specified ID.

| Direction | Type |
| --- | --- |
| Response | [`OrganizationResponse`](./src/straddle/types/organization_response.py) |

```python
organization = client.organizations.retrieve(
    organization_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

## `Representatives`

Representatives are people associated with a business account for ownership, control, or authorization purposes.

### Create a representative

Creates a representative for an account and returns the representative. Relationship fields identify primary representatives, control persons, and owners.

| Direction | Type |
| --- | --- |
| Request | [`RepresentativeCreateParams`](./src/straddle/types/representative_create_params.py) |
| Response | [`RepresentativeResponse`](./src/straddle/types/representative_response.py) |

```python
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
```

### List representatives

Returns a paginated list of representatives. Filter the list by account, organization, platform, or scope.

| Direction | Type |
| --- | --- |
| Request | [`RepresentativeListParams`](./src/straddle/types/representative_list_params.py) |
| Response | [`RepresentativeList`](./src/straddle/types/representative_list.py) |

```python
representative = client.representatives.list(
    page_number=1,
    page_size=100,
    sort_by="id",
    sort_order="asc",
)
```

### Update a representative

Updates a representative's personal, contact, relationship, external ID, and metadata fields, then returns the representative.

| Direction | Type |
| --- | --- |
| Request | [`RepresentativeUpdateParams`](./src/straddle/types/representative_update_params.py) |
| Response | [`RepresentativeResponse`](./src/straddle/types/representative_response.py) |

```python
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
```

### Get a representative

Returns the representative with the specified ID.

| Direction | Type |
| --- | --- |
| Response | [`RepresentativeResponse`](./src/straddle/types/representative_response.py) |

```python
representative = client.representatives.retrieve(
    representative_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Get an unmasked representative

Returns the representative with the specified ID without masking sensitive fields. This endpoint requires an administrator role.

| Direction | Type |
| --- | --- |
| Response | [`UnmaskedRepresentativeResponse`](./src/straddle/types/unmasked_representative_response.py) |

```python
representative = client.representatives.list_unmasked(
    representative_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

## `Bridge`

Bridge connects customer bank accounts and creates paykeys from supported provider tokens or bank account details.

### Create a paykey from bank account details

Creates a paykey from a routing number, account number, and account type.

| Direction | Type |
| --- | --- |
| Request | [`BridgeCreateBankAccountPaykeyParams`](./src/straddle/types/bridge_create_bank_account_paykey_params.py) |
| Response | [`PaykeyResponse`](./src/straddle/types/paykey_response.py) |

```python
bridge = client.bridge.create_bank_account_paykey(
    customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    routing_number="xxxxxxxxx",
    account_number="",
    account_type="checking",
)
```

### Create a paykey from a Plaid token

Creates a paykey from a Plaid processor token.

| Direction | Type |
| --- | --- |
| Request | [`BridgeCreatePlaidPaykeyParams`](./src/straddle/types/bridge_create_plaid_paykey_params.py) |
| Response | [`PaykeyResponse`](./src/straddle/types/paykey_response.py) |

```python
bridge = client.bridge.create_plaid_paykey(
    customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    plaid_token="",
)
```

### Create a Bridge widget session token

Creates a session token for the Bridge widget.

| Direction | Type |
| --- | --- |
| Request | [`BridgeCreateTokenParams`](./src/straddle/types/bridge_create_token_params.py) |
| Response | [`BridgeTokenResponse`](./src/straddle/types/bridge_token_response.py) |

```python
bridge = client.bridge.create_token(
    customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Create a paykey from a Quiltt token

Creates a paykey from a Quiltt processor token.

| Direction | Type |
| --- | --- |
| Request | [`BridgeCreateQuilttPaykeyParams`](./src/straddle/types/bridge_create_quiltt_paykey_params.py) |
| Response | [`RevealedPaykeyResponse`](./src/straddle/types/revealed_paykey_response.py) |

```python
bridge = client.bridge.create_quiltt_paykey(
    customer_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    quiltt_token="",
)
```

## `Customers`

Customers are individuals or businesses that send or receive payments through your integration.

### Get a customer

Returns a customer by `id`.

| Direction | Type |
| --- | --- |
| Response | [`CustomerResponse`](./src/straddle/types/customer_response.py) |

```python
customer = client.customers.retrieve(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Update a customer

Updates an existing customer's profile, status, and metadata.

| Direction | Type |
| --- | --- |
| Request | [`CustomerUpdateParams`](./src/straddle/types/customer_update_params.py) |
| Response | [`CustomerResponse`](./src/straddle/types/customer_response.py) |

```python
customer = client.customers.update(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    name="",
    email="user@example.com",
    phone="",
    device={"ip_address": "192.168.1.1"},
    status="verified",
)
```

### Delete a customer

Permanently deletes a customer record. The deletion cannot be undone. Use this endpoint only to meet regulatory or privacy requirements.

| Direction | Type |
| --- | --- |
| Response | [`CustomerResponse`](./src/straddle/types/customer_response.py) |

```python
customer = client.customers.delete(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### List customers

Returns a paginated list of customers for the account. Optional query parameters filter, search, and sort the results.

| Direction | Type |
| --- | --- |
| Request | [`CustomerListParams`](./src/straddle/types/customer_list_params.py) |
| Response | [`CustomerSummaryList`](./src/straddle/types/customer_summary_list.py) |

```python
customer = client.customers.list(
    page_number=1,
    page_size=100,
    sort_order="asc",
)
```

### Create a customer

Creates a customer and starts identity, fraud, and risk assessments.

| Direction | Type |
| --- | --- |
| Request | [`CustomerCreateParams`](./src/straddle/types/customer_create_params.py) |
| Response | [`CustomerResponse`](./src/straddle/types/customer_response.py) |

```python
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
```

### Get an unmasked customer

Returns unmasked details for a customer, including personally identifiable information. Straddle must enable this endpoint for your account. Use this endpoint only when unmasked data is necessary.

| Direction | Type |
| --- | --- |
| Response | [`UnmaskedCustomerResponse`](./src/straddle/types/unmasked_customer_response.py) |

```python
customer = client.customers.list_unmasked(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Refresh a customer review

Starts a new identity review for a customer. The review runs asynchronously. Webhooks and the customer review endpoint return updated results.

| Direction | Type |
| --- | --- |
| Response | [`CustomerResponse`](./src/straddle/types/customer_response.py) |

```python
customer = client.customers.refresh_review(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### `Customers Review`

Customers are individuals or businesses that send or receive payments through your integration.

#### Get a customer review

Returns the results of a customer's identity and fraud review. The response includes decisions, risk and correlation scores, reason codes, watchlist matches, and network alerts.

| Direction | Type |
| --- | --- |
| Response | [`CustomerReviewResponse`](./src/straddle/types/customers/customer_review_response.py) |

```python
review = client.customers.review.list(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

#### Set a customer verification decision

Updates the verification decision for a customer. The customer's current `status` must be `review`.

| Direction | Type |
| --- | --- |
| Request | [`ReviewSetVerificationDecisionParams`](./src/straddle/types/customers/review_set_verification_decision_params.py) |
| Response | [`CustomerResponse`](./src/straddle/types/customer_response.py) |

```python
review = client.customers.review.set_verification_decision(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    status="verified",
)
```

## `Paykeys`

A paykey links a verified customer to a bank account without exposing bank account details. Use a paykey to create charges and payouts.

### Get a paykey

Returns a paykey by `id`, including the masked paykey value and bank account details.

| Direction | Type |
| --- | --- |
| Response | [`PaykeyResponse`](./src/straddle/types/paykey_response.py) |

```python
paykey = client.paykeys.retrieve(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Get an unmasked paykey

Returns a paykey by `id`, including the full paykey value and unmasked bank account details. Straddle must enable this endpoint for your account. Use this endpoint only when unmasked data is necessary.

| Direction | Type |
| --- | --- |
| Response | [`UnmaskedPaykeyResponse`](./src/straddle/types/unmasked_paykey_response.py) |

```python
paykey = client.paykeys.list_unmasked(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### List paykeys

Returns a paginated list of paykeys for the account. Optional query parameters filter, search, and sort the results.

| Direction | Type |
| --- | --- |
| Request | [`PaykeyListParams`](./src/straddle/types/paykey_list_params.py) |
| Response | [`PaykeySummaryList`](./src/straddle/types/paykey_summary_list.py) |

```python
paykey = client.paykeys.list(
    page_number=1,
    page_size=100,
    sort_order="asc",
)
```

### Reveal a paykey token

Returns a paykey by `id`, including the full paykey value and masked bank account details.

| Direction | Type |
| --- | --- |
| Response | [`RevealedPaykeyResponse`](./src/straddle/types/revealed_paykey_response.py) |

```python
paykey = client.paykeys.reveal(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Cancel a paykey

Cancels a paykey so it cannot be used for new payments.

| Direction | Type |
| --- | --- |
| Request | [`PaykeyCancelParams`](./src/straddle/types/paykey_cancel_params.py) |
| Response | [`PaykeyResponse`](./src/straddle/types/paykey_response.py) |

```python
paykey = client.paykeys.cancel(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Refresh a paykey review

Starts a new verification review for a paykey. The review runs asynchronously. Webhooks and the paykey review endpoint return updated results.

| Direction | Type |
| --- | --- |
| Response | [`PaykeyResponse`](./src/straddle/types/paykey_response.py) |

```python
paykey = client.paykeys.refresh_review(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Refresh a paykey balance

Starts an asynchronous balance refresh for a paykey. The response returns the paykey before the refresh finishes.

| Direction | Type |
| --- | --- |
| Response | [`PaykeyResponse`](./src/straddle/types/paykey_response.py) |

```python
paykey = client.paykeys.refresh_balance(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Unblock a paykey

Unblocks a paykey that was blocked by an `R29` return. The paykey must not have been unblocked before.

| Direction | Type |
| --- | --- |
| Request | [`PaykeyUnblockParams`](./src/straddle/types/paykey_unblock_params.py) |
| Response | [`PaykeyResponse`](./src/straddle/types/paykey_response.py) |

```python
paykey = client.paykeys.unblock(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### `Paykeys Review`

A paykey links a verified customer to a bank account without exposing bank account details. Use a paykey to create charges and payouts.

#### Set a paykey verification decision

Updates the verification decision for a paykey. The paykey's current `status` must be `review`.

| Direction | Type |
| --- | --- |
| Request | [`ReviewSetVerificationDecisionParams`](./src/straddle/types/paykeys/review_set_verification_decision_params.py) |
| Response | [`PaykeyResponse`](./src/straddle/types/paykey_response.py) |

```python
review = client.paykeys.review.set_verification_decision(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    status="active",
)
```

#### Get a paykey review

Returns a paykey verification review, including the decision, score breakdowns, and result codes.

| Direction | Type |
| --- | --- |
| Response | [`PaykeyReviewResponse`](./src/straddle/types/paykeys/paykey_review_response.py) |

```python
review = client.paykeys.review.list(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

## `Charges`

Charges debit a customer's bank account through a paykey.

### Get a charge

Returns a charge by its unique identifier.

| Direction | Type |
| --- | --- |
| Response | [`ChargeResponse`](./src/straddle/types/charge_response.py) |

```python
charge = client.charges.retrieve(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Update a charge

Updates the description, amount, `payment_date`, or metadata. The charge must have a status of `created` or `on_hold`.

| Direction | Type |
| --- | --- |
| Request | [`ChargeUpdateParams`](./src/straddle/types/charge_update_params.py) |
| Response | [`ChargeResponse`](./src/straddle/types/charge_response.py) |

```python
charge = client.charges.update(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    description="Monthly subscription fee",
    amount=10000,
    payment_date="2024-01-01",
)
```

### Create a charge

Creates a charge against a customer's paykey. Straddle submits the charge for processing on `payment_date` unless the charge is on hold.

| Direction | Type |
| --- | --- |
| Request | [`ChargeCreateParams`](./src/straddle/types/charge_create_params.py) |
| Response | [`ChargeResponse`](./src/straddle/types/charge_response.py) |

```python
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
```

### Hold a charge

Places a charge on hold to prevent submission for processing. The charge must have a status of `created` or `scheduled`.

| Direction | Type |
| --- | --- |
| Request | [`ChargeHoldParams`](./src/straddle/types/charge_hold_params.py) |
| Response | [`ChargeResponse`](./src/straddle/types/charge_response.py) |

```python
charge = client.charges.hold(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Release a charge

Releases a charge from `on_hold` and returns it to `created` for submission on `payment_date`.

| Direction | Type |
| --- | --- |
| Request | [`ChargeReleaseParams`](./src/straddle/types/charge_release_params.py) |
| Response | [`ChargeResponse`](./src/straddle/types/charge_response.py) |

```python
charge = client.charges.release(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Cancel a charge

Cancels a charge. The charge must have a status of `created`, `scheduled`, or `on_hold`.

| Direction | Type |
| --- | --- |
| Request | [`ChargeCancelParams`](./src/straddle/types/charge_cancel_params.py) |
| Response | [`ChargeResponse`](./src/straddle/types/charge_response.py) |

```python
charge = client.charges.cancel(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Get an unmasked charge

Return a charge with its sensitive fields unmasked.

| Direction | Type |
| --- | --- |
| Response | [`UnmaskedChargeResponse`](./src/straddle/types/unmasked_charge_response.py) |

```python
charge = client.charges.list_unmasked(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Resubmit a charge

Creates a new charge from a failed, reversed, or cancelled charge. The request can override `description`, `external_id`, and `payment_date`. Other payment details come from the original charge.

| Direction | Type |
| --- | --- |
| Request | [`ChargeResubmitParams`](./src/straddle/types/charge_resubmit_params.py) |
| Response | [`ChargeResponse`](./src/straddle/types/charge_response.py) |

```python
charge = client.charges.resubmit(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Refund a paid charge

Creates a payout to return funds from a paid charge to the customer's bank account. The payout is linked to the charge through `related_payments`. A charge can be refunded once, either fully or partially.

| Direction | Type |
| --- | --- |
| Request | [`ChargeRefundParams`](./src/straddle/types/charge_refund_params.py) |
| Response | [`PayoutResponse`](./src/straddle/types/payout_response.py) |

```python
charge = client.charges.refund(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Upload a proof-of-authorization document for a charge

Uploads a proof-of-authorization document for a charge. A later upload adds another document and does not replace an existing one.

| Direction | Type |
| --- | --- |
| Request | [`ChargeUploadAuthorizationProofParams`](./src/straddle/types/charge_upload_authorization_proof_params.py) |
| Response | [`ChargeResponse`](./src/straddle/types/charge_response.py) |

```python
charge = client.charges.upload_authorization_proof(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    file=b"",
)
```

## `FundingEvents`

Funding events group charge and payout activity into transfers between Straddle and your linked bank account.

### List funding events

Returns a paginated list of funding events that match the specified filters.

| Direction | Type |
| --- | --- |
| Request | [`FundingEventListParams`](./src/straddle/types/funding_event_list_params.py) |
| Response | [`FundingEventSummaryList`](./src/straddle/types/funding_event_summary_list.py) |

```python
funding_event = client.funding_events.list(
    page_number=1,
    page_size=100,
    sort_order="asc",
)
```

### Get a funding event

Returns a funding event by its unique identifier, including its current status, status history, and linked bank account details when available.

| Direction | Type |
| --- | --- |
| Response | [`FundingEventResponse`](./src/straddle/types/funding_event_response.py) |

```python
funding_event = client.funding_events.retrieve(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Simulate a funding event

Creates a funding event for unfunded charge or payout activity in the sandbox and returns its ID. This endpoint is unavailable in production.

| Direction | Type |
| --- | --- |
| Request | [`FundingEventSimulateParams`](./src/straddle/types/funding_event_simulate_params.py) |
| Response | [`FundingEventSimulation`](./src/straddle/types/funding_event_simulation.py) |

```python
funding_event = client.funding_events.simulate(
    funding_event_job_type="charges",
)
```

### List funding event payments

Returns a paginated list of payments included in the funding event.

| Direction | Type |
| --- | --- |
| Request | [`FundingEventListPaymentsParams`](./src/straddle/types/funding_event_list_payments_params.py) |
| Response | [`FundingEventPaymentList`](./src/straddle/types/funding_event_payment_list.py) |

```python
funding_event = client.funding_events.list_payments(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    default_sort_order="asc",
    sort_order="asc",
)
```

## `Payments`

Payments provide a combined view of charges and payouts.

### List payments

Returns a paged list of charges and payouts that match the filters.

| Direction | Type |
| --- | --- |
| Request | [`PaymentListParams`](./src/straddle/types/payment_list_params.py) |
| Response | [`PaymentSummaryList`](./src/straddle/types/payment_summary_list.py) |

```python
payment = client.payments.list(
    page_number=1,
    page_size=100,
    sort_by="id",
    sort_order="asc",
    default_sort="id",
    default_sort_order="asc",
)
```

## `Payouts`

Payouts send money to a customer's bank account through a paykey.

### Get a payout

Returns a payout by its unique identifier.

| Direction | Type |
| --- | --- |
| Response | [`PayoutResponse`](./src/straddle/types/payout_response.py) |

```python
payout = client.payouts.retrieve(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Update a payout

Updates the description, amount, `payment_date`, or metadata. The payout must have a status of `created` or `on_hold`.

| Direction | Type |
| --- | --- |
| Request | [`PayoutUpdateParams`](./src/straddle/types/payout_update_params.py) |
| Response | [`PayoutResponse`](./src/straddle/types/payout_response.py) |

```python
payout = client.payouts.update(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    description="",
    amount=10000,
    payment_date="2024-01-01",
)
```

### Create a payout

Creates a payout to a customer's bank account. Straddle submits the payout for processing on `payment_date` unless the payout is on hold.

| Direction | Type |
| --- | --- |
| Request | [`PayoutCreateParams`](./src/straddle/types/payout_create_params.py) |
| Response | [`PayoutResponse`](./src/straddle/types/payout_response.py) |

```python
payout = client.payouts.create(
    paykey="",
    description="Vendor invoice payment",
    amount=10000,
    currency="USD",
    payment_date="2024-01-01",
    device={"ip_address": "192.168.1.1"},
    external_id="",
)
```

### Hold a payout

Places a payout on hold to prevent submission for processing. The payout must have a status of `created` or `scheduled`.

| Direction | Type |
| --- | --- |
| Request | [`PayoutHoldParams`](./src/straddle/types/payout_hold_params.py) |
| Response | [`PayoutResponse`](./src/straddle/types/payout_response.py) |

```python
payout = client.payouts.hold(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Release a payout

Releases a payout from `on_hold` and returns it to `created` for submission on `payment_date`.

| Direction | Type |
| --- | --- |
| Request | [`PayoutReleaseParams`](./src/straddle/types/payout_release_params.py) |
| Response | [`PayoutResponse`](./src/straddle/types/payout_response.py) |

```python
payout = client.payouts.release(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Cancel a payout

Cancels a payout. The payout must have a status of `created`, `scheduled`, or `on_hold`.

| Direction | Type |
| --- | --- |
| Request | [`PayoutCancelParams`](./src/straddle/types/payout_cancel_params.py) |
| Response | [`PayoutResponse`](./src/straddle/types/payout_response.py) |

```python
payout = client.payouts.cancel(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Get an unmasked payout

Return a payout with its sensitive fields unmasked.

| Direction | Type |
| --- | --- |
| Response | [`UnmaskedPayoutResponse`](./src/straddle/types/unmasked_payout_response.py) |

```python
payout = client.payouts.list_unmasked(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Resubmit a payout

Creates a new payout from a failed, reversed, or cancelled payout. The request can override `description`, `external_id`, and `payment_date`. Other payment details come from the original payout.

| Direction | Type |
| --- | --- |
| Request | [`PayoutResubmitParams`](./src/straddle/types/payout_resubmit_params.py) |
| Response | [`PayoutResponse`](./src/straddle/types/payout_response.py) |

```python
payout = client.payouts.resubmit(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

### Upload a proof-of-authorization document for a payout

Uploads a proof-of-authorization document for a payout. A later upload adds another document and does not replace an existing one.

| Direction | Type |
| --- | --- |
| Request | [`PayoutUploadAuthorizationProofParams`](./src/straddle/types/payout_upload_authorization_proof_params.py) |
| Response | [`PayoutResponse`](./src/straddle/types/payout_response.py) |

```python
payout = client.payouts.upload_authorization_proof(
    id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
    file=b"",
)
```

## `AccountSettings`

Account settings define payment limits, capabilities, statement details, and policy controls for an account.

### Get account settings

Returns all effective settings for the account, including values inherited from its organization, platform, and system defaults.

| Direction | Type |
| --- | --- |
| Response | [`AccountSettingsResponse`](./src/straddle/types/account_settings_response.py) |

```python
account_setting = client.account_settings.retrieve(
    account_id="7c9e6679-7425-40de-944b-e07fc1f90ae7",
)
```

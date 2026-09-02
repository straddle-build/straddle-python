# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .account_created_v1_webhook_event import AccountCreatedV1WebhookEvent
from .account_event_v1_webhook_event import AccountEventV1WebhookEvent
from .representative_event_v1_webhook_event import RepresentativeEventV1WebhookEvent
from .representative_created_v1_webhook_event import RepresentativeCreatedV1WebhookEvent
from .linked_bank_account_event_v1_webhook_event import LinkedBankAccountEventV1WebhookEvent
from .linked_bank_account_created_v1_webhook_event import LinkedBankAccountCreatedV1WebhookEvent
from .capability_request_event_v1_webhook_event import CapabilityRequestEventV1WebhookEvent
from .capability_request_created_v1_webhook_event import CapabilityRequestCreatedV1WebhookEvent
from .customer_event_v1_webhook_event import CustomerEventV1WebhookEvent
from .customer_created_v1_webhook_event import CustomerCreatedV1WebhookEvent
from .paykey_event_v1_webhook_event import PaykeyEventV1WebhookEvent
from .paykey_created_v1_webhook_event import PaykeyCreatedV1WebhookEvent
from .charge_created_v1_webhook_event import ChargeCreatedV1WebhookEvent
from .charge_event_v1_webhook_event import ChargeEventV1WebhookEvent
from .payout_created_v1_webhook_event import PayoutCreatedV1WebhookEvent
from .payout_event_v1_webhook_event import PayoutEventV1WebhookEvent
from .platform_event_v1_webhook_event import PlatformEventV1WebhookEvent
from .platform_created_v1_webhook_event import PlatformCreatedV1WebhookEvent
from .user_event_v1_webhook_event import UserEventV1WebhookEvent
from .user_created_v1_webhook_event import UserCreatedV1WebhookEvent
from .funding_event_created_v1_webhook_event import FundingEventCreatedV1WebhookEvent
from .funding_event_event_v1_webhook_event import FundingEventEventV1WebhookEvent

__all__ = ["ParsedWebhookEvent"]


ParsedWebhookEvent: TypeAlias = Union[
    AccountCreatedV1WebhookEvent,
    AccountEventV1WebhookEvent,
    RepresentativeEventV1WebhookEvent,
    RepresentativeCreatedV1WebhookEvent,
    LinkedBankAccountEventV1WebhookEvent,
    LinkedBankAccountCreatedV1WebhookEvent,
    CapabilityRequestEventV1WebhookEvent,
    CapabilityRequestCreatedV1WebhookEvent,
    CustomerEventV1WebhookEvent,
    CustomerCreatedV1WebhookEvent,
    PaykeyEventV1WebhookEvent,
    PaykeyCreatedV1WebhookEvent,
    ChargeCreatedV1WebhookEvent,
    ChargeEventV1WebhookEvent,
    PayoutCreatedV1WebhookEvent,
    PayoutEventV1WebhookEvent,
    PlatformEventV1WebhookEvent,
    PlatformCreatedV1WebhookEvent,
    UserEventV1WebhookEvent,
    UserCreatedV1WebhookEvent,
    FundingEventCreatedV1WebhookEvent,
    FundingEventEventV1WebhookEvent,
]

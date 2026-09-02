# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["RepresentativeRelationshipParam"]


class RepresentativeRelationshipParam(TypedDict, total=False):
    primary: Required[bool]
    """Whether this person is the account's primary representative. The primary representative provides personal and business information and accepts the services agreement. An account can have only one primary representative."""

    control: Required[bool]
    """Whether the representative controls, manages, or directs the business. Each legal entity must have one representative with `control` set to `true`."""

    owner: Required[bool]
    """Whether the representative owns any equity in the business."""

    percent_ownership: Optional[float]
    """The representative's ownership percentage. Required when `owner` is `true`."""

    title: Optional[str]
    """The representative's job title."""

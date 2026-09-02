# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["RepresentativeRelationship"]


class RepresentativeRelationship(BaseModel):
    primary: bool
    """Whether this person is the account's primary representative. The primary representative provides personal and business information and accepts the services agreement. An account can have only one primary representative."""

    control: bool
    """Whether the representative controls, manages, or directs the business. Each legal entity must have one representative with `control` set to `true`."""

    owner: bool
    """Whether the representative owns any equity in the business."""

    percent_ownership: Optional[float] = None
    """The representative's ownership percentage. Required when `owner` is `true`."""

    title: Optional[str] = None
    """The representative's job title."""

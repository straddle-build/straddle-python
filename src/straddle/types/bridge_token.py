# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .._models import BaseModel

__all__ = ["BridgeToken"]


class BridgeToken(BaseModel):
    bridge_token: str
    """JSON Web Token (JWT) for the Bridge widget."""

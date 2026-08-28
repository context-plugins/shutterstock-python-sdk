from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OauthAccessTokenResponse(SdkBaseModel):
    """Access token response to client apps"""

    access_token: str
    """Access token that can be used for future requests"""

    expires_in: Optional[int] = UNSET
    """Number of seconds before token expires, only present for expiring tokens"""

    token_type: str
    """Type of token"""

    refresh_token: Optional[str] = UNSET
    """A refresh token that can be used to renew the access_token when it expires, only present for expiring tokens"""

    user_token: Optional[str] = UNSET
    """Metadata about the access_token, only present for expiring tokens"""


class OauthAccessTokenResponseDict(TypedDict):
    access_token: str
    expires_in: NotRequired[int]
    token_type: str
    refresh_token: NotRequired[str]
    user_token: NotRequired[str]

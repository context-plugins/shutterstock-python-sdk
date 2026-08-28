from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.realm import RealmOrStr


class AccessTokenDetails(SdkBaseModel):
    """Access token details that are currently associated with this user"""

    client_id: Optional[str] = UNSET
    """Client ID that is associated with the user"""

    contributor_id: Optional[str] = UNSET
    """Contributor ID that is associated with the user"""

    customer_id: Optional[str] = UNSET
    """Customer ID that is associated with the user"""

    expires_in: Optional[int] = UNSET
    """Number of seconds until the access token expires; no expiration if this value is null"""

    organization_id: Optional[str] = UNSET
    """Organization ID that is associated with the user"""

    realm: Optional[RealmOrStr] = UNSET
    """Type of access token"""

    scopes: Optional[list[str]] = UNSET
    """Scopes that this access token provides when used as authentication"""

    user_id: Optional[str] = UNSET
    """User ID that is associated with the user"""

    username: Optional[str] = UNSET
    """User name that is associated with the user"""


class AccessTokenDetailsDict(TypedDict):
    client_id: NotRequired[str]
    contributor_id: NotRequired[str]
    customer_id: NotRequired[str]
    expires_in: NotRequired[int]
    organization_id: NotRequired[str]
    realm: NotRequired[RealmOrStr]
    scopes: NotRequired[list[str]]
    user_id: NotRequired[str]
    username: NotRequired[str]

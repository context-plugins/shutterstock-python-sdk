from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UserDetails(SdkBaseModel):
    """User details"""

    contributor_id: Optional[str] = UNSET
    """Unique internal identifier of the user, as a contributor"""

    customer_id: Optional[str] = UNSET
    """Unique internal identifier of the user, as a purchaser"""

    email: Optional[str] = UNSET
    """Email address of the user"""

    first_name: Optional[str] = UNSET
    """First name of the user"""

    full_name: Optional[str] = UNSET
    """Full name including first, middle, and last name of the user"""

    id: Optional[str] = UNSET
    """Unique internal identifier for the user, not tied to contributor or purchasing customer"""

    is_premier: Optional[bool] = UNSET
    """True if the user has access to the Premier collection, false otherwise"""

    is_premier_parent: Optional[bool] = UNSET
    """True if the user has access to the Premier collection and also has child users"""

    language: Optional[str] = UNSET
    """Main language of the user account"""

    last_name: Optional[str] = UNSET
    """Last name of the user"""

    only_enhanced_license: Optional[bool] = UNSET
    """True if the user has an enterprise license, false otherwise"""

    only_sensitive_use: Optional[bool] = UNSET
    """True if the user has access to sensitive use only, false otherwise"""

    organization_id: Optional[str] = UNSET
    """Unique internal identifier for the user's organization, specific to Premier users"""

    premier_permissions: Optional[list[str]] = UNSET
    """List of permissions allowed through the Premier client"""

    username: Optional[str] = UNSET
    """User name associated to the user"""


class UserDetailsDict(TypedDict):
    contributor_id: NotRequired[str]
    customer_id: NotRequired[str]
    email: NotRequired[str]
    first_name: NotRequired[str]
    full_name: NotRequired[str]
    id: NotRequired[str]
    is_premier: NotRequired[bool]
    is_premier_parent: NotRequired[bool]
    language: NotRequired[str]
    last_name: NotRequired[str]
    only_enhanced_license: NotRequired[bool]
    only_sensitive_use: NotRequired[bool]
    organization_id: NotRequired[str]
    premier_permissions: NotRequired[list[str]]
    username: NotRequired[str]

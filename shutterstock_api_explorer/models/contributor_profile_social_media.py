from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ContributorProfileSocialMedia(SdkBaseModel):
    """Contributor profile social media links"""

    facebook: Optional[str] = UNSET
    """Facebook link for contributor"""

    google_plus: Optional[str] = UNSET
    """Google+ link for contributor"""

    linkedin: Optional[str] = UNSET
    """LinkedIn link for contributor"""

    pinterest: Optional[str] = UNSET
    """Pinterest page for contributor"""

    tumblr: Optional[str] = UNSET
    """Tumblr link for contributor"""

    twitter: Optional[str] = UNSET
    """Twitter link for contributor"""


class ContributorProfileSocialMediaDict(TypedDict):
    facebook: NotRequired[str]
    google_plus: NotRequired[str]
    linkedin: NotRequired[str]
    pinterest: NotRequired[str]
    tumblr: NotRequired[str]
    twitter: NotRequired[str]

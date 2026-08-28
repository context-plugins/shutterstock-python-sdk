from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .contributor_profile_social_media import ContributorProfileSocialMedia, ContributorProfileSocialMediaDict


class ContributorProfile(SdkBaseModel):
    """Contributor profile data"""

    about: Optional[str] = UNSET
    """Short description of the contributors' library"""

    contributor_type: Optional[list[str]] = UNSET
    """Type of content that the contributor specializes in (photographer, illustrator, etc)"""

    display_name: Optional[str] = UNSET
    """Preferred name to be displayed for the contributor"""

    equipment: Optional[list[str]] = UNSET
    """List of equipment used by the contributor (Canon EOS 5D Mark II, etc)"""

    id: str
    """Contributor ID"""

    location: Optional[str] = UNSET
    """Country code representing the contributor's locale"""

    portfolio_url: Optional[str] = UNSET
    """Web URL for the contributors' profile"""

    social_media: Optional[ContributorProfileSocialMedia] = UNSET
    """Contributor profile social media links"""

    styles: Optional[list[str]] = UNSET
    """List of styles that the contributor specializes in (lifestyle, mixed media, etc)"""

    subjects: Optional[list[str]] = UNSET
    """Generic list of subjects for contributors' work (food_and_drink, holiday, people, etc)"""

    website: Optional[str] = UNSET
    """Personal website for the contributor"""


class ContributorProfileDict(TypedDict):
    about: NotRequired[str]
    contributor_type: NotRequired[list[str]]
    display_name: NotRequired[str]
    equipment: NotRequired[list[str]]
    id: str
    location: NotRequired[str]
    portfolio_url: NotRequired[str]
    social_media: NotRequired[ContributorProfileSocialMedia | ContributorProfileSocialMediaDict]
    styles: NotRequired[list[str]]
    subjects: NotRequired[list[str]]
    website: NotRequired[str]

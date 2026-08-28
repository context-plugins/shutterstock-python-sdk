from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, RFC3339DateTime, SdkBaseModel
from .contributor import Contributor, ContributorDict
from .sfxassets import Sfxassets, SfxassetsDict


class Sfx(SdkBaseModel):
    """SFX metadata"""

    added_date: Optional[Date] = UNSET
    """Date this sound effect was added to the Shutterstock library"""

    affiliate_url: Optional[str] = UNSET
    """Affiliate referral link; appears only for registered affiliate partners"""

    artist: Optional[str] = UNSET
    """Artist of the sound effect"""

    assets: Optional[Sfxassets] = UNSET
    """Files that are available as part of an sound effect asset"""

    contributor: Contributor
    """Information about a contributor"""

    description: Optional[str] = UNSET
    """Description of this sound effect"""

    duration: Optional[float] = UNSET
    """Duration of this sound effect in seconds"""

    id: str
    """Shutterstock ID of this sound effect"""

    keywords: Optional[list[str]] = UNSET
    """List of all keywords for this sound effect"""

    media_type: str
    """Media type of this track; should always be "sfx"
    """

    releases: Optional[list[str]] = UNSET
    """List of all releases of this sound effect"""

    title: Optional[str] = UNSET
    """Title of this sound effect"""

    updated_time: Optional[RFC3339DateTime] = UNSET
    """Time this sound effect was last updated"""

    url: Optional[str] = UNSET


class SfxDict(TypedDict):
    added_date: NotRequired[Date]
    affiliate_url: NotRequired[str]
    artist: NotRequired[str]
    assets: NotRequired[Sfxassets | SfxassetsDict]
    contributor: Contributor | ContributorDict
    description: NotRequired[str]
    duration: NotRequired[float]
    id: str
    keywords: NotRequired[list[str]]
    media_type: str
    releases: NotRequired[list[str]]
    title: NotRequired[str]
    updated_time: NotRequired[RFC3339DateTime]
    url: NotRequired[str]

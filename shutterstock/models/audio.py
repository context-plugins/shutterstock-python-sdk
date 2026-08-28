from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, RFC3339DateTime, SdkBaseModel
from .album import Album, AlbumDict
from .artist import Artist, ArtistDict
from .audio_assets import AudioAssets, AudioAssetsDict
from .contributor import Contributor, ContributorDict
from .model_release import ModelRelease, ModelReleaseDict


class Audio(SdkBaseModel):
    """Audio metadata"""

    added_date: Optional[Date] = UNSET
    """Date this track was added to the Shutterstock library"""

    affiliate_url: Optional[str] = UNSET
    """Affiliate referral link; appears only for registered affiliate partners"""

    album: Optional[Album] = UNSET
    """Album metadata"""

    artists: Optional[list[Artist]] = UNSET
    """List of artists"""

    assets: Optional[AudioAssets] = UNSET
    """Files that are available as part of an audio asset"""

    bpm: Optional[int] = UNSET
    """BPM (beats per minute) of this track"""

    contributor: Contributor
    """Information about a contributor"""

    deleted_time: Optional[RFC3339DateTime] = UNSET
    description: Optional[str] = UNSET
    """Description of this track"""

    duration: Optional[float] = UNSET
    """Duration of this track in seconds"""

    genres: Optional[list[str]] = UNSET
    """List of all genres for this track"""

    id: str
    """Shutterstock ID of this track"""

    instruments: Optional[list[str]] = UNSET
    """List of all instruments that appear in this track"""

    is_adult: Optional[bool] = UNSET
    """Whether or not this track contains adult content"""

    is_instrumental: Optional[bool] = UNSET
    """Whether or not this track is purely instrumental (lacking lyrics)"""

    isrc: Optional[str] = UNSET
    keywords: Optional[list[str]] = UNSET
    """List of all keywords for this track"""

    language: Optional[str] = UNSET
    """Language of this track's lyrics"""

    lyrics: Optional[str] = UNSET
    """Lyrics of this track"""

    media_type: str
    """Media type of this track; should always be "audio"
    """

    model_releases: Optional[list[ModelRelease]] = UNSET
    """List of all model releases for this track"""

    moods: Optional[list[str]] = UNSET
    """List of all moods of this track"""

    published_time: Optional[RFC3339DateTime] = UNSET
    """Time this track was published"""

    recording_version: Optional[str] = UNSET
    """Recording version of this track"""

    releases: Optional[list[str]] = UNSET
    """List of all releases of this track"""

    similar_artists: Optional[list[Artist]] = UNSET
    """List of all similar artists of this track"""

    submitted_time: Optional[RFC3339DateTime] = UNSET
    """Time this track was submitted"""

    title: Optional[str] = UNSET
    """Title of this track"""

    updated_time: Optional[RFC3339DateTime] = UNSET
    """Time this track was last updated"""

    vocal_description: Optional[str] = UNSET
    """Vocal description of this track"""

    url: Optional[str] = UNSET


class AudioDict(TypedDict):
    added_date: NotRequired[Date]
    affiliate_url: NotRequired[str]
    album: NotRequired[Album | AlbumDict]
    artists: NotRequired[list[Artist | ArtistDict]]
    assets: NotRequired[AudioAssets | AudioAssetsDict]
    bpm: NotRequired[int]
    contributor: Contributor | ContributorDict
    deleted_time: NotRequired[RFC3339DateTime]
    description: NotRequired[str]
    duration: NotRequired[float]
    genres: NotRequired[list[str]]
    id: str
    instruments: NotRequired[list[str]]
    is_adult: NotRequired[bool]
    is_instrumental: NotRequired[bool]
    isrc: NotRequired[str]
    keywords: NotRequired[list[str]]
    language: NotRequired[str]
    lyrics: NotRequired[str]
    media_type: str
    model_releases: NotRequired[list[ModelRelease | ModelReleaseDict]]
    moods: NotRequired[list[str]]
    published_time: NotRequired[RFC3339DateTime]
    recording_version: NotRequired[str]
    releases: NotRequired[list[str]]
    similar_artists: NotRequired[list[Artist | ArtistDict]]
    submitted_time: NotRequired[RFC3339DateTime]
    title: NotRequired[str]
    updated_time: NotRequired[RFC3339DateTime]
    vocal_description: NotRequired[str]
    url: NotRequired[str]

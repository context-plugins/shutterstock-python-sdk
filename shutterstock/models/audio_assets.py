from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .audio_asset_details import AudioAssetDetails, AudioAssetDetailsDict
from .shorts_loops_stems import ShortsLoopsStems, ShortsLoopsStemsDict


class AudioAssets(SdkBaseModel):
    """Files that are available as part of an audio asset"""

    album_art: Optional[AudioAssetDetails] = UNSET
    """Information about a file that is part of an audio asset"""

    clean_audio: Optional[AudioAssetDetails] = UNSET
    """Information about a file that is part of an audio asset"""

    original_audio: Optional[AudioAssetDetails] = UNSET
    """Information about a file that is part of an audio asset"""

    preview_mp3: Optional[AudioAssetDetails] = UNSET
    """Information about a file that is part of an audio asset"""

    preview_ogg: Optional[AudioAssetDetails] = UNSET
    """Information about a file that is part of an audio asset"""

    waveform: Optional[AudioAssetDetails] = UNSET
    """Information about a file that is part of an audio asset"""

    shorts_loops_stems: Optional[ShortsLoopsStems] = UNSET
    """Links for Shorts, Loops and Stems previews"""


class AudioAssetsDict(TypedDict):
    album_art: NotRequired[AudioAssetDetails | AudioAssetDetailsDict]
    clean_audio: NotRequired[AudioAssetDetails | AudioAssetDetailsDict]
    original_audio: NotRequired[AudioAssetDetails | AudioAssetDetailsDict]
    preview_mp3: NotRequired[AudioAssetDetails | AudioAssetDetailsDict]
    preview_ogg: NotRequired[AudioAssetDetails | AudioAssetDetailsDict]
    waveform: NotRequired[AudioAssetDetails | AudioAssetDetailsDict]
    shorts_loops_stems: NotRequired[ShortsLoopsStems | ShortsLoopsStemsDict]

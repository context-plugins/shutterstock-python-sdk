from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class License1(str, Enum):
    """Type of license"""

    AUDIO_PLATFORM = "audio_platform"
    PREMIER_MUSIC_BASIC = "premier_music_basic"
    PREMIER_MUSIC_EXTENDED = "premier_music_extended"
    PREMIER_MUSIC_PRO = "premier_music_pro"
    PREMIER_MUSIC_COMP = "premier_music_comp"
    ASSET_ALL_MUSIC = "asset_all_music"

    __str__ = str.__str__


License1OrStr: TypeAlias = Annotated[License1 | str, open_enum_validator(License1)]

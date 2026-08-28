from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class License3(str, Enum):
    """License agreement to use for licensing"""

    PREMIER_EDITORIAL_VIDEO_DIGITAL_ONLY = "premier_editorial_video_digital_only"
    PREMIER_EDITORIAL_VIDEO_ALL_MEDIA = "premier_editorial_video_all_media"
    PREMIER_EDITORIAL_VIDEO_ALL_MEDIA_SINGLE_TERRITORY = "premier_editorial_video_all_media_single_territory"
    PREMIER_EDITORIAL_VIDEO_COMP = "premier_editorial_video_comp"

    __str__ = str.__str__


License3OrStr: TypeAlias = Annotated[License3 | str, open_enum_validator(License3)]

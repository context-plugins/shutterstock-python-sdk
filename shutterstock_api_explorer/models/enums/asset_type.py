from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AssetType(str, Enum):
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    ELEMENTS = "elements"
    EDITORIAL_IMAGE = "editorial-image"
    EDITORIAL_VIDEO = "editorial-video"

    __str__ = str.__str__


AssetTypeOrStr: TypeAlias = Annotated[AssetType | str, open_enum_validator(AssetType)]

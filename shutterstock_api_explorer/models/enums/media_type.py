from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MediaType(str, Enum):
    """Media type of the license"""

    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    EDITORIAL = "editorial"

    __str__ = str.__str__


MediaTypeOrStr: TypeAlias = Annotated[MediaType | str, open_enum_validator(MediaType)]

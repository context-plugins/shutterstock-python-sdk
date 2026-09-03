from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type(str, Enum):
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    EDITORIAL_IMAGE = "editorial-image"
    EDITORIAL_VIDEO = "editorial-video"

    __str__ = str.__str__


TypeOrStr: TypeAlias = Annotated[Type | str, open_enum_validator(Type)]

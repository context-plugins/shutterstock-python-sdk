from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ImageType2(str, Enum):
    PHOTO = "photo"
    ILLUSTRATION = "illustration"
    VECTOR = "vector"

    __str__ = str.__str__


ImageType2OrStr: TypeAlias = Annotated[ImageType2 | str, open_enum_validator(ImageType2)]

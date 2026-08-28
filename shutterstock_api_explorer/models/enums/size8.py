from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Size8(str, Enum):
    """Size of the video being licensed"""

    WEB = "web"
    SD = "sd"
    HD = "hd"
    _4K = "4k"

    __str__ = str.__str__


Size8OrStr: TypeAlias = Annotated[Size8 | str, open_enum_validator(Size8)]

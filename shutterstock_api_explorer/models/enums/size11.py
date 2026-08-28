from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Size11(str, Enum):
    """Size of the video"""

    WEB = "web"
    SD = "sd"
    HD = "hd"
    _4K = "4k"

    __str__ = str.__str__


Size11OrStr: TypeAlias = Annotated[Size11 | str, open_enum_validator(Size11)]

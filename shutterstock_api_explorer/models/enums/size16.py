from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Size16(str, Enum):
    WEB = "web"
    SD = "sd"
    HD = "hd"
    _4K = "4k"

    __str__ = str.__str__


Size16OrStr: TypeAlias = Annotated[Size16 | str, open_enum_validator(Size16)]

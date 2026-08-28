from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AspectRatio(str, Enum):
    _4_3 = "4_3"
    _16_9 = "16_9"
    NONSTANDARD = "nonstandard"

    __str__ = str.__str__


AspectRatioOrStr: TypeAlias = Annotated[AspectRatio | str, open_enum_validator(AspectRatio)]

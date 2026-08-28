from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Size10(str, Enum):
    """Size of the image"""

    SMALL = "small"
    MEDIUM = "medium"
    HUGE = "huge"
    SUPERSIZE = "supersize"
    VECTOR = "vector"

    __str__ = str.__str__


Size10OrStr: TypeAlias = Annotated[Size10 | str, open_enum_validator(Size10)]

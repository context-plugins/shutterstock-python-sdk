from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Size4(str, Enum):
    """Image size to download"""

    SMALL = "small"
    MEDIUM = "medium"
    HUGE = "huge"
    CUSTOM = "custom"

    __str__ = str.__str__


Size4OrStr: TypeAlias = Annotated[Size4 | str, open_enum_validator(Size4)]

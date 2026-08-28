from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Size12(str, Enum):
    SMALL = "small"
    MEDIUM = "medium"
    HUGE = "huge"
    VECTOR = "vector"
    CUSTOM = "custom"

    __str__ = str.__str__


Size12OrStr: TypeAlias = Annotated[Size12 | str, open_enum_validator(Size12)]

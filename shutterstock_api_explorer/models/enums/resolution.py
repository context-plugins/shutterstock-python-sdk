from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Resolution(str, Enum):
    _4K = "4k"
    STANDARD_DEFINITION = "standard_definition"
    HIGH_DEFINITION = "high_definition"

    __str__ = str.__str__


ResolutionOrStr: TypeAlias = Annotated[Resolution | str, open_enum_validator(Resolution)]

from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Visibility(str, Enum):
    PRIVATE = "private"
    PUBLIC = "public"

    __str__ = str.__str__


VisibilityOrStr: TypeAlias = Annotated[Visibility | str, open_enum_validator(Visibility)]

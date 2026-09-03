from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Orientation2(str, Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"

    __str__ = str.__str__


Orientation2OrStr: TypeAlias = Annotated[Orientation2 | str, open_enum_validator(Orientation2)]

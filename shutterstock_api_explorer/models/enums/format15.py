from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Format15(str, Enum):
    EPS = "eps"
    JPG = "jpg"

    __str__ = str.__str__


Format15OrStr: TypeAlias = Annotated[Format15 | str, open_enum_validator(Format15)]

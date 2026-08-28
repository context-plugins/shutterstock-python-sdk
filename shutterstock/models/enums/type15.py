from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type15(str, Enum):
    EDIT = "edit"
    ADDITION = "addition"

    __str__ = str.__str__


Type15OrStr: TypeAlias = Annotated[Type15 | str, open_enum_validator(Type15)]

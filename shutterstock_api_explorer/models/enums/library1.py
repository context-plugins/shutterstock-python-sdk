from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Library1(str, Enum):
    SHUTTERSTOCK = "shutterstock"
    PREMIER = "premier"

    __str__ = str.__str__


Library1OrStr: TypeAlias = Annotated[Library1 | str, open_enum_validator(Library1)]

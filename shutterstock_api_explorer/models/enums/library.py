from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Library(str, Enum):
    SHUTTERSTOCK = "shutterstock"
    OFFSET = "offset"

    __str__ = str.__str__


LibraryOrStr: TypeAlias = Annotated[Library | str, open_enum_validator(Library)]

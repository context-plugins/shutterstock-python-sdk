from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Library2(str, Enum):
    SHUTTERSTOCK = "shutterstock"
    PREMIER = "premier"
    PREMIUMBEAT = "premiumbeat"

    __str__ = str.__str__


Library2OrStr: TypeAlias = Annotated[Library2 | str, open_enum_validator(Library2)]

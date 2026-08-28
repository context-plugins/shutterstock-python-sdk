from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class View2(str, Enum):
    MINIMAL = "minimal"
    FULL = "full"

    __str__ = str.__str__


View2OrStr: TypeAlias = Annotated[View2 | str, open_enum_validator(View2)]

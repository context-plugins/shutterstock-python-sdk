from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort17(str, Enum):
    RELEVANT = "relevant"
    NEWEST = "newest"
    OLDEST = "oldest"

    __str__ = str.__str__


Sort17OrStr: TypeAlias = Annotated[Sort17 | str, open_enum_validator(Sort17)]

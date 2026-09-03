from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort5(str, Enum):
    NEWEST = "newest"
    OLDEST = "oldest"

    __str__ = str.__str__


Sort5OrStr: TypeAlias = Annotated[Sort5 | str, open_enum_validator(Sort5)]

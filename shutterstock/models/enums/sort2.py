from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort2(str, Enum):
    NEWEST = "newest"
    POPULAR = "popular"
    RELEVANCE = "relevance"
    RANDOM = "random"

    __str__ = str.__str__


Sort2OrStr: TypeAlias = Annotated[Sort2 | str, open_enum_validator(Sort2)]

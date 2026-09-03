from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort15(str, Enum):
    POPULAR = "popular"
    NEWEST = "newest"
    RELEVANCE = "relevance"
    RANDOM = "random"
    OLDEST = "oldest"

    __str__ = str.__str__


Sort15OrStr: TypeAlias = Annotated[Sort15 | str, open_enum_validator(Sort15)]

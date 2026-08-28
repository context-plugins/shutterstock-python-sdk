from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort24(str, Enum):
    NEWEST = "newest"
    LAST_UPDATED = "last_updated"
    ITEM_COUNT = "item_count"

    __str__ = str.__str__


Sort24OrStr: TypeAlias = Annotated[Sort24 | str, open_enum_validator(Sort24)]

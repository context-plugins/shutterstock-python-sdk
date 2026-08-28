from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Size6(str, Enum):
    """Image size to download"""

    VECTOR = "vector"

    __str__ = str.__str__


Size6OrStr: TypeAlias = Annotated[Size6 | str, open_enum_validator(Size6)]

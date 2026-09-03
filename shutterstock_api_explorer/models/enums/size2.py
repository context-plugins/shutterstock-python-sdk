from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Size2(str, Enum):
    """Asset size to download"""

    ORIGINAL = "original"

    __str__ = str.__str__


Size2OrStr: TypeAlias = Annotated[Size2 | str, open_enum_validator(Size2)]

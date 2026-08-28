from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Format9(str, Enum):
    """(Deprecated) Image format to download"""

    EPS = "eps"

    __str__ = str.__str__


Format9OrStr: TypeAlias = Annotated[Format9 | str, open_enum_validator(Format9)]

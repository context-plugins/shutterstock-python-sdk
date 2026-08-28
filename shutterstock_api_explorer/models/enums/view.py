from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class View(str, Enum):
    """Amount of detail to render in the response"""

    MINIMAL = "minimal"
    FULL = "full"

    __str__ = str.__str__


ViewOrStr: TypeAlias = Annotated[View | str, open_enum_validator(View)]

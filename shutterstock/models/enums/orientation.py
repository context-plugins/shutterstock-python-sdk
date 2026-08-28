from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Orientation(str, Enum):
    """Show image results with horizontal or vertical orientation"""

    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"

    __str__ = str.__str__


OrientationOrStr: TypeAlias = Annotated[Orientation | str, open_enum_validator(Orientation)]

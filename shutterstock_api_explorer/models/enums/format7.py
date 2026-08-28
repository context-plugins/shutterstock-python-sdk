from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Format7(str, Enum):
    """(Deprecated) Image format to download"""

    JPG = "jpg"

    __str__ = str.__str__


Format7OrStr: TypeAlias = Annotated[Format7 | str, open_enum_validator(Format7)]

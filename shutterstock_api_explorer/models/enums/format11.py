from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Format11(str, Enum):
    WAV = "wav"
    MP3 = "mp3"

    __str__ = str.__str__


Format11OrStr: TypeAlias = Annotated[Format11 | str, open_enum_validator(Format11)]

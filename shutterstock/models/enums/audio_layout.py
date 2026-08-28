from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AudioLayout(str, Enum):
    AMBISONIC = "ambisonic"
    _5_1 = "5.1"
    STEREO = "stereo"

    __str__ = str.__str__


AudioLayoutOrStr: TypeAlias = Annotated[AudioLayout | str, open_enum_validator(AudioLayout)]

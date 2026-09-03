from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort12(str, Enum):
    SCORE = "score"
    RANKING_ALL = "ranking_all"
    ARTIST = "artist"
    TITLE = "title"
    BPM = "bpm"
    FRESHNESS = "freshness"
    DURATION = "duration"

    __str__ = str.__str__


Sort12OrStr: TypeAlias = Annotated[Sort12 | str, open_enum_validator(Sort12)]

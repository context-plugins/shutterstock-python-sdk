from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PeopleEthnicity5(str, Enum):
    AFRICAN = "african"
    AFRICAN_AMERICAN = "african_american"
    BLACK = "black"
    BRAZILIAN = "brazilian"
    CHINESE = "chinese"
    CAUCASIAN = "caucasian"
    EAST_ASIAN = "east_asian"
    HISPANIC = "hispanic"
    JAPANESE = "japanese"
    MIDDLE_EASTERN = "middle_eastern"
    NATIVE_AMERICAN = "native_american"
    PACIFIC_ISLANDER = "pacific_islander"
    SOUTH_ASIAN = "south_asian"
    SOUTHEAST_ASIAN = "southeast_asian"
    OTHER = "other"

    __str__ = str.__str__


PeopleEthnicity5OrStr: TypeAlias = Annotated[PeopleEthnicity5 | str, open_enum_validator(PeopleEthnicity5)]

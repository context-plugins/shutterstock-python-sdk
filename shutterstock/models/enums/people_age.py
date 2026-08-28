from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PeopleAge(str, Enum):
    """Show images that feature people of the specified age category"""

    INFANTS = "infants"
    CHILDREN = "children"
    TEENAGERS = "teenagers"
    _20S = "20s"
    _30S = "30s"
    _40S = "40s"
    _50S = "50s"
    _60S = "60s"
    OLDER = "older"

    __str__ = str.__str__


PeopleAgeOrStr: TypeAlias = Annotated[PeopleAge | str, open_enum_validator(PeopleAge)]

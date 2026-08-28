from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PeopleGender2(str, Enum):
    MALE = "male"
    FEMALE = "female"
    BOTH = "both"

    __str__ = str.__str__


PeopleGender2OrStr: TypeAlias = Annotated[PeopleGender2 | str, open_enum_validator(PeopleGender2)]

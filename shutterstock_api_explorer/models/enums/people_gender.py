from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PeopleGender(str, Enum):
    """Show images with people of the specified gender"""

    MALE = "male"
    FEMALE = "female"
    BOTH = "both"

    __str__ = str.__str__


PeopleGenderOrStr: TypeAlias = Annotated[PeopleGender | str, open_enum_validator(PeopleGender)]

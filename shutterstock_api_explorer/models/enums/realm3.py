from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Realm3(str, Enum):
    """User type to be authorized (usually 'customer')"""

    CUSTOMER = "customer"
    CONTRIBUTOR = "contributor"

    __str__ = str.__str__


Realm3OrStr: TypeAlias = Annotated[Realm3 | str, open_enum_validator(Realm3)]

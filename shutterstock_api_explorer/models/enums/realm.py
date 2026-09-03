from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Realm(str, Enum):
    """Type of access token"""

    CUSTOMER = "customer"
    CONTRIBUTOR = "contributor"

    __str__ = str.__str__


RealmOrStr: TypeAlias = Annotated[Realm | str, open_enum_validator(Realm)]

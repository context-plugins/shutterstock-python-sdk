from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Realm2(str, Enum):
    CUSTOMER = "customer"
    CONTRIBUTOR = "contributor"

    __str__ = str.__str__


Realm2OrStr: TypeAlias = Annotated[Realm2 | str, open_enum_validator(Realm2)]

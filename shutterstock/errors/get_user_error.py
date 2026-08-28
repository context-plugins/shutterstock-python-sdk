from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetUserErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetUserError:
    def map(self, response: HttpResponse) -> GetUserErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_user_error_mapper: Final[ErrorMapper[GetUserErrorBody]] = _GetUserError()

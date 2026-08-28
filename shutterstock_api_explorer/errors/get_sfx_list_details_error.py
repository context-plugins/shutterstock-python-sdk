from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetSfxListDetailsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetSfxListDetailsError:
    def map(self, response: HttpResponse) -> GetSfxListDetailsErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_sfx_list_details_error_mapper: Final[ErrorMapper[GetSfxListDetailsErrorBody]] = _GetSfxListDetailsError()

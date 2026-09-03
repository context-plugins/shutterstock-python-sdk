from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetSfxDetailsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetSfxDetailsError:
    def map(self, response: HttpResponse) -> GetSfxDetailsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 503:
                return RawError(response)
            case _:
                return RawError(response)


get_sfx_details_error_mapper: Final[ErrorMapper[GetSfxDetailsErrorBody]] = _GetSfxDetailsError()

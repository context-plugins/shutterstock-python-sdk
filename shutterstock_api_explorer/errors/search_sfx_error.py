from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

SearchSfxErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _SearchSfxError:
    def map(self, response: HttpResponse) -> SearchSfxErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 503:
                return RawError(response)
            case _:
                return RawError(response)


search_sfx_error_mapper: Final[ErrorMapper[SearchSfxErrorBody]] = _SearchSfxError()

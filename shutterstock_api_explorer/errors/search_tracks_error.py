from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

SearchTracksErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _SearchTracksError:
    def map(self, response: HttpResponse) -> SearchTracksErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


search_tracks_error_mapper: Final[ErrorMapper[SearchTracksErrorBody]] = _SearchTracksError()

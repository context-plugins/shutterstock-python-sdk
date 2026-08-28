from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

SearchVideosErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _SearchVideosError:
    def map(self, response: HttpResponse) -> SearchVideosErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return RawError(response)
            case _:
                return RawError(response)


search_videos_error_mapper: Final[ErrorMapper[SearchVideosErrorBody]] = _SearchVideosError()

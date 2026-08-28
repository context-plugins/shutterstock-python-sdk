from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

SearchEditorialVideosErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _SearchEditorialVideosError:
    def map(self, response: HttpResponse) -> SearchEditorialVideosErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 406:
                return RawError(response)
            case _:
                return RawError(response)


search_editorial_videos_error_mapper: Final[ErrorMapper[SearchEditorialVideosErrorBody]] = _SearchEditorialVideosError()

from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

ListEditorialVideosErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _ListEditorialVideosError:
    def map(self, response: HttpResponse) -> ListEditorialVideosErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


list_editorial_videos_error_mapper: Final[ErrorMapper[ListEditorialVideosErrorBody]] = _ListEditorialVideosError()

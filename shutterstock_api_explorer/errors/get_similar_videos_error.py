from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetSimilarVideosErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetSimilarVideosError:
    def map(self, response: HttpResponse) -> GetSimilarVideosErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_similar_videos_error_mapper: Final[ErrorMapper[GetSimilarVideosErrorBody]] = _GetSimilarVideosError()

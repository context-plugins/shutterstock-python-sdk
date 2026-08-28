from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

FindSimilarVideosErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _FindSimilarVideosError:
    def map(self, response: HttpResponse) -> FindSimilarVideosErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


find_similar_videos_error_mapper: Final[ErrorMapper[FindSimilarVideosErrorBody]] = _FindSimilarVideosError()

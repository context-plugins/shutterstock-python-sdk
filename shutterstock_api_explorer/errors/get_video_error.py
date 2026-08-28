from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetVideoErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetVideoError:
    def map(self, response: HttpResponse) -> GetVideoErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return RawError(response)
            case _:
                return RawError(response)


get_video_error_mapper: Final[ErrorMapper[GetVideoErrorBody]] = _GetVideoError()

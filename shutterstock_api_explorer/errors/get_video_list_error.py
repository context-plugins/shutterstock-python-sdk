from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetVideoListErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetVideoListError:
    def map(self, response: HttpResponse) -> GetVideoListErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_video_list_error_mapper: Final[ErrorMapper[GetVideoListErrorBody]] = _GetVideoListError()

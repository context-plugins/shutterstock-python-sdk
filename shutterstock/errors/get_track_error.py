from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetTrackErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetTrackError:
    def map(self, response: HttpResponse) -> GetTrackErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_track_error_mapper: Final[ErrorMapper[GetTrackErrorBody]] = _GetTrackError()

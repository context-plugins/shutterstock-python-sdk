from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetTrackListErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetTrackListError:
    def map(self, response: HttpResponse) -> GetTrackListErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


get_track_list_error_mapper: Final[ErrorMapper[GetTrackListErrorBody]] = _GetTrackListError()

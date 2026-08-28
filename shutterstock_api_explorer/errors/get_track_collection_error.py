from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetTrackCollectionErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetTrackCollectionError:
    def map(self, response: HttpResponse) -> GetTrackCollectionErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return RawError(response)
            case _:
                return RawError(response)


get_track_collection_error_mapper: Final[ErrorMapper[GetTrackCollectionErrorBody]] = _GetTrackCollectionError()

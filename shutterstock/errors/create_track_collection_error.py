from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

CreateTrackCollectionErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _CreateTrackCollectionError:
    def map(self, response: HttpResponse) -> CreateTrackCollectionErrorBody:
        match response.status_code:
            case 400 | 401 | 403:
                return RawError(response)
            case _:
                return RawError(response)


create_track_collection_error_mapper: Final[ErrorMapper[CreateTrackCollectionErrorBody]] = _CreateTrackCollectionError()

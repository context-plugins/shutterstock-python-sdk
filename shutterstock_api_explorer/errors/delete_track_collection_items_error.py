from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeleteTrackCollectionItemsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteTrackCollectionItemsError:
    def map(self, response: HttpResponse) -> DeleteTrackCollectionItemsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return RawError(response)
            case _:
                return RawError(response)


delete_track_collection_items_error_mapper: Final[
    ErrorMapper[DeleteTrackCollectionItemsErrorBody]
] = _DeleteTrackCollectionItemsError()

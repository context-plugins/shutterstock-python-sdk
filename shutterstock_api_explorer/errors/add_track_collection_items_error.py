from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

AddTrackCollectionItemsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _AddTrackCollectionItemsError:
    def map(self, response: HttpResponse) -> AddTrackCollectionItemsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return RawError(response)
            case _:
                return RawError(response)


add_track_collection_items_error_mapper: Final[
    ErrorMapper[AddTrackCollectionItemsErrorBody]
] = _AddTrackCollectionItemsError()

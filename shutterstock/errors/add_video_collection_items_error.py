from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

AddVideoCollectionItemsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _AddVideoCollectionItemsError:
    def map(self, response: HttpResponse) -> AddVideoCollectionItemsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return RawError(response)
            case _:
                return RawError(response)


add_video_collection_items_error_mapper: Final[
    ErrorMapper[AddVideoCollectionItemsErrorBody]
] = _AddVideoCollectionItemsError()

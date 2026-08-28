from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetImageCollectionItemsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetImageCollectionItemsError:
    def map(self, response: HttpResponse) -> GetImageCollectionItemsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404:
                return RawError(response)
            case _:
                return RawError(response)


get_image_collection_items_error_mapper: Final[
    ErrorMapper[GetImageCollectionItemsErrorBody]
] = _GetImageCollectionItemsError()
